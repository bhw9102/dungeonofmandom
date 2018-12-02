import datetime
from django.db import models
from dungeonofmandom.models import NameDescMixin, CreatedUpdatedMixin


class Player(NameDescMixin, models.Model):
    def __str__(self):
        return self.name


ROOM_STATE = (
    ('READY', '준비'),
    ('PLAY', '진행'),
    ('END', '종료')
)


class Room(NameDescMixin, CreatedUpdatedMixin, models.Model):
    state = models.CharField(max_length=16, choices=ROOM_STATE, help_text='방의 진행 상태')

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.now()
        if not self.name:
            self.name = str(self.created_at)
        self.updated_at = datetime.datetime.now()
        super(Room, self).save()


ROOM_PLAYER_STATE = (
    ('JOIN', '참여중'),
    ('LEAVE', '떠남')
)


class RoomPlayer(CreatedUpdatedMixin, models.Model):
    player = models.ForeignKey('Player', null=True, on_delete=models.SET_NULL)
    room = models.ForeignKey('Room', null=True, on_delete=models.SET_NULL)
    state = models.CharField(max_length=16, choices=ROOM_PLAYER_STATE, help_text='플레이어의 방 참여 상태')

    def __str__(self):
        if not bool(self.player) or not bool(self.room):
            return 'Null-Null-{}'.format(self.created_at)
        return '{room}-{player}'.format(room=self.room, player=self.player)

    def save(self, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        super(RoomPlayer, self).save()





