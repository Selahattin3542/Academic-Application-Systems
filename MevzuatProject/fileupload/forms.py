from django import forms
from .models import Document
from django.utils import timezone
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['ad','soyad','basvurulanbolum','yayinadi','yayinturu','file','upload_date']
        widgets= {
            "ad": forms.TextInput(attrs={"class": "form-control"}),
            "soyad": forms.TextInput(attrs={"class": "form-control"}),
            "basvurulanbolum":forms.Select(attrs={"class":"form-control"}),
            "yayinadi": forms.Select(attrs={"class": "form-control"}),
            "yayinturu": forms.Select(attrs={"class": "form-control"}),
            "file":forms.ClearableFileInput(attrs={"class" : "form-control"}),
            "uploaddate":forms.DateTimeField(initial=timezone.now, widget=forms.HiddenInput()),



     }

