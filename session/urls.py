from django.conf.urls import url
from django.urls import path, include
from django.views.generic import RedirectView
from session import views


urlpatterns = [
    path('', RedirectView.as_view(url='play/index', permanent=False), name='redirect_play'),
    path('play/', include([
        path('', RedirectView.as_view(url='index/', permanent=False), name='redirect_play'),
        path('index/', views.index, name='index'),
        path('entrance/', views.entrance, name='entrance'),
        path('login/', views.login, name='login'),
        path('room-list/', views.room_list, name='room_list')
    ]))
]

