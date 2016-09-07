from django import forms
from .models import AdditionalPreference

class PrefsForm(forms.ModelForm):
    class Meta:
        model = AdditionalPreference
        exclude = ()
#        fields = ('customer_id','pref_one')
