# Generated by Django 2.0.7 on 2018-07-11 18:59

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', django.contrib.postgres.fields.jsonb.JSONField(default=[])),
                ('max_hit_ships', models.IntegerField(default=0)),
            ],
        ),
    ]
