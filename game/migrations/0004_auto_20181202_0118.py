# Generated by Django 2.1.3 on 2018-12-02 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20181202_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentclass',
            name='name',
            field=models.CharField(help_text='이름', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='jobclass',
            name='name',
            field=models.CharField(help_text='이름', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='monsterclass',
            name='name',
            field=models.CharField(help_text='이름', max_length=32, unique=True),
        ),
    ]
