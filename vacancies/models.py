from django.db import models


class Vacancy(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Айди вакансии')
    name = models.CharField(verbose_name='Название вакансии', max_length=300)
    alternate_url = models.CharField(verbose_name='Ссылка на представление вакансии на сайте', max_length=2000)
    apply_alternate_url = models.CharField(verbose_name='Ссылка на отклик на вакансию на сайте', max_length=2000)
    published_at = models.DateTimeField(verbose_name='Дата и время публикации вакансии')


class Experience(models.Model):
    id = models.CharField(primary_key=True, verbose_name='Айди опыта', max_length=150)
    name = models.CharField(verbose_name='Выбор опыта', max_length=150)

    def __str__(self):
        return self.name


class Employment(models.Model):
    id = models.CharField(primary_key=True, verbose_name='Айди занятости', max_length=150)
    name = models.CharField(verbose_name='Выбор занятости', max_length=150)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    id = models.CharField(primary_key=True, verbose_name='Айди графика работы', max_length=150)
    name = models.CharField(verbose_name='Выбор графика работы', max_length=150)

    def __str__(self):
        return self.name
