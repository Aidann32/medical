from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class CustomAuthenticationForm(AuthenticationForm):
	def __init__(self, request=None, *args, **kwargs):
		super().__init__(request=None, *args, **kwargs)
		self.fields['username'].label = 'Логин'
		self.fields['password'].label = 'Пароль'
	