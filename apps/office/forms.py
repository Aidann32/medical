from django.forms import ModelForm, TextInput, DateTimeInput, HiddenInput, ModelChoiceField
from django.core.exceptions import ValidationError

from .models import Patient, XRay, XRayRequest
from .tools import iin_to_datetime
from .widgets import DatePickerInput

from apps.profiles.models import Profile


class PatientModelForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'iin', 'birth_date', 'gender', 'email', 'phone_number')

        widgets = {
            'phone_number': TextInput(attrs={'id': 'phone-mask'}),
            'birth_date': DatePickerInput(),
        }

    def clean(self):
        cd = self.cleaned_data

        iin = cd.get('iin')
        birth_date = cd.get('birth_date')
        phone_number = cd.get('phone_number')

        # if Patient.objects.filter(iin=iin).exists():
        #     raise ValidationError("Пациент с таким ИИН уже существует")

        # if Patient.objects.filter(phone_number=phone_number).exists():
        #     raise ValidationError('Пациент с таким номером телефона уже существует')

        if not iin.isnumeric():
            raise ValidationError("ИИН должен содержать только цифры")   

        if not(iin_to_datetime(iin) == birth_date):
            raise ValidationError("ИИН и дата рождения должны совпадать")

        return cd


class XRayModelForm(ModelForm):
    class Meta:
        model = XRay
        fields = ('photo',)


class XRayRequestForm(ModelForm):
    class Meta:
        model = XRayRequest
        fields = ('doctor', )

    def __init__(self, *args, **kwargs):
        super(XRayRequestForm, self).__init__(*args, **kwargs)
        self.fields['doctor'] = ModelChoiceField(queryset=Profile.objects.filter(role=1), label='Доктор')


class XRayRequestDetailsForm(ModelForm):
    class Meta:
        model = XRayRequest
        fields = ('diagnosis', 'doctor_comment')

