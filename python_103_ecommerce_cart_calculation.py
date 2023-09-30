"""
Exercise: E-commerce Cart Calculation (id=103)

Requirements:

You are building a simple e-commerce cart calculator. Users can add items to their cart, and your task is to calculate the total cost of the items in the cart while handling potential errors gracefully.

Function Name: calculate_cart_total(cart_items)

Parameters:
- cart_items (list of dictionaries): A list representing the user's shopping cart. Each item in the cart is a dictionary with 'name', 'price', and 'quantity' keys.

Handle exceptions when users:
   - Try to add an item with a negative price or quantity.
   - Attempt to calculate the total when the cart is empty.
Display informative error messages for each type of exception.

Examples:

Here's an example of how the program should work:

# User's shopping cart
cart_items = [
    {"name": "Laptop", "price": 1000, "quantity": 2},
    {"name": "Mouse", "price": 20, "quantity": 3},
]

# Calculate the total cost of items in the cart
calculate_cart_total(cart_items)  # Output: 2060

# User adds an item with a negative price
cart_items.append({"name": "Headphones", "price": -50, "quantity": 1})
calculate_cart_total(cart_items)  # Error: Invalid price. Please enter a positive number.

# User tries to calculate the total with an empty cart
calculate_cart_total([])  # Error: Cart is empty.

Instructions:

1. Implement the `calculate_cart_total` function according to the specified requirements, using try and except blocks to handle exceptions as described.
2. Provide clear and informative error messages for each type of exception to guide users.

"""

cart_items = [
    {"name": "Laptop", "price": 1000, "quantity": 2},
    {"name": "Mouse", "price": 20, "quantity": 3},
]
# modify cart_items as needed


def calculate_cart_total(cart_items):
    try:
        if not cart_items:
            raise ValueError("Error: Cart is empty.")

        cart_total = 0
        for cart_item in cart_items:
            if cart_item["price"] < 0 or cart_item["quantity"] < 0:
                    raise ValueError("Error: Invalid price or quantity. Please enter positive numbers.")
            cart_total += cart_item["price"] * cart_item["quantity"]
        return cart_total


    except ValueError as ve:
        return str(ve)






#### Unit Tests #######
#### DON NAME MAKE ANY CHANGES IN THIS CLASS #####
import unittest


class TestCartCalculation(unittest.TestCase):

    def test_cart_total(self):
        """
        Test the calculation of the total cost in the cart.
        """
        cart_items = [
            {"name": "Laptop", "price": 1000, "quantity": 2},
            {"name": "Mouse", "price": 20, "quantity": 3},
        ]
        self.assertEqual(calculate_cart_total(cart_items), 2060)

    def test_negative_price(self):
        """
        Test adding an item with a negative price.
        """
        cart_items = [
            {"name": "Laptop", "price": 1000, "quantity": 2},
        ]
        cart_items.append({"name": "Headphones", "price": -50, "quantity": 1})
        self.assertEqual(calculate_cart_total(cart_items), "Error: Invalid price or quantity. Please enter positive numbers.")

    def test_negative_quantity(self):
        """
        Test adding an item with a negative quantity.
        """
        cart_items = [
            {"name": "Laptop", "price": 1000, "quantity": 2},
        ]
        cart_items.append({"name": "Mouse", "price": 20, "quantity": -1})
        self.assertEqual(calculate_cart_total(cart_items), "Error: Invalid price or quantity. Please enter positive numbers.")

    def test_empty_cart(self):
        """
        Test calculating the total of an empty cart.
        """
        self.assertEqual(calculate_cart_total([]), "Error: Cart is empty.")

if __name__ == "__main__":
    unittest.main()

    # cart_items = [
    #     {"name": "Laptop", "price": 1000, "quantity": 2},
    #     {"name": "Mouse", "price": 20, "quantity": 3},
    # ]
    # calculate_cart_total()
