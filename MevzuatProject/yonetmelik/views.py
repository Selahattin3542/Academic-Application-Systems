import requests
from django.shortcuts import render,redirect
def yonetmelik_yonlendir(request):
    url ="https://www.ktun.edu.tr/Resimler/Mevzuat/Kriterler_22.11.2022.pdf"
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


