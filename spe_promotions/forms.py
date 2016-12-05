from django.forms import ModelForm, ModelMultipleChoiceField
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import SimpleEventPromotion, EventPromotionSelectionPlugin


class SimplePromotionsSelectionForm(ModelForm):
    promotions = ModelMultipleChoiceField(SimpleEventPromotion.objects.all().order_by('-start', '-end'),
                                      widget=FilteredSelectMultiple("briefs", False, ))

    class Meta:
        model = EventPromotionSelectionPlugin
        fields = ['template', 'promotions', ]