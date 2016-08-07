## Current Expected Server Design
### Things the Server Will Need to do:
 - Know information about all of the monsters.
 - Keep track of all player accounts.
 - Keep track of each player's inventory.
 - Keep track of each specific instance of a monster in a player's roster.
 - Generate monster spawns for players to find.
 - Track players and set up battles.
 - Store game settings.
 - Store monster abilities.
 
### Calls the Server Will Understand:
 - A client will be able to authenticate themselves.
 - A client will be able to load their inventory.
 - A client will be able to modify their inventory and persist it to the server.
 - A client will be able to get their monster roster.
 - A client will be able to request information on each monster in their roster.
 - A client will be able to modify their monster roster and persist it to the server.
 - A client will be able to update the server with their position.
 - A client will be able to request a list of nearby monsters.
 - A client will be able to matchmake with other players.
 
### Other Potential Server Functions:
 - Allow a client to ask for any rules or config changes (saves having to push a game update everytime a slight tweak to an ability is made).
 
