from django.shortcuts import render, HttpResponse

def Home(request):
    return HttpResponse("<h1>Hello Yashar!</h1>")