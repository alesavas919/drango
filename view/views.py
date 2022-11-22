from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    data = {'name':'test','group':["algo","esta","mal"]}
    return render(request, "Index.html",context=data)

def test(request):
    return HttpResponse("Prueba")

def find(request):
    data = {"some":"test: " + request.GET["test"]}

    return render(request,"Index.html",data)