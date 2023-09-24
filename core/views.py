from django.shortcuts import render
#render es la peticion del usuario
# model template vista (MTV) siosi
# Create your views here.

def home(request):
    return render(request,"home.html")