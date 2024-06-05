import requests
from django.shortcuts import render,redirect
from .models import Docent
from .forms import DocentForm
from django.contrib import messages


def dfile(request):
    if request.method == 'POST':
        form = DocentForm(request.POST, request.FILES)
        if form.is_valid():
            form = Docent(
                ad=form.cleaned_data['ad'],
                soyad=form.cleaned_data['soyad'],
                email=form.cleaned_data['email'],
                telefon=form.cleaned_data['telefon'],
                onay=request.FILES['onay'],
                ozgecmis=request.FILES['ozgecmis'],
                AYOK=request.FILES['AYOK'],
                form3=request.FILES['form3'],
                form4=request.FILES['form4'],
                tez=request.FILES['tez'],
                form7=request.FILES['form7'],
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
    return render(request, 'dfile.html', context)
def dupload(request):
    basvurular = Docent.objects.all()
    return render(request, 'dupload.html', {'basvurular': basvurular})

