# Generated by Django 2.1.3 on 2018-12-02 01:34

from django.db import migrations, models
import dungeonofmandom.tools
import functools


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20181202_0118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipmentclass',
            name='imagemixin_ptr',
        ),
        migrations.RemoveField(
            model_name='jobclass',
            name='imagemixin_ptr',
        ),
        migrations.RemoveField(
            model_name='monsterclass',
            name='imagemixin_ptr',
        ),
        migrations.AddField(
            model_name='equipmentclass',
            name='id',
            field=models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipmentclass',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=functools.partial(dungeonofmandom.tools.build_file_path, *(), **{})),
        ),
        migrations.AddField(
            model_name='jobclass',
            name='id',
            field=models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobclass',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=functools.partial(dungeonofmandom.tools.build_file_path, *(), **{})),
        ),
        migrations.AddField(
            model_name='monsterclass',
            name='id',
            field=models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='monsterclass',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=functools.partial(dungeonofmandom.tools.build_file_path, *(), **{})),
        ),
    ]