from django.db import models
from dungeonofmandom.models import NameDescMixin, ImageMixin


class JobClass(NameDescMixin, ImageMixin, models.Model):
    health = models.PositiveSmallIntegerField(default=0, help_text="HP")

    def __str__(self):
        return self.name


class EquipmentClass(NameDescMixin, ImageMixin, models.Model):
    health = models.PositiveSmallIntegerField(default=0, help_text="HP")
    defeat = models.ManyToManyField('MonsterClass')

    def __str__(self):
        return self.name


class MonsterClass(NameDescMixin, ImageMixin, models.Model):
    attack = models.PositiveSmallIntegerField(default=0, help_text="ATK")
    count = models.PositiveSmallIntegerField(default=0, help_text="게임에 들어가는 카드 장 수")

    def __str__(self):
        return self.name

