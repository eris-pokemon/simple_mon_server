from django.db import models


class MonsterDex(models.Model):
    """
    Stores the information common to every monster.
    Presently, stores the number and the name of the monster.
    """
    monster_number = models.IntegerField(primary_key=True)
    monster_name = models.CharField(max_length=64)

    def __str__(self):
        return str(self.monster_name)
