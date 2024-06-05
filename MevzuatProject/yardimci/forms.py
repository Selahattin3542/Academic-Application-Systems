from django import forms
from .models import Yardimci



class YardimciForm(forms.ModelForm):
    class Meta:
        model= Yardimci
        fields = ["ad", "soyad", "email", "telefon", "özgeçmiş","AYOK","tez","yds"]
        widgets= {
            "ad": forms.TextInput(attrs={"class": "form-control"}),
            "soyad": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "telefon": forms.TextInput(attrs={"class": "form-control"}),
            "özgeçmiş": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "AYOK":forms.ClearableFileInput(attrs={"class": "form-control"}),
            "tez":forms.ClearableFileInput(attrs={"class": "form-control"}),
            "yds": forms.ClearableFileInput(attrs={"class": "form-control"}),

        }

