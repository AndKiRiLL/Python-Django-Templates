from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def about(request):
    data = {"full_name": "Андриянов Кирилл Евгеньевич", "height": 185, "weight": 60, "age": 17}
    return render(request, "about.html", context = data)

def contacts(request):
    cont = {
        "Номер телефона": "+7 905 396 10 44",
        "VK": "https://vk.com/l0l_kirill_l0l",
        "Telegram": "+7 905 396 10 44",
    }
    return render(request, "contacts.html", context = {"cont": cont})

def form(request):
    return render(request, "form.html")

