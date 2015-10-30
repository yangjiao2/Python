# Anita Marie Gilbert 00871067, Yang Jiao 82222745. ICS 31 Lab sec 6.  Lab asst 5.
# c.1
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
Dish = namedtuple('Dish', 'name price calories')
r1 = Restaurant('Thai Dishes', 'Thai', '334-4433', [Dish('Mee Krob', 12.50, 500),
                                                    Dish('Larb Gai', 11.00, 450)])
r2 = Restaurant('Taillevent', 'French', '01-44-95-15-01', 
				[Dish('Homard Bleu', 45.00, 750),
				 Dish('Tournedos Rossini', 65.00, 950),
				 Dish("Selle d'Agneau", 60.00, 850)])
r3 = Restaurant('Pascal', 'French', '940-752-0107',
                [Dish('escargots', 12.95,250),
                 Dish('poached salmon', 18.50, 550),
                 Dish('rack of lamb', 24.00, 850),
                 Dish('marjolaine cake', 8.50, 950)])
DL = [r1, r2, r3]

DL2= [Restaurant('Thai Dishes', 'Thai', '334-4433', [Dish('Mee Krob', 12.50, 500),
                                                    Dish('Larb Gai', 11.00, 450)]),Restaurant('Taillevent', 'French', '01-44-95-15-01', 
				[Dish('Homard Bleu', 45.00, 750),
				 Dish('Tournedos Rossini', 65.00, 950),
				 Dish("Selle d'Agneau", 60.00, 850)]),Restaurant('Pascal', 'French', '940-752-0107',
                [Dish('escargots', 12.95,250),
                 Dish('poached salmon', 18.50, 550),
                 Dish('rack of lamb', 24.00, 850),
                 Dish('marjolaine cake', 8.50, 950)])]
print ("---------------------- c.2 \n assert (Restaurant_first_dish_name(r1) == 'Mee Krob')\n")
def Restaurant_first_dish_name(r: Restaurant) -> str:
    '''that takes a Restaurant as its argument and returns the name of the first dish on the restaurant's menu'''
    return r.menu[0].name
assert (Restaurant_first_dish_name(r1) == 'Mee Krob')


print ("---------------------- c.3 \nassert (Restaurant_is_cheap(r1, 12.00))\n")
def Restaurant_is_cheap(r:Restaurant, num:int) -> bool:
    '''that takes two arguments, a Restaurant and a number,
    and returns True if the average price of the Restaurant's menu is less than or equal to the number'''
    summ = 0
    for i in r.menu:
        summ = summ + i.price
    return (summ / (len(r.menu)) <= num) 
assert (Restaurant_is_cheap(r1, 12.00))


print ("---------------------- c.4 \nassert (Collection_raise_prices(DL) == [Dish(name='Mee Krob', price=15.0, calories=500), Dish(name='Larb Gai', price=13.5, calories=450)], [Dish(name='Homard Bleu', price=47.5, calories=750), Dish(name='Tournedos Rossini', price=67.5, calories=950), Dish(name='Selle d\'Agneau', price=62.5, calories=850)], [Dish(name='escargots', price=15.45, calories=250), Dish(name='poached salmon', price=21.0, calories=550), Dish(name='rack of lamb', price=26.5, calories=850), Dish(name='marjolaine cake', price=11.0, calories=950)]\n \nassert (Collection_change_prices(DL, 100) == [Dish(name='Mee Krob', price=30.0, calories=500), Dish(name='Larb Gai', price=27.0, calories=450)], [Dish(name='Homard Bleu', price=95.0, calories=750), Dish(name='Tournedos Rossini', price=135.0, calories=950), Dish(name='Selle d\'Agneau', price=125.0, calories=850)], [Dish(name='escargots', price=30.9, calories=250), Dish(name='poached salmon', price=42.0, calories=550), Dish(name='rack of lamb', price=53.0, calories=850), Dish(name='marjolaine cake', price=22.0, calories=950)] \n")
def Collection_raise_prices(C:list) -> list:
    ''' takes a Collection and returns the Collection with the price of every dish at every restaurant raised by $2.50'''
    newList = []
    for i in C:
        newList.append(Restaurant_raise_prices(i))
    return newList

def Restaurant_raise_prices(r:Restaurant) -> Restaurant:
    '''that takes a restaurant and returns that restaurant with all its prices raised by $2.50'''
    return Menu_raise_prices(r.menu)

def Menu_raise_prices(Menu:list) ->list:
    '''which takes a Menu, applies a function like Dish_raise_250'''
    for i in range(len(Menu)):
        Menu[i] = Dish_raise_250(Menu[i])
    return Menu
    
def Dish_raise_250(dish:tuple) -> Dish:
    '''take a Dish on the Menu, and returns the modified dish'''   
    return dish._replace(price = dish.price + 2.50)

assert (Collection_raise_prices(DL) == [Dish(name='Mee Krob', price=15.0, calories=500), Dish(name='Larb Gai', price=13.5, calories=450)], [Dish(name='Homard Bleu', price=47.5, calories=750), Dish(name='Tournedos Rossini', price=67.5, calories=950), Dish(name="Selle d'Agneau", price=62.5, calories=850)], [Dish(name='escargots', price=15.45, calories=250), Dish(name='poached salmon', price=21.0, calories=550), Dish(name='rack of lamb', price=26.5, calories=850), Dish(name='marjolaine cake', price=11.0, calories=950)])


def Collection_change_prices(C:list, percentage: int) -> list:
    ''' takes a Collection and returns the Collection with the price of every dish at every restaurant raised by $2.50'''
    newList = []
    for i in C:
        newList.append(Restaurant_change_prices(i, percentage))
    return newList

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

assert (Collection_change_prices(DL2, 100) == [Dish(name='Mee Krob', price=30.0, calories=500), Dish(name='Larb Gai', price=27.0, calories=450)], [Dish(name='Homard Bleu', price=95.0, calories=750), Dish(name='Tournedos Rossini', price=135.0, calories=950), Dish(name='Selle d\'Agneau', price=125.0, calories=850)], [Dish(name='escargots', price=30.9, calories=250), Dish(name='poached salmon', price=42.0, calories=550), Dish(name='rack of lamb', price=53.0, calories=850), Dish(name='marjolaine cake', price=22.0, calories=950)])
print ("--------------------- c.5 \nassert (Collection_select_cheap(DL, 15) == [Restaurant(name='Thai Dishes', cuisine='Thai', phone='334-4433', menu=[Dish(name='Mee Krob', price=15.0, calories=500),Dish(name='Larb Gai', price=13.5, calories=450)])])")
def Collection_select_cheap(C:list, num:int) ->list:
    '''that takes a Collection and a number and returns a list of all the Restaurants in the collection
    whose average price is less than or equal to that number'''
    newList =[]
    for i in C:
        if Restaurant_is_cheap(i, num):
            newList.append(i)
    return newList
assert (Collection_select_cheap(DL, 15) == [Restaurant(name='Thai Dishes', cuisine='Thai', phone='334-4433',
                                                       menu=[Dish(name='Mee Krob', price=15.0, calories=500),
                                                         Dish(name='Larb Gai', price=13.5, calories=450)])])
print ("-------------e) 4.13\nassert (s[1:3] == 'bc')\nassert (s[:14] == 'abcdefghijklmn')\nassert (s[14:] == 'opqrstuvwxyz')\nassert (s[1:-1] == 'bcdefghijklmnopqrstuvwxy')")

s = 'abcdefghijklmnopqrstuvwxyz'
assert (s[1:3] == 'bc')
assert (s[:14] == 'abcdefghijklmn')
assert (s[14:] == 'opqrstuvwxyz')
assert (s[1:-1] == 'bcdefghijklmnopqrstuvwxy')

print ("-------------e) 4.14\n")
log = "128.0.0.1 - - [12/Feb/2011:10:31:08 -0600] \"GET /docs/test.txt HTTP/1.0"
address = log[0:15]
print ('(b)', address)

front = log.index('[')
end = log.index(']')
print ('(c)', log[front:end + 1])

print ("-------------e) 4.19\n")

first = 'Marlena'
last = 'Sigel'
middle = 'Mae'
print ('(a)', last, ", ", first, " ", middle, sep="")
print ('(b)', last, ", ", first, " ", middle[0], ".", sep="")
print ('(c)', first, " ", middle[0],". ", last, sep="")
print ('(d)', first[0],". ",middle[0],". ", last, sep="")

print ("-------------e) 4.23\n")

def average()->int:
    ''' user enters a sentence and code returns the average length of a word in the sentence'''
    sentence = input("Please enter a clever sentence:")
    number_of_word = sentence.count(" ")
    print ((len(sentence) - number_of_word)/ (number_of_word + 1))
average()

print ("-------------e) 4.25\nassert (letter_count('coooool', 'ioilc')== [Count(letter='i', number=0), Count(letter='o', number=5), Count(letter='i', number=0), Count(letter='o', number=5), Count(letter='p', number=0)]")

Count = namedtuple("Count", "letter number")
def letter_count(str1:str, str2:str) -> tuple:
    '''that has two strings as parameters.
    The function returns the counts of certain letters in the first parameter;
    the second parameter is a string that specifies which letters to count.'''
    c =[]
    for i in range(len(str2)):
        c.append(Count(str2[i], str1.count(str2[i])))
    return c
assert (letter_count('coooool', 'ioiop')== [Count(letter='i', number=0), Count(letter='o', number=5), Count(letter='i', number=0), Count(letter='o', number=5), Count(letter='p', number=0)])
