from django.shortcuts import render, redirect
from .forms import EventForm,Event
from django.contrib import messages

def event_ekle(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            messages.success(request,"Etkinlik başarıyla kaydedilmiştir.")
            return redirect("index")
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})



def etkinlik_listesi(request):
    etkinlikler = Event.objects.all()
    return render(request, 'liste.html', {'etkinlikler': etkinlikler})
