import datetime
from django.db import models
from dungeonofmandom.models import NameDescMixin, CreatedUpdatedMixin
from game.models import HeroClass, ItemClass, MonsterClass


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
        if not self.name:
            self.name = str(self.created_at)
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


MONSTER_PLACE = (
    ('DECK', '덱'),
    ('DUNGEON', '던전'),
    ('REMOVE', '제거'),
    ('DEFEATED', '무찌름')
)


class Monster(CreatedUpdatedMixin, models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    monster = models.ForeignKey('game.MonsterClass', on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField(default=0, help_text='카드의 등장 순서')
    place = models.CharField(max_length=16, choices=MONSTER_PLACE, default='DECK')


ITEM_PLACE = (
    ('EQUIPPED', '장비'),
    ('REMOVE', '제거')
)


class Item(CreatedUpdatedMixin, models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    item = models.ForeignKey('game.ItemClass', on_delete=models.CASCADE)
    place = models.CharField(max_length=16, choices=ITEM_PLACE, default='EQUIPPED')


class RemovedPackage(CreatedUpdatedMixin, models.Model):
    room_player = models.ForeignKey('RoomPlayer', on_delete=models.CASCADE)
    monster = models.ForeignKey('Monster', on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)


