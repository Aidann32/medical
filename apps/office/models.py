from django.db import models


class Patient(models.Model):
    GENDERS = (
        ('Male', 'Мужской'), 
        ('Female', 'Женский')
    )

    first_name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Имя')
    last_name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Фамилия')
    iin = models.CharField(max_length=12, blank=False, null=False, verbose_name='ИИН', unique=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=16, verbose_name='Номер телефона', blank=True, null=True, unique=True)
    gender = models.CharField(null=True, blank=False, verbose_name='Пол', choices=GENDERS, max_length=12)
    birth_date = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'


class Diagnosis(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False, verbose_name='Название диагноза')
    description = models.TextField(verbose_name='Описание диагноза', null=True, blank=True)
    treatment = models.TextField(verbose_name='Способ лечения', null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Пациент')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Диагноз'
        verbose_name_plural = 'Диагнозы'
