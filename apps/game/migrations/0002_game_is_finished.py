# Generated by Django 2.0.7 on 2018-07-11 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
    ]
