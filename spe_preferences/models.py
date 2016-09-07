from django.db import models
from django.utils import timezone
# from mainsite.models import Customer


class AdditionalPreference(models.Model):
    customer_id = models.CharField(max_length=12, blank=True, null=True)
#    customer_id = models.ForeignKey(Customer, related_name="customers", on_delete=models.SET_NULL, blank=True, null=True)
    pref_one = models.CharField(max_length=1, blank=True, null=True)  # fav lowercase letter?
    pref_two = models.CharField(max_length=1, blank=True, null=True)  # fav uppercase letter?

#    author_email = models.CharField(max_length=90, blank=True, null=True)
#    customer_id = models.CharField(max_length=12, blank=True, null=True)
#    customer_email = models.CharField(max_length=90, blank=True, null=True)
#    customer_first_name = models.CharField(max_length=80, blank=True, null=True)
#    customer_last_name = models.CharField(max_length=60, blank=True, null=True)
#    customer_country_code = models.CharField(max_length=2, blank=True, null=True)
    submitted_date = models.DateTimeField(default=timezone.now)

#    class Meta:
#        verbose_name = "Country"
#        verbose_name_plural = "Countries"

    def __str__(self):
        return "ci=" + self.customer_id + " p1=" + self.pref_one + " p2=" + self.pref_two