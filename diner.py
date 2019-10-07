# Dinner Bottega Diner Have a Main Menu, and a Sides Menu You get one entree and two
# side choices at regular cost.

# *show them the entire menu (print out)
# *User selects an entree.
# *“Waitress” makes a comment based on their selection
# *comment can either be a comparison of the two items, or random comment pulled from
# a comment vault.

# *Tell them the price

# *repeat the above options for side choices (suggestion and a price, don’t repeat
# chef suggestion)

# *total up the cost BONUS Have a breakfast, lunch and dinner menu. Breakfast has
# different items, lunch and dinner have the same items but are different prices.

# BONUS: Allow for item *customization (how items are prepared, decide additional
# cost implications) EXTRA BONUS: 3D print out actual food and eat it.

# Opening Script
# Display Menu
# Pick item by name or id
#    > allow customization
# Play comment based on item's tag
# Loop back through until the user is finished
#  Iterate through Order List
#  Display total
#  Offer tip

from os import system, name
import random
import copy

diner_cook_options = ["Rare","Medium","Medium Well","Well Done"]
diner_burger_adds = ["Pepper Jack Cheese","Cheddar Cheese","Bacon"]
diner_burger_adds_cost = 0.50
diner_salad_dressings = ["Ranch","Lite Ranch","Thousand Island","Italian","Vinegarette"]

order_list = []

class Menu_Item:

    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    
    def list_addons(self, list):
        if len(list) == 1:
            return list[0].lower()
        elif len(list) == 2:
            return list[0].lower() + " and " + list[1].lower()
        elif len(list) > 1:
            addon_string = ""
            for item in list[:-1]:
                addon_string = str(item).lower() + ", " + addon_string
            addon_string = addon_string + "and " + str(list[-1]).lower()
            return addon_string

    def add_order(self):
        return
    
    def print_order(self):
        return f"\t${self.price:.2f} | {self.name}"


class Burger(Menu_Item):

    def __init__(self, name, price):
        self.toppings = []
        self.topping_options = diner_burger_adds
        self.cook = None
        self.cook_options = diner_cook_options
        super().__init__(name, price)
    

    def print_order(self):
        if self.cook and self.toppings:
            return f"\t${self.price:.2f} | {self.name} --> Cooked {self.cook.lower()} with {self.list_addons(self.toppings)} on top."
        elif self.cook:
            return f"\t${self.price:.2f} | {self.name} --> Cooked {self.cook.lower()}."
        elif self.toppings:
            return f"\t${self.price:.2f} | {self.name} --> With {self.list_addons(self.toppings)} on top."
        else:
            return f"\t${self.price:.2f} | {self.name} --> Plain"


    def add_order(self):

        print(str(self.cook_options).strip("[]"))
        cook_input = input("Any special cooking instructions? Type in any of the above options or just press ENTER to skip:  ")

        if cook_input in self.cook_options:
            self.cook = cook_input.title()
            print(f"Okay, the {self.name} will be cooked {self.cook.lower()}.")

        print(str(self.topping_options).strip("[]"))
        topping_input = input(f"Any add-ons for ${diner_burger_adds_cost:.2f}? Enter the toppings one at a time, or just press ENTER with no input to finish:  ")

        while True:
            if topping_input.title() in self.topping_options and topping_input.title() not in self.toppings:
                self.price += 0.50
                self.toppings.append(topping_input.title())
                topping_input = input("Would you like another topping? Otherwise, press ENTER with no input: ")
            elif topping_input == "":
                break
            else:
                topping_input = input("Invalid input, please try again: ")


class Salad(Menu_Item):
    def __init__(self, name, price):
        self.dressing = None
        self.dressing_options = diner_salad_dressings
        super().__init__(name, price)


class Side(Menu_Item):
    print


class Drink(Menu_Item):
    print


menu_list = [
    # item name, price, menu class, 
    Burger("Classic Burger", 11.75),
    Burger("Big Texas Burger", 13.75),
    Burger("Ruby on Rails Burger", 12.75),
    Salad("Pipenv Salad", 11.75),
    Salad("Python Cobb Salad", 11.75),
    Salad("J-Vue Salad", 11.75),
    Side("Java Fries", 4.00),
    Side("Javascript Rings", 3.00),
    Side("HTML Tots", 3.75),
    Drink("Repl.it Shake", 5.00),
    Drink("Fizzbuzz Soda", 4.00)
]


bark_dict = {
    "Burger" : ["That burger is equally mouth watering and delicious. I hope you enjoy it.",
    "That burger is one of our most popular specials.",
    "You'll be happy to know that all of our burgers are served on gluten-free buns!"],

    "Salad" : ["It's a great option if you're wanting to watch your calories!",
    "That salad is a favorite with my family. Good choice!",
    "All of our salads are made with farm fresh greens. I know you'll enjoy it!"],

    "Drink" : ["I'll get it out to ice cold just as soon as I'm done taking your order.",
    "Great choice if you wanna beat the heat!"],

    "Side" : ["I can get you a separate container for your side, if you'd like to take it to go."]
}

def screen_clear():
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')


def bark(bark_class):
    if bark_class in bark_dict.keys():
        rand_range = len(list(bark_dict[bark_class]))
        bark_string = random.randint(0,rand_range-1)
        return bark_dict[bark_class][bark_string]


def get_total():
    customer_total = 0
    for item in order_list:
        customer_total += item.price
    return customer_total


def display_menu():
    screen_clear()
    def sub_menu(menu_type):
        print(f"NO.\tPRICE\tITEM")
        for item in menu_list:
            if isinstance(item, menu_type):
                print(f"{menu_list.index(item)}\t${item.price:.2f}\t{item.name}")

    print("\n <<======== SPECIALS MENU ==============================>> \n")
    sub_menu(Burger)
    print(f"\n\t {{Add for ${diner_burger_adds_cost:.2f} each: }}")
    print(f'\t   > {str(diner_burger_adds).strip("[]")}\n')
    sub_menu(Salad)
    print(f'\n\t {{Dressing Options}}: ')
    print(f'\t   > {str(diner_salad_dressings).strip("[]")}')
    print("\n\n <<========  SIDES  MENU  ==============================>> \n")
    sub_menu(Side)
    print("\n\n <<========  DRINKS MENU  ==============================>> \n")
    sub_menu(Drink)
    print("\n\n YOUR CURRENT ORDER:  ")
    order_number = 1
    for item in order_list:
        print(f"{item.print_order()} - (Item #{order_number})")
        order_number += 1
    print(f"\t CURRENT TOTAL: ${get_total():.2f}")


display_menu()

order_input = input("\nTo order: please enter the item No. to the left \nof the item, and then press ENTER:  ")

while True:
    if order_input.isdigit():
        order_input = int(order_input)
        input(f"The {menu_list[order_input].name}? {bark(menu_list[order_input].__class__.__name__)}\n")
        #### WAITER COMMENTS GO HERE ^ ^ ^
        order_list.append(copy.deepcopy(menu_list[order_input]))
        order_list[-1].add_order()
        display_menu()
        order_input = input("\nIf you'd like to order something else, type the item No. to the left \nof the item, and then press ENTER:  ")
    elif order_input == "":
        break
    else:
        order_input = input("Invalid input, please try again:  ")

input("We'll get that order started for you right way. Press ENTER to pay: ")

tip = input(f"""\nYour total total is going to be ${get_total()}.
Would you like to add a tip?\n
[10% - ${round(get_total()*.10,2):.2f} | 15% - ${round(get_total()*.15,2):.2f} | 18% - ${round(get_total()*.18,2):.2f}]
\nPlease enter the percentage number 1 - 100 or just press ENTER:  """)

while True:
    if tip.isdigit():
        tip = int(tip)
        total_due = round(get_total() + (tip * .01 * get_total()),2)
        break
    elif tip == "":
        total_due = get_total()
        break
    else:
        tip = input("Invalid input, please try again: ")

print(f"\n Your total today is ${total_due:.2f}")
input("We'll have your order ready in 10 minutes. Press ENTER to exit:")