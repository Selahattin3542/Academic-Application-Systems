from django.shortcuts import render, redirect
from .forms import CategoryForm
from django.contrib import messages

def create_category(request):

    form = CategoryForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request,"Kategoriler başarıyla seçilmiştir.")
        return redirect('index')

    return render(request, 'kategori_puan.html', {'form': form})

