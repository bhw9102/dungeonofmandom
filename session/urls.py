from django.conf.urls import url
from django.urls import path, include
from session import views

urlpatterns = [
    path('play/', include([
        path('index/', views.index, name='index'),
    ]))
]

