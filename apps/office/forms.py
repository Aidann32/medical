from django.forms import ModelForm, TextInput, DateTimeInput
from django.core.exceptions import ValidationError

from .models import Patient
from .tools import iin_to_datetime
from .widgets import DatePickerInput


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

        if not iin.isnumeric():
            raise ValidationError("ИИН должен содержать только цифры")   

        if not(iin_to_datetime(iin) == birth_date):

            raise ValidationError("ИИН и дата рождения должны совпадать")

        return cd