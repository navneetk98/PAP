from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    cpi = forms.IntegerField(help_text='Your nightmare')
    tier = forms.IntegerField(help_text='Your class xD')
    group_id = forms.IntegerField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'cpi', 'tier', 'group_id', 'password1', 'password2', )
