import requests
from django.shortcuts import render,redirect
def indir_belge_form(request):
    url ="https://www.ktun.edu.tr/tr/Birim/Index/?brm=+cVZiaNYjK0cPMQi6AEyXw=="
    return redirect(url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open("indirilen_belge.pdf", "wb") as f:
                f.write(response.content)
            print("Belge başarıyla indirildi.")
        else:
            print("Belge indirme hatası:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Bağlantı hatası:", e)

        return render(request, "", {"url": url})


