from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = (

         'ad', 'soyad', 'email', 'telefon','eser','eser_türü', 'makale', 'makale_türü', 'doktora_tezi','tez_türü','yds_belge'
        )
        widgets = {
            "ad":forms.TextInput(attrs={"class":"form-control"}),
            "soyad": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "telefon": forms.TextInput(attrs={"class": "form-control"}),
            "eser": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "makale": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "doktora_tezi": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "yds_belge":forms.ClearableFileInput(attrs={"class":"form-control"}),

        }