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
        self.number_served = num

    def add_number_served(self):
        self.number_served += 1

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavours = ['Chocolate', 'Strawberry', 'Vanilla', 'Mint Choc', 'Honeycomb']

    def print_flavours(self):
        print(flavour for flavour in self.flavours)


restaurant1 = Restaurant('McDonalds', 'American')
restaurant2 = Restaurant('Wagamama', 'Japanese')
restaurant3 = Restaurant('The Dirty Onion', 'Irish')
ice_cream_stand = IceCreamStand('Ice Cream Shop', 'Ice Cream')

def main_menu(restaurant):
    print(f'Welcome to {restaurant.restaurant_name}!\n'
          f'1. Describe Restaurant\n'
          f'2. Set Number of People Served\n'
          f'3. Add Person Served\n'
          f'4. Exit')

    while True:
        choice = input("Enter your choice (1-4):")

        if choice == '1':
            restaurant.describe_restaurant()
        elif choice == '2':
            restaurant.set_number_served()
        elif choice == '3':
            restaurant.add_number_served()
        elif choice == '4':
            print('Goodbye!')
            break
        else:
            print('Invalid Choice, Try Again:')

        print(f'[{restaurant.restaurant_name}] - {restaurant.number_served} People Served Today')

if __name__ == "__main__":
    main_menu(ice_cream_stand)