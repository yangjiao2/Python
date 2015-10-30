# RESTAURANT COLLECTION PROGRAM
# ICS 31, UCI, David G. Kay, Fall 2012

# Implement Restaurant as a namedtuple, collection as a list

##### MAIN PROGRAM (CONTROLLER)

def restaurants():  # nothing -> interaction
    """ Main program
    """
    print("Welcome to the restaurants program!")
    our_rests = Collection_new()
    our_rests = handle_commands(our_rests)
    print("\nThank you.  Good-bye.")

MENU = """
Restaurant Collection Program --- Choose one
 a:  Add a new restaurant to the collection
 c:  Change prices for the dishes served
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 p:  Print all the restaurants
 l:  Select restaurant with average price of dishes below a certain price
 q:  Quit
"""

def handle_commands(C: list) -> list:
    """ Display menu, accept and process commands.
    """
    while True:
        response = input(MENU)
        if response=="q":
            return C
        elif response=='a':
            r = Restaurant_get_info()
            C = Collection_add(C, r)
        elif response == 'c':
            percentage = int(input("Please input the percentage change: "))
            C = Collection_change_prices(C, percentage)
        elif response=='r':
            n = input("Please enter the name of the restaurant to remove:  ")
            C = Collection_remove_by_name(C, n)
        elif response=='p':
            print(Collection_str(C))
        elif response == 'l':
            num = eval(input('Please input a certain price:  '))
            print (Collection_select_cheap(C, num))
        elif response=='s':
            n = input("Please enter the name of the restaurant to search for:  ")
            for r in Collection_search_by_name(C, n):
                print(Restaurant_str(r))
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")




##### Restaurant
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
Dish = namedtuple('Dish', 'name price calories')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', 'Escargots', 23.50)


def Restaurant_str(self: Restaurant) -> str:
    return (
        "Name:     " + self.name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        "Phone:    " + self.phone + "\n" +
        " -- Menu --\n" +
        Menu_str(self.menu) +
        "--------------------------------\n\n")

def Restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Restaurant(
        input("Please enter the restaurant's name:  "),
        input("Please enter the kind of food served:  "),
        input("Please enter the phone number:  "),
        Menu_enter())


#### COLLECTION
# A collection is a list of restaurants

def Collection_new() -> list:
    ''' Return a new, empty collection
    '''
    return [ ]

def Collection_str(C: list) -> str:
    ''' Return a string representing the collection
    '''
    s = ""
    for r in C:
        s = s + Restaurant_str(r)
    return s

def Collection_search_by_name(C: list, name: str) -> list:
    """ Return list of Restaurants in input list whose name matches input string.
    """
    result = [ ]
    for r in C:
        if r.name == name:
            result.append(r)
    return result
    # alternative (using a list comprehension):
    # return [r for r in C if r.name == name]

def Collection_add(C: list, R: Restaurant) -> list:
    """ Return list of Restaurants with input Restaurant added at end.
    """
    C.append(R)
    return C

def Collection_remove_by_name(C: list, name: str) -> list:
    """ Given name, remove all Restaurants with that name from collection.
    """
    result = [ ]
    for r in C:
        if r.name != name:
            result.append(r)
    return result
    #    Alternative:
    #    return [r for r in self.rests if r.name != name]

#### MENU

def Dish_get_info() -> Dish:
    """ Prompt user for fields of Dishes; create and return.
    """
    return Dish(
        input("Please enter the dish's name:  "),
        float(input("Please enter the price of that dish:  ")),
        input("Please enter the calories:  "))

def Menu_enter() -> list:
    '''function that repeatedly asks whether the user wants to add a Dish'''

    Menu = []
    while True:
        choice = input("Do you want to add a Dish? Please enter yes or no." )
        if choice == 'yes' or choice == 'Yes' or choice == 'YES':
             Menu.append(Dish_get_info())
        elif choice == 'no' or choice == 'No' or choice == 'NO':
             return Menu
         
   

def Menu_str(menu: list) -> str:
    '''create a display string for the menu of dishes'''
    dish_str = ""
    for i in menu:
        dish_str += Dish_str(i)
    return dish_str

def Dish_str(a_dish:tuple):
    '''takes a Dish and returns a string'''
    return a_dish.name + ' ($' + str(a_dish.price) + '): ' + str(a_dish.calories) + ' cal \n'

# change price

def Collection_change_prices(C:list, percentage: int) -> list:
    ''' takes a Collection and returns the Collection with the price of every dish at every restaurant raised by $2.50'''

    for i in C:
        i = Restaurant_change_prices(i, percentage)
    return C

def Restaurant_change_prices(r:Restaurant, percentage: int) -> Restaurant:
    '''that takes a restaurant and returns that restaurant with all its prices raised by $2.50'''
    return Menu_change_prices(r.menu, percentage)

def Menu_change_prices(Menu:list, percentage: int) ->list:
    '''which takes a Menu, applies a function like Dish_raise_250'''
    for i in range(len(Menu)):
        Menu[i] = Dish_change_prices(Menu[i], percentage)
    return Menu
    
def Dish_change_prices(dish:tuple, percentage: int) -> Dish:
    '''take a Dish on the Menu, and returns the modified dish'''
    return dish._replace(price = dish.price * (1 + 0.01 * percentage))
        
def Collection_select_cheap(C:list, num:int) ->list:
    '''that takes a Collection and a number and returns a list of all the Restaurants in the collection
    whose average price is less than or equal to that number'''
    newList =''
    for i in C:
        if Restaurant_is_cheap(i, num):
            newList += Restaurant_str(i)
    return newList

def Restaurant_is_cheap(r:Restaurant, num:int) -> bool:
    '''that takes two arguments, a Restaurant and a number,
    and returns True if the average price of the Restaurant's menu is less than or equal to the number'''
    summ = 0
    for i in r.menu:
        summ = summ + i.price
    return (summ / (len(r.menu)) <= num) 
restaurants()