#!/usr/bin/env python3
class CashRegister:
    def __init__(self):
        self.total = 0  # This will track the total cost of items
        self.items = []  # List to track all items added, each as a tuple (quantity, price)
        self.last_transaction = 0  # Tracks the amount of the last transaction

    def add_item(self, price, quantity=1):
        """
        Adds an item to the register with a price and quantity.
        Updates the total amount and stores the transaction for later voiding.
        """
        self.total += price * quantity
        self.items.append((price, quantity))
        self.last_transaction = price * quantity

    def apply_discount(self, discount):
        """
        Applies a discount to the total. Discount is in percentage (0-100).
        """
        if discount < 0 or discount > 100:
            raise ValueError("Discount must be between 0 and 100.")
        discount_amount = self.total * (discount / 100)
        self.total -= discount_amount

    def void_last_transaction(self):
        """
        Voids the last transaction added. This will remove the last item
        added to the register.
        """
        self.total -= self.last_transaction
        # Remove the last item from the items list
        self.items.pop()
        self.last_transaction = 0  # Reset last transaction to prevent it from being used again

    def get_total(self):
        """
        Returns the current total after all items and discounts have been applied.
        """
        return self.total


