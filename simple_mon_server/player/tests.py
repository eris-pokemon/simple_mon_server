from django.test import TestCase

from .models import Player, Inventory, Monster
from items.models import Item
from monsters.models import MonsterDex


class PlayerTests(TestCase):
    def test_create_player(self):
        """
        Tests creation of a player.
        """
        nickname = "Bob"
        test_player = Player(nickname=nickname)
        test_player.save()
        Player.objects.get(nickname=nickname)

    def test_add_inventory(self):
        """
        Tests adding two items to the player's inventory.
        """
        nickname = "Bob"
        cnt_a = 42
        cnt_b = 47
        item_a = Item(name="Banapple", description="Is it a Banana? An Apple? No one cares!")
        item_b = Item(name="Apprange", description="Turns out you can compare Apples and Oranges.")
        # Create player and existing items
        Player(nickname=nickname).save()
        item_a.save()
        item_b.save()
        # Save the items.
        test_player = Player.objects.get(nickname=nickname)
        test_item_a = Item.objects.get(name=item_a.name)
        test_item_b = Item.objects.get(name=item_b.name)
        inventory_a = Inventory(item_owner=test_player, item_type=test_item_a, count=cnt_a)
        inventory_a.save()
        inventory_b = Inventory(item_owner=test_player, item_type=test_item_b, count=cnt_b)
        inventory_b.save()
        # Get the items.
        inv = test_player.inventory
        # Check the results.
        self.assertEqual(inv[0], inventory_a)
        self.assertEqual(inv[1], inventory_b)

    def test_update_inventory(self):
        nickname = "Bob"
        cnt = 42
        new_cnt = 47
        name = "Banapple"
        description = "Is it a Banana? An Apple? No one cares!"
        # Create player and existing item
        Player(nickname=nickname).save()
        item = Item(name=name, description=description)
        item.save()
        test_player = Player.objects.get(nickname=nickname)
        test_item = Item.objects.get(name=name)
        inventory = Inventory(item_owner=test_player, item_type=test_item, count=cnt)
        inventory.save()
        # Update inventory.
        inv = test_player.inventory[0]
        inv.count = new_cnt
        inv.save()
        inv = test_player.inventory[0]
        # Check if the count of the item is correct.
        self.assertTrue(inv.count == new_cnt)


    def test_add_monster(self):
        nickname = "Bob"
        nick_a = "Digger"
        nick_b = "Zappy"
        name_a = "Badgerino"
        name_b = "Elecster"
        num_a = 1
        num_b = 2
        # Create player and monsterdex entries.
        test_player = Player(nickname=nickname)
        test_player.save()
        dex_a = MonsterDex(monster_number=num_a, monster_name=name_a)
        dex_b = MonsterDex(monster_number=num_b, monster_name=name_b)
        dex_a.save()
        dex_b.save()
        test_player = Player.objects.get(nickname=nickname)
        # Add monsters to the player.
        mon_a = Monster(monster_type=dex_a, monster_owner=test_player, monster_nickname=nick_a)
        mon_b = Monster(monster_type=dex_b, monster_owner=test_player, monster_nickname=nick_b)
        mon_a.save()
        mon_b.save()

        #Get the monsters back to check.
        monsters = test_player.roster
        self.assertEqual(monsters[0], mon_a)
        self.assertEqual(monsters[1], mon_b)
