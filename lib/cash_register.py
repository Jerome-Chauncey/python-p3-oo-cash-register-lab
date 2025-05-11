#!/usr/bin/env python3


class CashRegister:

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = {"title": title, "price": price, "quantity": quantity}

    def apply_discount(self):
        try:
            if self.total == 0:
                raise ValueError("There is no discount to apply.")
            discount_amount = (self.total * self.discount) / 100
            final_price = self.total - discount_amount
            self.total = final_price
            print(f"After the discount, the total comes to ${int(self.total)}.")
        except ValueError as e:
            print(str(e))

        return self.total


    def void_last_transaction(self):
        if self.items:
            last_price = self.last_transaction["price"] * self.last_transaction["quantity"]
            self.total -= last_price
            for _ in range(self.last_transaction["quantity"]):
                self.items.pop()
        else:
            print("No transaction to void.")


register = CashRegister(10)
# register.add_item("macbook air", 1000)
register.add_item("Notebook", 5.00, 2)
print("Total after adding items:", register.total)
print("Items:", register.items)
# register.add_item("tomato", 1.76, 2)

# print("Before voiding:", register.total)
# print(register.items)
# print(register.total)
register.apply_discount()
print("Total after discount:", register.total)


register.void_last_transaction()
print("Total after void:", round((register.total), 2))
print("Items after void:", register.items)
