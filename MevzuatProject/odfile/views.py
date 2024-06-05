import requests
from django.shortcuts import render,redirect
from .models import  Doctor
from .forms import DoctorForm
from django.contrib import messages


def dfile(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form = Doctor(
                ad=form.cleaned_data['ad'],
                soyad=form.cleaned_data['soyad'],
                email=form.cleaned_data['email'],
                telefon=form.cleaned_data['telefon'],
                eser1=request.FILES['eser1'],
                eser_türü1=form.cleaned_data['eser_türü1'],
                eser2=request.FILES['eser2'],
                eser_türü2=form.cleaned_data['eser_türü2'],
                makale=request.FILES['makale'],
                makale_türü=form.cleaned_data['makale_türü'],
                doktora_tezi=request.FILES['doktora_tezi'],
                tez_türü=form.cleaned_data['tez_türü'],
                yds_belge=request.FILES['yds_belge'],
                sözlü=request.FILES['sözlü']
            )
            form.save()
            messages.success(request,"Doçentlik için ön başvurunuz alınmıştır.")
            return redirect('index')
    else:
        form = DoctorForm()

    context = {
        'form': form,
    }
    return render(request, 'odfile.html', context)
def dupload(request):
    basvurular = Doctor.objects.all()
    return render(request, 'odupload.html', {'basvurular': basvurular})

