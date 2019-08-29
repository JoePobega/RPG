## Including Inventory

`from lib import inventory`

## Instantiating New Inventory

`inv = inventory.Inventory()`

## Accessing inventory

`inv()` or `inv.get_items()`

## Checking if a player owns an item

`inv.has_item("surgical flashlight")`

## Adding an item to the player's inventory

`inv.add_item("surgical flashlight")`

## Removing an item from a player's inventory

`inv.remove_item("surgical flashlight")

## Note

It is up to the game designer to control what items get passed in and out of the inventory. The Inventory library doesn't do any sanity checking of items, and currently doesn't return any state of whether a method took any action (for example trying to remove an item that doesn't exist requires the designer to explicitly check the inventory for the item if they want to know whether the player had it before it was removed.)
