from django.http import request
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.context import RequestContext
import json
import requests


# Create your views here.
def test1(request):
    api_request = requests.get("https://api.github.com/users?since=0")
    api = json.loads(api_request.content)
    return render(request, "test1/t2.html", {
        "api": api
    })


def test2(request):
    return render(request, "test1/t1.html", {
        "title": "test2",
        "content": "jdoaphoieq938"
    })
