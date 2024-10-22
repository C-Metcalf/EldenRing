from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    return redirect("godfrey:godfrey")


def godfrey(request):
    return render(request, "godfrey/index.html")