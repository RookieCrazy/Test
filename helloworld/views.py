from django.shortcuts import render, HttpResponse
from helloworld.models import People
from django.template import Context, Template
# Create your views here.


def hello(request):
    person = People(name='lois', job='officer')
    html = '''
        <html>
            <head>test</head>
            <body>
            <h1>hello,{{person.name}}!</h1>
            </body>
        </html>

    '''
    t = Template(html)
    c = Context({'person': person})
    web_page = t.render(c)
    return HttpResponse(web_page)