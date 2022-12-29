from django import forms


class GenerateForm(forms.Form):
    seria = forms.CharField()
    col = forms.CharField()

class InfoForm(forms.Form):
    seria = forms.CharField()
    nomer = forms.CharField()