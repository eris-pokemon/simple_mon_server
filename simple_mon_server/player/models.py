from django.contrib.postgres.fields import HStoreField, JSONField
from django.db import models
from uuid import uuid4


class Player(models.Model):
    """
    Stores the information related to a player.
    Presently, stores a nickname, the player's inventory and information on their monsters.
    inventory is a {item_id: count} dictionary.
    monster_roster is intended to be json encoding the various attributes of all of a player's monsters.
    """
    player_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nickname = models.CharField(max_length=32, unique=True)
    inventory = HStoreField()

