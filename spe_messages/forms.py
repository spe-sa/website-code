from django.forms import ModelForm, ModelMultipleChoiceField
from django.contrib.admin.widgets import FilteredSelectMultiple

from mainsite.models import CustomerClassification
from .models import TargetedMessageForMemberPlugin


class TargetedMessageForMemberForm(ModelForm):
    messages = ModelMultipleChoiceField(CustomerClassification.objects.all().order_by('code'),
                                          widget=FilteredSelectMultiple("classifications", False, ))

    class Meta:
        model = TargetedMessageForMemberPlugin
        fields = ['template', 'count', 'classifications', ]
