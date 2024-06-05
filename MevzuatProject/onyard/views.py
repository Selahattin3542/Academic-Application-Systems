from django.shortcuts import render,redirect
from .models import Application
from  django.contrib import messages
from .forms import ApplicationForm


def onyard_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Doktor Öğretim Üyeliği için ön başvurunuz başarıyla alınmıştır.")
            return redirect('index')
    else:
        form = ApplicationForm()

    context = {
        'form': form,
    }
    return render(request, 'yard_formu.html', context)


