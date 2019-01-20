from django import forms
from session.models import Player, Room, RoomPlayer


class NameForm(forms.Form):
    name = forms.CharField(label='name', max_length=12)


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name']


class RoomPlayerForm(forms.ModelForm):
    class Meta:
        model = RoomPlayer
        fields = ['room', 'player', 'state']



