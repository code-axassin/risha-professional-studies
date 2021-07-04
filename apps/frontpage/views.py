from django.shortcuts import render

def frontpage(request):
    return render(request, "frontpage/base.html")

def about(request):
    return render(request, "frontpage/about.html")