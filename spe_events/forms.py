from django import forms
from .models import ImageItems


class ImageItemInLineForm(forms.ModelForm):

    imageurl = forms.CharField(widget=forms.TextInput(attrs={'data-validate-url': 'true'}), required=False)

    class Meta:
        model = ImageItems
        exclude = []

    class Media:
        js=(
            'js/validate_urls.js',
        )
