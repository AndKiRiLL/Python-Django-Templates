from django.shortcuts import render
from django.template.response import TemplateResponse

def index(request):
    # langs = ["Python", "JavaScript", "Java", "C#", "C++"]
    #return render(request, "index.html", context={"langs": langs})
    data = {"red": "красный", "green": "зеленый", "blue": "синий"}
    return render(request, "index.html", context={"data": data})

    # data = {"n" : 5}
    # return render(request, "index.html", context=data)
    # return render(request, "index.html", context = {"body": "<h1>Hello World!</h1>"})
    # return render(request, "index.html", context = {"person": Person("Tom")})
    # header = "Данные пользователя"
    # langs = ["Python", "Java", "C#"]
    # user = {"name": "Tom", "age" : 23}
    # address = ("Абрикосовая", 23, 45)
    #
    # data = {"header": header, "langs": langs, "user": user, "address": address}
    # return render(request, "index.html", context=data)

# class Person:
#     def __init__(self, name):
#         self.name = name # имя человека

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")