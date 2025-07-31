from Restaurant import *

# Test Comment

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