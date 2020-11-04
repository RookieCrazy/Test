from django.shortcuts import render, HttpResponse
import json
import requests
# from helloworld.models import People
# from django.template import Context, Template

# Create your views here.


def hello(request):
    api_request = requests.get("https://api.github.com/users?since=0")
    api = json.loads(api_request.content)
    return render(request, "test1/hello.html", {
        "api": api
    })

def user(request):
    user = request.POST['user']
    user_request = requests.get("https://api.github.com/users/"+user)
    username = json.loads(user_request.content)

    return render(request, "test1/user.html", {"user": user, "username": username})

# def hello(request):
#     return render(request, 'test1/hello.html', {})
    # person = People(name='lois', job='officer')
    # html = '''
    #     <html>
    #         <head>test</head>
    #         <body>
    #         <h1>hello,{{person.name}}!</h1>
    #         </body>
    #     </html>

    # '''
    # t = Template(html)
    # c = Context({'person': person})
    # web_page = t.render(c)
    # return HttpResponse(web_page)