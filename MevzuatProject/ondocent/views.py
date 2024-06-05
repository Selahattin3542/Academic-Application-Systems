from django.shortcuts import render,redirect
from .models import Application
from .forms import ApplicationForm
from django.contrib import messages

def ondocent_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Doçentlik için ön başvurunuz başarıyla alınmıştır.")
            return redirect('index')
    else:
        form = ApplicationForm()

    context = {
        'form': form,
    }
    return render(request, 'ondocent_form.html', context)
