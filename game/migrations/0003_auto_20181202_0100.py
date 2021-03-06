# Generated by Django 2.1.3 on 2018-12-02 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dungeonofmandom', '__first__'),
        ('game', '0002_monsterclass_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipmentclass',
            name='id',
        ),
        migrations.RemoveField(
            model_name='jobclass',
            name='id',
        ),
        migrations.RemoveField(
            model_name='monsterclass',
            name='id',
        ),
        migrations.AddField(
            model_name='equipmentclass',
            name='imagemixin_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dungeonofmandom.ImageMixin'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobclass',
            name='imagemixin_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dungeonofmandom.ImageMixin'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='monsterclass',
            name='imagemixin_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dungeonofmandom.ImageMixin'),
            preserve_default=False,
        ),
    ]
