import datetime
from django.db import models
from dungeonofmandom.models import NameDescMixin, CreatedUpdatedMixin
from game.models import HeroClass, ItemClass, MonsterClass


class Player(NameDescMixin, CreatedUpdatedMixin, models.Model):
    def __str__(self):
        return self.name


ROOM_STATE = (
    ('READY', '준비'),
    ('PLAY', '진행'),
    ('END', '종료')
)


class Room(NameDescMixin, CreatedUpdatedMixin, models.Model):
    state = models.CharField(max_length=16, choices=ROOM_STATE, default='READY', help_text='방의 진행 상태')

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        if not self.name:
            self.name = str(self.created_at)
        super(Room, self).save()


ROUND_STATE = (
    ('PLAY', '진행'),
    ('END', '종료')
)


class Round(CreatedUpdatedMixin, models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    state = models.CharField(max_length=16, choices=ROUND_STATE, default='PLAY', help_text='라운드의 진행 상태')
    order = models.PositiveSmallIntegerField(default=1, help_text='라운드 회차')

    def __str__(self):
        return '{}-{}'.format(self.room, str(self.order))


ROOM_PLAYER_STATE = (
    ('JOIN', '참여중'),
    ('LEAVE', '떠남'),
    ('WIN', '게임 승리'),
    ('LOSE', '게임 패배')
)


class RoomPlayer(CreatedUpdatedMixin, models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    state = models.CharField(max_length=16, choices=ROOM_PLAYER_STATE, help_text='플레이어의 방 참여 상태')

    def __str__(self):
        return '{room}-{player}'.format(room=self.room, player=self.player)


ROUND_PLAYER_STATE = (
    ('PLAY', '게임중'),
    ('PASS', '패스'),
    ('DUNGEON', '던전'),
    ('FAIL', '던전 실패'),
    ('SUCCESS', '던전 성공')
)


class RoundPlayer(CreatedUpdatedMixin, models.Model):
    round = models.ForeignKey('Round', on_delete=models.CASCADE)
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    state = models.CharField(max_length=16, choices=ROUND_PLAYER_STATE, default='PLAY')

    def __str__(self):
        return '{}-{}'.format(self.round, self.player)


MONSTER_PLACE = (
    ('DECK', '덱'),
    ('DUNGEON', '던전'),
    ('REMOVE', '제거'),
    ('DEFEATED', '무찌름')
)


class Monster(CreatedUpdatedMixin, models.Model):
    round = models.ForeignKey('Round', on_delete=models.CASCADE)
    monster = models.ForeignKey('game.MonsterClass', on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField(default=0, help_text='카드의 등장 순서')
    place = models.CharField(max_length=16, choices=MONSTER_PLACE, default='DECK')

    def __str__(self):
        return '{}-{}'.format(self.round, self.monster)


class Hero(CreatedUpdatedMixin, models.Model):
    round = models.ForeignKey('Round', on_delete=models.CASCADE)


ITEM_PLACE = (
    ('EQUIPPED', '장비'),
    ('REMOVE', '제거')
)


class Item(CreatedUpdatedMixin, models.Model):
    round = models.ForeignKey('Round', on_delete=models.CASCADE)
    item = models.ForeignKey('game.ItemClass', on_delete=models.CASCADE)
    place = models.CharField(max_length=16, choices=ITEM_PLACE, default='EQUIPPED')
    defeat = models.ManyToManyField('game.MonsterClass', blank=True)


class RemovedPackage(CreatedUpdatedMixin, models.Model):
    round_player = models.ForeignKey('RoundPlayer', on_delete=models.CASCADE)
    monster = models.ForeignKey('Monster', on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)


