from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm

from .models import Profile
from apps.office.models import Patient


class CustomAuthenticationForm(AuthenticationForm):
	def __init__(self, request=None, *args, **kwargs):
		super().__init__(request=None, *args, **kwargs)
		self.fields['username'].label = 'Логин'
		self.fields['password'].label = 'Пароль'


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = Profile
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.confirmed = False
		user.role = 2
		if commit:
			user.save()
			Patient.objects.create(profile=user)
		return user
	