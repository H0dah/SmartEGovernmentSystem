from django.shortcuts import render

# Create your views here.
def splash(request):
    return render(request, 'splash.html')
def login(request):
    return render(request, 'login.html')
def lisence2(request):
    return render(request, 'lisence2.html')
def lisence(request):
    return render(request, 'lisence.html')
def index(request):
    return render(request, 'index.html')
def id2(request):
    return render(request, 'id2.html')
def id(request):
    return render(request, 'id.html')
def Birth3(request):
    return render(request, 'Birth3.html')
def Birth2(request):
    return render(request, 'Birth2.html')
def Birth(request):
    return render(request, 'Birth.html')
