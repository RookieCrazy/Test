from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def test1(request):
    return HttpResponse("test1 测试成功")

def test2(request):
    return HttpResponse("test2 测试成功 ")

