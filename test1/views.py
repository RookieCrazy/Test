from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def test1(request):
    return render(request, "test1/t1.html", {
        "title": "Test web",
        "content": "ceshiceshiceshi718049519"
    })


def test2(request):
    return render(request, "test1/t1.html", {
        "title": "test2",
        "content": "jdoaphoieq938"
    })
