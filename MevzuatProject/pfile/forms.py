from django import forms
from .models import Prof
from django.utils import timezone



class ProfesorForm(forms.ModelForm):
    class Meta:
        model= Prof
        fields = ["ad", "soyad", "email", "telefon","ozgecmis","yds","onay","AYOK2","form5","form6","form7","tez","upload_date"]
        widgets= {
            "ad": forms.TextInput(attrs={"class": "form-control"}),
            "soyad": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "telefon": forms.TextInput(attrs={"class": "form-control"}),
            "ozgecmis":forms.ClearableFileInput(attrs={"class" : "form-control"}),
            "yds": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "onay": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "AYOK2": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "form5": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "form6": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "form7": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "tez": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "uploaddate": forms.DateTimeField(initial=timezone.now, widget=forms.HiddenInput()),

        }
