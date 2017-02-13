from django import forms


class HomeForm(forms.Form):
    post = forms.CharField()
