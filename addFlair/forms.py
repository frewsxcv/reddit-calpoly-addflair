import calpoly

from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=20)
    year = forms.ChoiceField(choices=calpoly.years())
    major = forms.ChoiceField(choices=calpoly.majors())
