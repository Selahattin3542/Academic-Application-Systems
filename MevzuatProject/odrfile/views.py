import requests
from django.shortcuts import render,redirect
from .models import  Application
from .forms import ApplicationForm
from django.contrib import messages


def dfile(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form = Application(
                ad=form.cleaned_data['ad'],
                soyad=form.cleaned_data['soyad'],
                email=form.cleaned_data['email'],
                telefon=form.cleaned_data['telefon'],
                eser=request.FILES['eser'],
                eser_türü=form.cleaned_data['eser_türü'],
                makale=request.FILES['makale'],
                makale_türü=form.cleaned_data['makale_türü'],
                doktora_tezi=request.FILES['doktora_tezi'],
                tez_türü=form.cleaned_data['tez_türü'],
                yds_belge=request.FILES['yds_belge'],
            )
            form.save()
            messages.success(request,"Doktor Öğretim Üyeliği için ön başvurunuz alınmıştır.")
            return redirect('index')
    else:
        form = ApplicationForm()

    context = {
        'form': form,
    }
    return render(request, 'odrfile.html', context)
def dupload(request):
    basvurular = Application.objects.all()
    return render(request, 'odrupload.html', {'basvurular': basvurular})

