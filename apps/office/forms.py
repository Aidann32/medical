from django.forms import ModelForm, TextInput
from django.core.exceptions import ValidationError

from .models import Patient

class PatientModelForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'iin', 'email', 'phone_number')

        widgets = {
            'phone_number': TextInput(attrs={'id': 'phone-mask'}),
        }

    def clean(self):
        cd = self.cleaned_data

        iin = cd.get('iin')
        if not iin.isnumeric():
            raise ValidationError("ИИН должен содержать только цифры")           
        
        return cd