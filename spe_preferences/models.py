from django.db import models
from django.utils import timezone
# from mainsite.models import Customer


# class AdditionalPreference(models.Model):
#     customer_id = models.CharField(max_length=12, blank=True, null=True)
# #    customer_id = models.ForeignKey(Customer, related_name="customers", on_delete=models.SET_NULL, blank=True, null=True)
#     pref_one = models.CharField(max_length=1, blank=True, null=True)  # fav lowercase letter?
#     pref_two = models.CharField(max_length=1, blank=True, null=True)  # fav uppercase letter?
# #    author_email = models.CharField(max_length=90, blank=True, null=True)
# #    customer_id = models.CharField(max_length=12, blank=True, null=True)
# #    customer_email = models.CharField(max_length=90, blank=True, null=True)
# #    customer_first_name = models.CharField(max_length=80, blank=True, null=True)
# #    customer_last_name = models.CharField(max_length=60, blank=True, null=True)
# #    customer_country_code = models.CharField(max_length=2, blank=True, null=True)
#     submitted_date = models.DateTimeField(default=timezone.now)
# #    class Meta:
# #        verbose_name = "Country"
# #        verbose_name_plural = "Countries"

# class PrefsSubmission(models.Model):
#     id = models.IntegerField(primary_key=True)
#     when_submitted = models.DateTimeField(auto_now=True)
#     purpose_comment = models.TextField(max_length=180, blank=True)
#     member_id = models.SlugField(max_length=12)
# # $ cat pref_one pref_two | awk - F "\t" '{print "    pref_>",$1,"<_is_selected = models.IntegerField(blank=True,default=None,verbose_name=\">",$2,"<\")"}' | sed - r 's,(> | <),,g' | sed - r 's __ _group_ g'
#     pref_r_group_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Resources")
#     pref_r_1_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Carbonates")
#     pref_r_2_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Gas condensates")
#     pref_r_3_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Geothermal")
#     pref_r_4_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Heavy oil/tar sands")
#     pref_r_5_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Shale oil")
#     pref_r_6_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Tight gas/shale gas/coalbed methane")
#     pref_oe_group_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Operating environments")
#     pref_oe_1_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Arctic/extreme environments")
#     pref_oe_2_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Greenfields")
#     pref_oe_3_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Marginal/aging fields")
#     pref_oe_4_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Offshore")
#     pref_oe_5_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Onshore")
#     pref_wd_group_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Drilling ")
#     pref_wd_1_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Casing/cementing/zonal isolation")
#     pref_wd_2_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Drilling automation")
#     pref_wd_3_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Drilling fluids")
#     pref_wd_4_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Drilling operations")
#     pref_wd_5_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Formation damage")
#     pref_wd_6_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Directional/extended reach wells")
#     pref_wd_7_is_selected = models.IntegerField(blank=True, default=None, verbose_name="HP/HT")
#     pref_wd_8_is_selected = models.IntegerField(blank=True, default=None, verbose_name="MPD/UBD")
#     pref_wd_9_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Water treatment and management")
#     pref_wd_10_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Well integrity/control")
#     pref_wc_group_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Completions")
#     pref_wc_1_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Stimulation/acidizing")
#     pref_wc_2_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Completion fluids")
#     pref_wc_3_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Formation damage")
#     pref_wc_4_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Hydraulic fracturing")
#     pref_wc_5_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Intelligent fields/surveillance")
#     pref_wc_6_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Sand management/control")
#     pref_wc_7_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Water treatment and management")
#     pref_wc_8_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Well integrity/control")
#     pref_wc_9_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Well intervention/recompletion")
#     pref_rdd_group_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Reservoir description and dynamics")
#     pref_rdd_1_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Carbon capture and storage")
#     pref_rdd_2_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Enhanced recovery")
#     pref_rdd_3_is_selected = models.IntegerField(blank=True, default=None, verbose_name="HP/HT")
#     pref_rdd_4_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Intelligent fields/surveillance")
#     pref_rdd_5_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Petroleum reserves")
#     pref_rdd_6_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Petrophysics/geophysics")
#     pref_rdd_7_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Reservoir characterization")
#     pref_rdd_8_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Reservoir management")
#     pref_rdd_9_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Reservoir simulation")
#     pref_po_group_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Production and well operations")
#     pref_po_1_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Artificial lift")
#     pref_po_2_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Carbon capture and storage")
#     pref_po_3_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Coiled tubing")
#     pref_po_4_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Continued service of fields")
#     pref_po_5_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Decommisioning/site remediation")
#     pref_po_6_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Enhanced recovery")
#     pref_po_7_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Field start-up/commissioning")
#     pref_po_8_is_selected = models.IntegerField(blank=True, default=None, verbose_name="H2S/sour gas")
#     pref_po_9_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Intelligent fields/surveillance")
#     pref_po_10_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Production chemistry")
#     pref_po_11_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Sand management/control")
#     pref_po_12_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Separation/metering")
#     pref_po_13_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Stimulation/acidizing")
#     pref_po_14_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Water treatment and management")
#     pref_po_15_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Well intervention/recompletion")
#     pref_pfc_group_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Projects, facilities & construction")
#     pref_pfc_1_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Carbon capture and storage")
#     pref_pfc_2_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Continued service of fields")
#     pref_pfc_3_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Corrosion")
#     pref_pfc_4_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Decommisioning/site remediation")
#     pref_pfc_5_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Facilities planning and maintenance")
#     pref_pfc_6_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Field start-up/commissioning")
#     pref_pfc_7_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Flow assurance")
#     pref_pfc_8_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Gas conversion (LNG/GTL)")
#     pref_pfc_9_is_selected = models.IntegerField(blank=True, default=None, verbose_name="HP/HT")
#     pref_pfc_10_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Processing systems/design")
#     pref_pfc_11_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Project management")
#     pref_pfc_12_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Risers/flowlines/pipelines")
#     pref_pfc_13_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Separation/metering")
#     pref_pfc_14_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Subsea systems")
#     pref_pfc_15_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Topsides/floating production systems")
#     pref_pfc_16_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Water treatment and management")
#     pref_hse_group_is_selected = models.IntegerField(blank=True, default=None, verbose_name="HSSE-SR")
#     pref_hse_1_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Carbon capture and storage")
#     pref_hse_2_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Decommisioning/site remediation")
#     pref_hse_3_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Environment")
#     pref_hse_4_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Safety/health")
#     pref_hse_5_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Social responsibility/sustainability")
#     pref_hse_6_is_selected = models.IntegerField(blank=True, default=None,  verbose_name="Water treatment and management")
#     pref_mi_group_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Management and Information")
#     pref_mi_1_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Asset/portfolio management")
#     pref_mi_2_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Petroleum economics/production forecasting")
#     pref_mi_3_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Risk management/decision-making")
#     pref_mi_4_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Data and information management")
#     pref_mi_5_is_selected = models.IntegerField(blank=True, default=None, verbose_name="R&D")
#     pref_mi_6_is_selected = models.IntegerField(blank=True, default=None, verbose_name="Faculty/engineering education")
#     pref_mi_7_is_selected = models.IntegerField(blank=True, default=None, verbose_name="HR/people management")
#
#     def __str__(self):
#         return "ci=" + self.customer_id + " p1=" + self.pref_one + " p2=" + self.pref_two


class PreferenceGroup(models.Model):
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    status = models.CharField(max_length=12, blank=True, default='ACTIVE')
    sort_order = models.IntegerField(default=0)


class Preference(models.Model):
    group = models.ForeignKey(PreferenceGroup, on_delete=models.PROTECT)
    name = models.CharField(max_length=120, blank=True, null=True)
    status = models.CharField(max_length=12, blank=True, default='ACTIVE')
    sort_order = models.IntegerField(default=0)
    submitted_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.name


class CustomerPreference(models.Model):
    meeting_id = models.CharField(max_length=25)
    customer_id = models.CharField(max_length=12)
    preference = models.ForeignKey(Preference, on_delete=models.PROTECT)

    def __str__(self):
        return "[" + self.meeting_id + "] " + self.customer_id + " - " + self.preference.name
