import requests
from django.shortcuts import render,redirect
from .models import Yardimci
from .forms import DocentForm
from django.contrib import messages


def dfile(request):
    if request.method == 'POST':
        form = DocentForm(request.POST, request.FILES)
        if form.is_valid():
            form = Yardimci(
                ad=form.cleaned_data['ad'],
                soyad=form.cleaned_data['soyad'],
                email=form.cleaned_data['email'],
                telefon=form.cleaned_data['telefon'],
                onay=request.FILES['onay'],
                ozgecmis=request.FILES['ozgecmis'],
                AYOK=request.FILES['AYOK'],
                tez=request.FILES['tez'],
                yds=request.FILES['yds']
            )
            form.save()
            messages.success(request,"Doçentlik için başvurunuz alınmıştır.")
            return redirect('index')
    else:
        form = DocentForm()

    context = {
        'form': form,
    }
    return render(request, 'drfile.html', context)
def dupload(request):
    basvurular = Yardimci.objects.all()
    return render(request, 'drupload.html', {'basvurular': basvurular})

