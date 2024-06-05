from django import forms
from .models import Profesor



class ProfesorForm(forms.ModelForm):
    class Meta:
        model= Profesor
        fields = ["ad", "soyad", "email", "telefon","özgeçmiş","yds","onay","AYOK2","tez"]
        widgets= {
            "ad": forms.TextInput(attrs={"class": "form-control"}),
            "soyad": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "telefon": forms.TextInput(attrs={"class": "form-control"}),
            "özgeçmiş":forms.ClearableFileInput(attrs={"class" : "form-control"}),
            "yds": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "onay": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "AYOK2": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "form7": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "form5": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "form6": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "tez": forms.ClearableFileInput(attrs={"class": "form-control"}),






        }
