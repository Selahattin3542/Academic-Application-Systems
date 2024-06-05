from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfesorForm,Profesor
from user.forms import LoginForm
from django.http import HttpResponseRedirect



def basvuru(request):
    if request.method == "GET":
        form = ProfesorForm
    elif request.method == "POST":
        form = ProfesorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Profesörlük için başvurunuz başarıyla alınmıştır")
            return redirect("index")
    context = {"form": form}
    return render(request, "prof_formu.html", context)

def basvuru_listesi(request):
    basvurular = Profesor.objects.all()
    return render(request, 'basvuru_liste.html', {'basvurular': basvurular})
