from .models import SimpleEventPromotion
from mainsite.models import Regions, Tier1Discipline, Web_Region
from spe_events.models import EventType

import django_filters
from django_filters.widgets import RangeWidget
from django import forms


class SimplePromotionFilter(django_filters.FilterSet):
    start = django_filters.DateFilter(
        widget=forms.TextInput(attrs={'class': 'datepicker', 'placeholder': 'YYYY-MM-DD'}), lookup_expr='lte',
        label='Start of test date range (blank for no filtering)', )
    end = django_filters.DateFilter(widget=forms.TextInput(attrs={'class': 'datepicker', 'placeholder': 'YYYY-MM-DD'}),
                                    lookup_expr='gte', label='End of test date range (blank for no filtering)', )
    event_type = django_filters.ModelMultipleChoiceFilter(queryset=EventType.objects.filter(active=True),
                                                          widget=forms.CheckboxSelectMultiple, lookup_expr='in',
                                                          label='Event type (all blank for no filtering)', )
    disciplines = django_filters.ModelMultipleChoiceFilter(queryset=Tier1Discipline.objects.filter(active=True),
                                                           widget=forms.CheckboxSelectMultiple, lookup_expr='in',
                                                           label='Disciplines (all blank for no filtering)', )
    regions = django_filters.ModelMultipleChoiceFilter(queryset=Web_Region.objects.filter(is_visible=True),
                                                       widget=forms.CheckboxSelectMultiple, lookup_expr='in',
                                                       label='Regions (all blank for no filtering)', )

    class Meta:
        model = SimpleEventPromotion
        fields = [
            'start',
            'end',
            'event_type',
            'disciplines',
            'regions',
        ]


class SimpleMembershipFilter(django_filters.FilterSet):
    start = django_filters.DateFilter(
        widget=forms.TextInput(attrs={'class': 'datepicker', 'placeholder': 'YYYY-MM-DD'}), lookup_expr='lte',
        label='Start of test date range (blank for no filtering)', )
    end = django_filters.DateFilter(widget=forms.TextInput(attrs={'class': 'datepicker', 'placeholder': 'YYYY-MM-DD'}),
                                    lookup_expr='gte', label='End of test date range (blank for no filtering)', )
    regions = django_filters.ModelMultipleChoiceFilter(queryset=Web_Region.objects.filter(is_visible=True),
                                                       widget=forms.CheckboxSelectMultiple, lookup_expr='in',
                                                       label='Regions (all blank for no filtering)', )

    class Meta:
        model = SimpleEventPromotion
        fields = [
            'start',
            'end',
            'regions',
        ]
