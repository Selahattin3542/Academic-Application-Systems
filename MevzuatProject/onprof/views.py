from django.shortcuts import render,redirect
from .models import Application
from .forms import ApplicationForm
from django.contrib import messages

def prof_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Profesörlük için ön başvurunuz başarıyla alınmıştır.")
            return redirect('index')
    else:
        form = ApplicationForm()

    context = {
        'form': form,
    }
    return render(request, 'onprof_form.html', context)
