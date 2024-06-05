from django import forms
from .models import Yardimci
from django.utils import timezone


class DocentForm(forms.ModelForm):
    class Meta:
        model = Yardimci
        fields = ['ad','soyad','email','telefon','onay','ozgecmis','AYOK','tez','yds','upload_date']
        widgets = {
            "ad": forms.TextInput(attrs={"class": "form-control"}),
            "soyad": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "telefon": forms.TextInput(attrs={"class": "form-control"}),
            "onay": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "ozgecmis": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "AYOK": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "tez": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "yds": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "uploaddate": forms.DateTimeField(initial=timezone.now, widget=forms.HiddenInput()),

        }