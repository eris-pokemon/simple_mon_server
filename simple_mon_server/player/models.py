from django.db import models
from uuid import uuid4


class Player(models.Model):
    """
    Stores the information related to a player.
    Presently, stores a nickname.
    """
    player_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nickname = models.CharField(max_length=32, unique=True)

    @property
    def inventory(self):
        """
        Get's the players inventory.
        """
        return Inventory.objects.filter(item_owner=self)

    @property
    def roster(self):
        """
        Get's the player's roster of monsters.
        """
        return Monster.objects.filter(monster_owner=self)

    def __str__(self):
        return "{}, {}".format(self.player_id, self.nickname)


class Monster(models.Model):
    """
    Stores a specific monster instance.
    This includes what sort of monster it is, which player owns it and the nickname the player has given it.
    """
    monster_type = models.ForeignKey("monsters.MonsterDex", on_delete=models.CASCADE)
    monster_owner = models.ForeignKey(Player, on_delete=models.CASCADE)
    monster_nickname = models.CharField(max_length=32)

    def __str__(self):
        return "{} belongs to: {} and is named: {}".format(self.monster_type.monster_name, self.monster_owner.nickname, self.monster_nickname)


class Inventory(models.Model):
    """
    Stores a single object for a player.
    """
    item_owner = models.ForeignKey(Player, on_delete=models.CASCADE)
    item_type = models.ForeignKey("items.Item", on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return "{}: {}".format(self.item_type.name, self.count)
