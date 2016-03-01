from django import forms


class FakeLoginForm(forms.Form):
    ERIGHTS = forms.CharField(label='ERIGHTS', max_length=400)
    sm_constitid = forms.CharField(label='sm_constitid', max_length=12)
    first_name = forms.CharField(label='first_name', max_length=200)
    last_name = forms.CharField(label='last_name', max_length=200)
