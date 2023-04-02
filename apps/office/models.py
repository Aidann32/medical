from django.db import models

from apps.profiles.models import Profile
from .exceptions import ProfileNotDoctorException

class Patient(models.Model):
    GENDERS = (
        ('Male', 'Мужской'), 
        ('Female', 'Женский')
    )

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Аккаунт')
    first_name = models.CharField(max_length=255, blank=False, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=255, blank=False, null=True, verbose_name='Фамилия')
    iin = models.CharField(max_length=12, blank=False, null=True, verbose_name='ИИН', unique=True)
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


class XRay(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Пациент')
    photo = models.ImageField(upload_to='xrays/', verbose_name='Рентгеновский снимок')
    result = models.CharField(max_length=1024, null=True, blank=True, verbose_name='Результат')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.patient}: {self.created_at}'

    def save(self, *args, **kwargs):
        if not self.pk:
            # If instance is newly created
            # TODO: Check in ML backend and save to self.result
            self.result = "Test result"

        super(XRay, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Снимок пациента'
        verbose_name_plural = 'Снимки пациентов'


class XRayRequest(models.Model):
    x_ray = models.ForeignKey(XRay, on_delete=models.CASCADE, verbose_name='Рентгеновский снимок')
    doctor = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Доктор')
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Диагноз')
    doctor_comment = models.TextField(verbose_name='Комментарий доктора', null=True, blank=True)
    is_answered = models.BooleanField(default=False, verbose_name='Отвечен ли доктором')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.x_ray}: {self.doctor}'

    def save(self, *args, **kwargs):
        if doctor.role != 1:
            raise ProfileNotDoctorException()
        
        super(XRayRequest, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заявка на рассмотрение доктора'
        verbose_name_plural = 'Заявки на рассмотрение доктора'
