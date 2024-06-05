from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        # Use the fields attribute to include all the fields in the form
        fields = '__all__'