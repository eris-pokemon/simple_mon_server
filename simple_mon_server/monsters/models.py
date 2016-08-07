from django.db import models


class MonsterDex(models.Model):
    """
    Stores the information common to every monster.
    Presently, stores the number and the name of the monster.
    """
    monster_number = models.IntegerField(primary_key=True)
    monster_name = models.CharField(max_length=64)


class Monster(models.Model):
    """
    Stores a specific monster instance.
    This includes what sort of monster it is, which player owns it and the nickname the player has given it.
    """
    monster_type = models.ForeignKey(MonsterDex, on_delete=models.CASCADE)
    monster_owner = models.ForeignKey('player.Player', on_delete=models.CASCADE)
    monster_nickname = models.CharField(max_length=32)