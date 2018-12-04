from django.conf.urls import url
from django.urls import path, include
from django.views.generic import RedirectView
from session import views


urlpatterns = [
    path('', RedirectView.as_view(url='play/entrance', permanent=False), name='redirect_play'),
    path('play/', include([
        path('', RedirectView.as_view(url='entrance/', permanent=False), name='redirect_play'),
        path('index/', views.index, name='index'),
        path('entrance/', views.entrance, name='entrance')
    ]))
]

