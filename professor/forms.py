from django import forms
from django.contrib.auth.models import User

from .models import Professor


class ProfessorForm(forms.ModelForm):
    ID = forms.IntegerField()
    first_name       = forms.CharField(label='',
                    widget=forms.TextInput(attrs={"placeholder": "First Name"}))
    last_name = forms.CharField(label='',
                                 widget=forms.TextInput(attrs={"placeholder": "Last Name"}))
    area_of_interest = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Your description",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 20,
                                    'cols': 120
                                }
                            )
                        )
    class Meta:
        model = Professor
        fields = [
            'ID',
            'area_of_interest',
            'first_name',
            'last_name',
        ]

class proffform(forms.ModelForm):
    queryset = Professor.objects.all()
    proff1 = forms.ModelChoiceField(queryset=Professor.objects.all())
    proff2 = forms.ModelChoiceField(queryset=Professor.objects.all())
    class Meta:
        model = Professor
        fields = [
            'proff1',
            'proff2'
        ]