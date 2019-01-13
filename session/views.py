from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from session.models import Player, Room
from session.models import ROOM_STATE
from session.forms import NameForm, RoomForm
from session.constants import *
from django.core import serializers


def index(request):
    return render(request, 'session/index.html')


def entrance(request):
    return render(request, 'session/entrance.html')


def login(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data[CONST_NAME]
            player = Player.objects.filter(name=name).first()

            if player is None:
                # 등록된 플레이어가 없을 때
                player = Player.objects.create(name=name)
            request.session[IS_LOGINED] = True
            request.session[CONST_PLAYER_ID] = player.id
            player_data = serializers.serialize('json', Player.objects.filter(pk=player.id), fields=('id', 'name'))
            request.session[CONST_PLAYER] = player_data
            return HttpResponseRedirect(reverse('room-list'))
    # GET
    player_id = request.session.get(CONST_PLAYER_ID)
    player_data = serializers.deserialize('json', request.session.get(CONST_PLAYER), ignorenonexistent=True)
    print(player_data)
    form = NameForm(initial={'name': ''})
    if player_id is not None:
        player = Player.objects.filter(pk=player_id).first()
        form = NameForm(initial={'name': player.name})
    return render(request, 'session/login.html', {'form': form})


def room_list(request):
    # GET
    room_list_c = Room.objects.filter(state='READY').all()
    return render(request, 'session/room_list.html', {CONST_ROOM_LIST: room_list_c})


def create_room(request):
    if request.method == "POST":
        print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            new_room = form.save()
            return HttpResponseRedirect(reverse('room-list'))
    # GET
    form = RoomForm(initial={'name': ''})
    return render(request, 'session/create_room.html', {'form': form})

