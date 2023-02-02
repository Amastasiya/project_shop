from django.shortcuts import render
#from .models import Employee
#from .models import Guide
#from django.http import HttpResponse

#import json

def index(request):
    return render(
    request,  # Запрос
    'home_page/index.html',  # путь к шаблону
    #context  # подстановки словарь
    )


# Create your views here.
