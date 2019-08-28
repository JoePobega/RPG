#!/usr/bin/env python3

class Inventory:
    """Class used for managing the player's inventory."""

    def __init__(self):
        """Initialize an empty item list."""
        self.item_list = []

    def __call__(self):
        """Make the instance callable to quickly access inventory."""
        return self.get_items()

    def get_items(self):
        """Return the current list of items."""
        return self.item_list

    def has_item(self, item_name):
        """Check if a player has an item."""
        if item_name in self.item_list:
            return True
        return False

    def add_item(self, item_name):
        """Add an item to a player's inventory if it doesn't already exist."""
        if not self.has_item(item_name):
            self.item_list.append(item_name)

    def remove_item(self, item_name):
        """Remove an item in a player's inventory if it exists."""
        if item_name in self.item_list:
            self.item_list.remove(item_name)
