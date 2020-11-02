from django.urls.conf import path
from helloworld import views
urlpatterns = [
    path('', views.hello),
]