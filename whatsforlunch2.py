# The program that picks where we are going to eat lunch!

# Make the lists
# styles = ['Pizza', 'Chinese', 'American', 'Italian', 'Mexican', 'Fast Food']

# Lists of each resteraunt for each cuisine style
pizza = ['Pizza Joes', 'Foxs', 'Pizza Pie', 'Pizza Plus', 'Vocellis', 'Dominoes', 'Tanis', 'Anna Maries']
chinese = ['China Gourmet', 'China One', 'China Palace']
american = ['Monroe Hotel', 'Rachels Roadhouse', 'Chop Shop', 'Burger Hut', 'Texas Roadhouse', 'Upper Crust', 'Cannella Cafe', 'Hoagie Shop', 'Chilis', 'Applebees']
italian = ['Villa Grande', 'Mama Rosas']
mexican = ['Rey Azteca', 'Compadres']
fastfood = ['Mcdonalds', 'Arbys', 'Wendys', 'Burger King', 'Subway', 'KFC', 'Dairy Queen', 'Taco Bell']

# Give the user some context.
print("\nPlease make a selection:")

# Set an initial value for choice other than the value for 'quit'.
choice = ''

import random

# Start a loop that runs until the user enters the value for 'quit'.
while choice != 'q':
    # Give all the choices in a series of print statements.
    print("\n[1] Pizza")
    print("[2] Chinese")
    print("[3] American")
    print("[4] Italian")
    print("[5] Mexican")
    print("[6] Fast food")
    print("[q] Enter q to quit.")
    
    # Ask for the user's choice.
    choice = input("\nWhat style would you like? ")
    
    # Respond to the user's choice.
    
    if choice == 'q':
        print('Goodbye')
        break
    if choice == '1':
        print("We're having", random.choice(pizza), "for lunch.")
        break
    elif choice =='2' :
        print("We're having", random.choice(chinese), "for lunch.")
        break
    elif choice == '3' :
        print("We're having", random.choice(american), "for lunch.")
        break
    elif choice == '4' :
        print("We're having", random.choice(italian), "for lunch.")
        break
    elif choice == '5' :
        print("We're having", random.choice(mexican), "for lunch.")
        break
    elif choice == '6' :
        print("We're having", random.choice(fastfood), "for lunch.")
        break
    else:
        print('Invalid Selection. Try again: ')

