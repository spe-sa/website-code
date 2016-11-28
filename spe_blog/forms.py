# from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, ModelMultipleChoiceField
# from django.forms.models import ModelFormOptions
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import Article, ArticlesPlugin, Editorial, EditorialPlugin, Brief, BriefPlugin, \
    Topics, TopicsPlugin, TopicsListPlugin, BriefListingPlugin, Web_Region, Category, SecondaryCategory, \
    ArticlesListingPlugin


class ArticleSelectionForm(ModelForm):
    articles = ModelMultipleChoiceField(Article.objects.all().order_by('-date'),
                                        widget=FilteredSelectMultiple("articles", False, ))

    class Meta:
        model = ArticlesPlugin
        exclude = []
        fields = ['template', 'order_by', 'articles', 'all_url', 'all_text', 'backcol', 'fixedheight', 'whitetext',
                  'boxwidth', 'boxheight', ]


class ArticlesListSelectionForm(ModelForm):
    categories = ModelMultipleChoiceField(Category.objects.all(),
                                          widget=FilteredSelectMultiple("categories", False, ), required=False)

    secondary_categories = ModelMultipleChoiceField(SecondaryCategory.objects.all(),
                                                    widget=FilteredSelectMultiple("secondary_categories", False, ),
                                                    required=False)

    class Meta:
        model = ArticlesListingPlugin
        exclude = []
        fields = ['template', 'cnt', 'order_by', 'starting_with', 'publication', 'print_volume', 'print_issue',
                  'categories', 'secondary_categories', 'all_url', 'all_text', 'backcol',
                  'whitetext', 'boxtitle', 'personalized', 'discipline', 'fixedheight', 'boxwidth', 'boxheight']


class EditorialSelectionForm(ModelForm):
    editorial = ModelMultipleChoiceField(Editorial.objects.all(),
                                         widget=FilteredSelectMultiple("editorial", False, ))

    class Meta:
        model = EditorialPlugin
        fields = ['template', 'backcol', 'editorial', 'lnk']


class BriefSelectionForm(ModelForm):
    briefs = ModelMultipleChoiceField(Brief.objects.all().order_by('-date'),
                                      widget=FilteredSelectMultiple("briefs", False, ))

    class Meta:
        model = BriefPlugin
        fields = ['template', 'order_by', 'briefs', 'backcol', 'whitetext', ]


class TopicsSelectionForm(ModelForm):
    topics = ModelMultipleChoiceField(Topics.objects.all(),
                                      widget=FilteredSelectMultiple("topics", False, ))

    class Meta:
        model = TopicsPlugin
        fields = ['allow_url_to_override_selection', 'publication', 'template', 'cnt', 'order_by', 'starting_with',
                  'topics', ]


class TopicsListSelectionForm(ModelForm):
    topics = ModelMultipleChoiceField(Topics.objects.all(),
                                      widget=FilteredSelectMultiple("topics", False, ))

    class Meta:
        model = TopicsListPlugin
        fields = ['template', 'publication', 'topics', ]


class BriefsListSelectionForm(ModelForm):
    regions = ModelMultipleChoiceField(Web_Region.objects.filter(is_visible__gte=1),
                                       widget=FilteredSelectMultiple("regions", False, ), required=False)

    categories = ModelMultipleChoiceField(Category.objects.all(),
                                          widget=FilteredSelectMultiple("categories", False, ), required=False)

    secondary_categories = ModelMultipleChoiceField(SecondaryCategory.objects.all(),
                                                    widget=FilteredSelectMultiple("secondary_categories", False, ),
                                                    required=False)

    class Meta:
        model = BriefListingPlugin
        exclude = []
