# import re
# from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, ModelMultipleChoiceField
from django.contrib.admin.widgets import FilteredSelectMultiple
# from cms.models import Page
# from django.contrib.contenttypes.models import ContentType
from .models import Article, ArticlesPlugin, Editorial, EditorialPlugin


class ArticleSelectionForm(ModelForm):
    articles = ModelMultipleChoiceField(Article.objects.all().order_by('-date'),
                                        widget=FilteredSelectMultiple("articles", False, ))

    class Meta:
        model = ArticlesPlugin
        fields = ['template', 'order_by', 'articles', ]
#        fields = ['template', 'keep_original_order', 'order_by', 'articles', ]

class EditorialSelectionForm(ModelForm):
    editorial = ModelMultipleChoiceField(Editorial.objects.all(),
                                        widget=FilteredSelectMultiple("editorial", False, ))

    class Meta:
        model = EditorialPlugin
        fields = ['template', 'editorial', 'lnk' ]
