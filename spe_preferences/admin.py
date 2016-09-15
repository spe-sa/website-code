from django.contrib import admin
from .models import PreferenceGroup, Preference, CustomerPreference


admin.site.register(PreferenceGroup)
admin.site.register(Preference)
admin.site.register(CustomerPreference)
