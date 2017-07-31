from django.contrib import admin


from .models import Topics
from .models import CustomerSubscription, CustomerClassification, Customer  # CustomerAchievement,
from .models import Tier1Discipline
from .models import Countries
from .models import Regions
from .models import Web_Region, Web_Region_Country
from .models import TimeZone


# class CustomerSubscriptionInline(admin.StackedInline):
#     model = Customer.subscriptions.through
#
#
# class CustomerClassificationInline(admin.TabularInline):
#     model = Customer.classifications.through
#
#
# class CustomerAchievementsInline(admin.TabularInline):
#     model = Customer.achievements.through
#
#

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ('id', 'last_name', 'first_name',)
    filter_horizontal = ('subscriptions', 'classifications',)


class CustomerClassificationAdmin(admin.ModelAdmin):
    search_fields = ('code', 'description')

admin.site.register(Customer, CustomerAdmin)
# admin.site.register(Customer)
admin.site.register(CustomerSubscription)
admin.site.register(CustomerClassification, CustomerClassificationAdmin)
# admin.site.register(CustomerAchievement)
admin.site.register(Tier1Discipline)
admin.site.register(TimeZone)
admin.site.register(Topics)
admin.site.register(Countries)
admin.site.register(Regions)
admin.site.register(Web_Region)
admin.site.register(Web_Region_Country)


# Reversion Control for User Accounts

from reversion.helpers import patch_admin
from cms.models import User
from cms.models import Group

patch_admin(User)
patch_admin(Group)
