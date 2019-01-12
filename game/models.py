from django.db import models
from dungeonofmandom.models import NameDescMixin, ImageMixin


class HeroClass(NameDescMixin, ImageMixin, models.Model):
    health = models.PositiveSmallIntegerField(default=0, help_text="HP")

    def __str__(self):
        return self.name


class ItemClass(NameDescMixin, ImageMixin, models.Model):
    hero = models.ForeignKey('HeroClass', on_delete=models.CASCADE)
    health = models.PositiveSmallIntegerField(default=0, help_text="HP")
    defeat = models.ManyToManyField('MonsterClass', null=True, blank=True)

    def __str__(self):
        return self.name


class MonsterClass(NameDescMixin, ImageMixin, models.Model):
    attack = models.PositiveSmallIntegerField(default=0, help_text="ATK")
    count = models.PositiveSmallIntegerField(default=0, help_text="게임에 들어가는 카드 장 수")

    def __str__(self):
        return self.name

