from django import forms

class ArticleForm(forms.Form):
    url = forms.URLField(label='Makale URL')
