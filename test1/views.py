from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def test1(request):
    return render(request, "test1/t1.html", {})


def test2(request):
    return render(request, "test1/t2.html", {})
