from django import forms
from .models import *


class VacanciesForm(forms.Form):
    vacancy_name = forms.CharField(max_length=150, label='Название вакансии',
                                   widget=forms.TextInput(attrs={"class": "form-control"}))
    experience = forms.ModelChoiceField(queryset=Experience.objects.all(), label='Опыт работы',
                                        widget=forms.Select(attrs={"class": "form-control"}))
    employment = forms.ModelChoiceField(queryset=Employment.objects.all(), label='Тип занятости',
                                        widget=forms.Select(attrs={"class": "form-control"}))
    schedule = forms.ModelChoiceField(queryset=Schedule.objects.all(), label='График работы',
                                      widget=forms.Select(attrs={"class": "form-control"}))
