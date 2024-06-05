from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import YardimciForm
from user.forms import LoginForm
from django.http import HttpResponseRedirect



def basvuru(request):
    if request.method == "GET":
        form = YardimciForm
    elif request.method == "POST":
        form = YardimciForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Doktor Öğretim Üyeliği için başvurunuz başarıyla alınmıştır")
            return redirect("index")
    context = {"form": form}
    return render(request, "yard_formu.html", context)

def login_view(request):
    if request.method == "POST":
        form =LoginForm(request.POST)
        if form.is_valid():
            kullanici_adi = form.cleaned_data.get("kullanici_adi")
            sifre = form.cleaned_data.get("sifre")


        else:
            form = YardimciForm()
            return render(request,"yard_formu.html",{"form":form})