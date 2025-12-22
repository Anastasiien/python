# app/views.py
from django.http import HttpResponse

def collection_list(request):
    return HttpResponse("Привет! Это ваша коллекция.")
