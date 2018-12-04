# Generated by Django 2.1.3 on 2018-12-01 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='이름', max_length=32)),
                ('desc', models.TextField(help_text='설명')),
                ('health', models.PositiveSmallIntegerField(default=0, help_text='HP')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JobClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='이름', max_length=32)),
                ('desc', models.TextField(help_text='설명')),
                ('health', models.PositiveSmallIntegerField(default=0, help_text='HP')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MonsterClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='이름', max_length=32)),
                ('desc', models.TextField(help_text='설명')),
                ('attack', models.PositiveSmallIntegerField(default=0, help_text='ATK')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='equipmentclass',
            name='defeat',
            field=models.ManyToManyField(to='game.MonsterClass'),
        ),
    ]
