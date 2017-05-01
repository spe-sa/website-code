from django.forms import ModelForm, ModelMultipleChoiceField
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import SimpleEventPromotion, EventPromotionSelectionPlugin, SimpleMembershipPromotion, \
    MembershipPromotionSelectionPlugin


class SimplePromotionsSelectionForm(ModelForm):
    promotions = ModelMultipleChoiceField(SimpleEventPromotion.objects.all().order_by('-start', '-end'),
                                          widget=FilteredSelectMultiple("promotions", False, ))

    class Meta:
        model = EventPromotionSelectionPlugin
        fields = ['template', 'promotions', 'more_text', 'more_url', ]


class SimpleMembershipPromotionSelectionForm(ModelForm):
    promotions = ModelMultipleChoiceField(SimpleMembershipPromotion.objects.all().order_by('-start', '-end'),
                                          widget=FilteredSelectMultiple("promotions", False, ))

    class Meta:
        model = MembershipPromotionSelectionPlugin
        fields = ['template', 'promotions', 'more_text', 'more_url', ]
