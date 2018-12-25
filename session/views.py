from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from session.models import Player
from session.forms import NameForm
from session.constants import *


def index(request):
    return render(request, 'session/index.html')


def entrance(request):
    return render(request, 'session/entrance.html')


def login(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            player = Player.objects.filter(name=form.cleaned_data["name"]).first()

            if player is None:
                # 등록된 플레이어가 없을 때
                player = Player.objects.create(name=form.name)
            request.session[IS_LOGINED] = True
            request.session[CONST_PLAYER] = player
            return HttpResponseRedirect(reverse('room-list'))
    # GET
    player = request.session.get(CONST_PLAYER)
    form = NameForm(initial={'name': ''})
    if player is not None:
        form = NameForm(initial={'name': player.name})
    return render(request, 'session/login.html', {'form': form})


def room_list(request):
    return render(request, 'session/room_list.html')


