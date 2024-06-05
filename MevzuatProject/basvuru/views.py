
from django.shortcuts import render
from .forms import ApplicationForm


def basvuru(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            # Başvuru başarıyla kaydedildi, istediğiniz işlemi yapabilirsiniz
            # Örneğin, başvurunun uygunluğunu kontrol etmek için application.is_eligible() kullanılabilir
    else:
        form = ApplicationForm()

    return render(request, 'basvuru_formu.html', {'form': form})
