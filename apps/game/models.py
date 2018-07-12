from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.


class Game(models.Model):

    board = JSONField(default=[])
    max_hit_ships = models.IntegerField(default=0)
    is_finished = models.BooleanField(default=False)
