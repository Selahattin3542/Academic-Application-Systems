from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['ad', 'bastarih', 'bittar','düzenleyen', 'aciklama']

        widgets={
            "ad": forms.Select(attrs={"class": "form-control"}),
            "bastarih": forms.DateInput(attrs={"type": "date"}),
            "bittar":  forms.DateInput(attrs={"type": "date"}),
            "düzenleyen": forms.TextInput(attrs={"class":"form-control"}),
            "aciklama":  forms.TextInput(attrs={"class": "form-control"})


        }
