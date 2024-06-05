from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm
from django.contrib import messages

def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = Document(
                ad=form.cleaned_data['ad'],
                soyad=form.cleaned_data['soyad'],
                basvurulanbolum=form.cleaned_data['basvurulanbolum'],
                yayinadi=form.cleaned_data['yayinadi'],
                yayinturu=form.cleaned_data['yayinturu'],
                file=request.FILES['file']
            )
            document.save()
            messages.success(request,"Dosyalar başarıyla yüklenmiştir")
            return redirect("index")
    else:
        form = DocumentForm()
    return render(request, 'file_upload.html', {'form': form})

def dosya_listesi(request):
    files = Document.objects.all()
    return render(request,"upload.html",{'files': files})
