from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def conf(request):
    return render(request, 'main/conf.html')
