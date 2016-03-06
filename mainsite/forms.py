from django import forms
from cms.wizards.forms import BaseFormMixin
# from .models import PageTemplate, DEFAULT_PAGE_TYPE, PAGE_TYPES, DEFAULT_PAGE_TEMPLATE, PAGE_TEMPLATES
from spe_blog.models import Article


class FakeLoginForm(forms.Form):
    ERIGHTS = forms.CharField(label='ERIGHTS', max_length=400)
    sm_constitid = forms.CharField(label='sm_constitid', max_length=12)
    first_name = forms.CharField(label='first_name', max_length=200)
    last_name = forms.CharField(label='last_name', max_length=200)

# class PageCreationForm(BaseFormMixin, forms.ModelForm):

#     class Meta:
#         model = PageTemplate
#         exclude = []

class ArticleCreationForm(BaseFormMixin, forms.ModelForm):

     class Meta:
         model = Article
         exclude = ['auto_tags']

