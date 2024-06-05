import requests
from django.shortcuts import render,redirect
from .models import Prof
from .forms import ProfesorForm
from django.contrib import messages


def dfile(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST, request.FILES)
        if form.is_valid():
            form = Prof(
                ad=form.cleaned_data['ad'],
                soyad=form.cleaned_data['soyad'],
                email=form.cleaned_data['email'],
                telefon=form.cleaned_data['telefon'],
                onay=request.FILES['onay'],
                ozgecmis=request.FILES['ozgecmis'],
                AYOK2=request.FILES['AYOK2'],
                form5=request.FILES['form5'],
                form6=request.FILES['form6'],
                tez=request.FILES['tez'],
                form7=request.FILES['form7'],
                yds=request.FILES['yds']
            )
            form.save()
            messages.success(request,"Profesörlük için başvurunuz alınmıştır.")
            return redirect('index')
    else:
        form = ProfesorForm()

    context = {
        'form': form,
    }
    return render(request, 'pfile.html', context)
def dupload(request):
    basvurular = Prof.objects.all()
    return render(request, 'pupload.html', {'basvurular': basvurular})

