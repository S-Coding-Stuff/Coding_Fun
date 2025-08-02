"""Quickly learning classes"""

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print("Restaurant:", self.restaurant_name)
        print("Cuisine:", self.cuisine_type)
        print("People Served Today:", self.number_served)

    def set_number_served(self):
        num = input("How many customers served today?")
        self.number_served = int(num)

    def add_number_served(self):
        self.number_served += 1

# Ice Cream Stand class inherits from Restaurant
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavours = ['Chocolate', 'Strawberry', 'Vanilla', 'Mint Choc', 'Honeycomb']

    def print_flavours(self):
        print(flavour for flavour in self.flavours)