#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
       
        amount = price * quantity

        
        self.total += amount
        self.last_transaction = amount

      
        for _ in range(quantity):
            self.items.append(title)

        
        print(f"Added {title} to your cart. Total is now ${self.total}.")
        return self.total

    def apply_discount(self):
        if self.discount > 0:
            self.total = int(self.total * (100 - self.discount) / 100)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction

        if self.total < 0:
            self.total = 0

        self.last_transaction = 0

        return self.total
