from django.shortcuts import render
from django.http import HttpResponse
from .forms import VacanciesForm
from .models import Vacancy
import requests


def search_vacancies(request):
    if request.method == 'POST':
        form = VacanciesForm(request.POST)
        if form.is_valid():
            return vacancy_analysis(request, form.cleaned_data)
    else:
        form = VacanciesForm()
    return render(request, 'vacancies/vacancy_analysis.html', {'form': form})


def vacancy_analysis(request, data):
    parametrs = {
        'text': data.get('vacancy_name'),
        'experience': data['experience'].id,
        'employment': data['employment'].id,
        'schedule': data['schedule'].id
    }
    response = requests.get('https://api.hh.ru/vacancies', params=parametrs)
    response_json = response.json()

    vacancies = []
    for item in response_json.get('items'):
        vacancies.append(Vacancy(id=item.get('id'), name=item.get('name'), alternate_url=item.get('alternate_url'),
                                 apply_alternate_url=item.get('apply_alternate_url'),
                                 published_at=item.get('published_at')))
    Vacancy.objects.bulk_create(vacancies, ignore_conflicts=True)

    return render(request, 'vacancies/analysis_result.html',
                  {'found': response_json.get('found')})
# response_json.get('found')
