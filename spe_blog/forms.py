# from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, ModelMultipleChoiceField
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import Article, ArticlesPlugin, ArticlesListingPlugin, Editorial, EditorialPlugin, Brief, BriefPlugin, \
    Topics, TopicsPlugin, TopicsListPlugin, Category


class ArticlesListingForm(ModelForm):
    categories = ModelMultipleChoiceField(Category.objects.all().order_by('name'),
                                          widget=FilteredSelectMultiple("categories", False, ), required=False)

    class Meta:
        model = ArticlesListingPlugin
        fields = ['template', 'cnt', 'order_by', 'starting_with', 'publication', 'print_volume', 'print_issue',
                  'personalized', 'discipline', 'categories', 'all_url', 'all_text', ]


class ArticleSelectionForm(ModelForm):
    articles = ModelMultipleChoiceField(Article.objects.all().order_by('-date'),
                                        widget=FilteredSelectMultiple("articles", False, ))

    class Meta:
        model = ArticlesPlugin
        fields = ['template', 'order_by', 'articles', ]


# fields = ['template', 'keep_original_order', 'order_by', 'articles', ]

class EditorialSelectionForm(ModelForm):
    editorial = ModelMultipleChoiceField(Editorial.objects.all(),
                                         widget=FilteredSelectMultiple("editorial", False, ))

    class Meta:
        model = EditorialPlugin
        fields = ['template', 'editorial', 'lnk']


class BriefSelectionForm(ModelForm):
    briefs = ModelMultipleChoiceField(Brief.objects.all().order_by('-date'),
                                      widget=FilteredSelectMultiple("briefs", False, ))

    class Meta:
        model = BriefPlugin
        fields = ['template', 'order_by', 'briefs', ]


class TopicsSelectionForm(ModelForm):
    topics = ModelMultipleChoiceField(Topics.objects.all(),
                                      widget=FilteredSelectMultiple("briefs", False, ))

    class Meta:
        model = TopicsPlugin
        fields = ['allow_url_to_override_selection', 'publication', 'template', 'cnt', 'order_by', 'starting_with',
                  'topics', ]


class TopicsListSelectionForm(ModelForm):
    topics = ModelMultipleChoiceField(Topics.objects.all(),
                                      widget=FilteredSelectMultiple("briefs", False, ))

    class Meta:
        model = TopicsListPlugin
        fields = ['publication', 'topics', ]
