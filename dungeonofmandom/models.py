from django.conf.global_settings import MEDIA_URL
from django.db import models
from functools import partial
from .tools import build_file_path


class NameDescMixin(models.Model):
    name = models.CharField(max_length=32, unique=True, help_text="이름")
    desc = models.TextField(help_text="설명")

    class Meta:
        abstract = True


class ImageMixin(models.Model):
    image = models.ImageField(blank=True, null=True, default=None, upload_to=partial(build_file_path))

    class Meta:
        abstract = True

    def image_url(self):
        if bool(self.image):
            return MEDIA_URL + self.image.url
        else:
            return 'about:blank'


class CreatedUpdatedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False, help_text='생성 시간')
    updated_at = models.DateTimeField(auto_now=True, editable=False, help_text='갱신 시간')

    class Meta:
        abstract = True
