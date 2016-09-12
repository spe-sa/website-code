from django import forms
from .models import AdditionalPreference


#class FindUserForm(forms.fields_for_model('constituent_id', 'email_address', 'first_name', 'last_name', 'country_code'))
class FindUserForm(forms.Form):
    constituent_id = forms.CharField(max_length=12)
    email = forms.CharField(max_length=90)
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=60)
    country_code = forms.CharField(max_length=3)
#    class Meta:
#        model = AdditionalPreference
#        fields = ('constituent_id', 'email_address', 'first_name', 'last_name', 'country_code')

class PrefsForm(forms.ModelForm):
    class Meta:
        model = AdditionalPreference
        exclude = ()
#        fields = ('customer_id','pref_one')

class PrefsUserSearchForm(forms.Form):
    customer_id = forms.CharField(max_length=12, required=False)
    email = forms.CharField(max_length=90, required=False)
    first_name = forms.CharField(max_length=80, required=False)
    last_name = forms.CharField(max_length=60, required=False)
