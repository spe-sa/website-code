from django.contrib import admin
from .models import PreferenceGroup, Preference, CustomerPreference, ContactPreference


admin.site.register(PreferenceGroup)
admin.site.register(Preference)
admin.site.register(CustomerPreference)

admin.site.register(ContactPreference)
