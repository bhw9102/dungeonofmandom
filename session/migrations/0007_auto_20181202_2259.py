# Generated by Django 2.1.3 on 2018-12-02 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0006_hero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='desc',
            field=models.TextField(blank=True, help_text='설명', null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='desc',
            field=models.TextField(blank=True, help_text='설명', null=True),
        ),
    ]
