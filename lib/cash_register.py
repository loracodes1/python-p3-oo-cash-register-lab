class CashRegister:
    def __init__(self, discount=0):
        self.total = 0  # Total amount
        self.items = []  # List to store item data (dictionaries with title, price, and quantity)
        self.discount = discount  # Discount percentage

    def add_item(self, title, price, quantity=1):
        # Add the item as a dictionary to the items list
        item = {
            "title": title,
            "price": price,
            "quantity": quantity
        }
        self.items.append(item)  # Append the item dictionary to the list
        self.total += price * quantity

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            # Format the total without decimals if it's an integer
            if self.total.is_integer():
                print(f"After the discount, the total comes to ${int(self.total)}.")
            else:
                print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()  # Remove the last item dictionary
            # Subtract the item's price multiplied by its quantity from the total
            self.total -= last_item["price"] * last_item["quantity"]

    def get_item_titles(self):
        # Return only the titles of the items
        return [item["title"] for item in self.items]

# Example usage:
if __name__ == "__main__":
    # Create a CashRegister object with a 20% discount
    register = CashRegister(20)
    
    # Add some items
    register.add_item("Laptop", 1000, 1)
    register.add_item("Mouse", 50, 2)
    
    # Get the titles of the items
    print(register.get_item_titles())  # This will print ['Laptop', 'Mouse']
