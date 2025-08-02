from Restaurant import *

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

        match choice:
            case '1':
                restaurant.describe_restaurant()
            case '2':
                restaurant.set_number_served()
            case '3':
                restaurant.add_number_served()
            case '4':
                print('Goodbye!')
                break
            case _:
                print('Invalid Choice, Try Again:')

        print(f'[{restaurant.restaurant_name}] - {restaurant.number_served} People Served Today')

if __name__ == "__main__":
    main_menu(ice_cream_stand)