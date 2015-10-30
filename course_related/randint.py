# Jonathan Shokoor 54287589,  Yang Jiao 82222745. ICS 31 Lab sec 6.  Lab asst 6.

#  Rules of the game Craps:
#
# Roll two dice:
#   If you roll 7 or 11, "natural":  you win.
#               2, 3, or 12, "craps":  you lose.
#               anything else, that number is "your point"
#   Subsequent rolls:
#           Roll your "point":  you win.
#                7, "crap out":  you lose.
#                anything else, roll again.

print ('(c)')
from random import randint

def roll() -> int:
    ''' Return a roll of two dice, 2-12
    '''
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    return die1 + die2

number = 2000
print ('Suppose we want to roll', number, 'times')
    
def Count(num:int) -> list:
    '''count the list of dice result and return the total of each result in a list'''
    n = [0,0,0,0,0,0,0,0,0,0,0]
    for i in range(num):
        r = roll()
        n[r - 2] = n[r - 2] + 1
        
    return n

newList = Count(number)


def Star() ->str:
    star = []
    for i in range(len(newList)):

        star.append('*' * (int(newList[i] / sum(newList) * 100)))
    return star

def Distribution_str(num:int):
    '''take a list and print the diagram in string'''
    print ('-- Distribution of dice rolls --')
    for i in range(11):
        print (' {:2}:{:6} ({:5.2f}%)  {:10}'.format(i + 2, newList[i], newList[i]/ sum(newList) * 100, Star()[i]))
    print('-----------------\nTotal   ', number,' rolls')
    
Distribution_str(number)
        

print ('(d) \nassert (Caesar_decrypt(\'Vw amkzmb!\', 8) == \'no secret!\')')

ALPHABET = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
alphabet = ALPHABET.lower()

def Lowercase(string:str) -> str:
    '''takes a string and returns the str with all lower case alphabet'''
    translation = str.maketrans(ALPHABET, alphabet)
    newStr = (string.translate(translation))
    return newStr     

def Rotate(string: str, num:int) -> str:
    '''takes a number and produces a "rotated" alphabet with the specified number of characters taken off the front and added on to the end of the string. '''
    rotatedStr = ''
    if num >= 26:
        num = num % 26
    for i in range(len(string)):
        if string[i] not in list(alphabet):
            rotatedStr = rotatedStr + string[i] 
        elif (alphabet.find(string[i]) + num) >= 26:
            rotatedStr = rotatedStr + alphabet[alphabet.find(string[i]) + num - 26]
        else:
            rotatedStr = rotatedStr + alphabet[alphabet.find(string[i]) + num]
    return rotatedStr

def Caesar_encrypt(plain: str, num:int) -> str:
    ''' takes a string containing the plaintext for encryption,
    returns the ciphertext '''
    result = Rotate(Lowercase(plain), num)
    return result

def Caesar_decrypt(cipher: str, num: int) -> str:
    ''' takes a string containing the ciphertext for decryption,
     returns the plaintext '''
    result = Rotate(Lowercase(cipher), -num)
    return result

assert (Caesar_decrypt(Caesar_encrypt('buzz!', 3), 3) == 'buzz!')
assert (Rotate('zz?',1) == 'aa?')
assert (Caesar_decrypt('Vw amkzmb!', 8) == 'no secret!')
assert (Caesar_encrypt("cat", 29) ==  Caesar_encrypt("cat", 3))

print('\n(e)')
print ('(e.1)')

S = [ "Four score and seven years ago, our fathers brought forth on",
      "this continent a new nation, conceived in liberty and dedicated",
      "to the proposition that all men are created equal.  Now we are",
      "   engaged in a great 		civil war, testing whether that nation, or any",
      "nation so conceived and so dedicated, can long endure.        "]

def print_line_numbers(s:list) -> str:
    ''' takes a list of strings and prints each string preceded by a line number'''
    for i in range(len(S)):
        print (('{:'+str(len(str(len(S))))+'}:  {:1}').format(i + 1, S[i]))

print_line_numbers(S)

print ('\n(e.2)')

def stats(s: list):
    '''
    total lines
    empty lines
    total characters
    '''
    '''takes a list of strings and prints statistics'''
    characters = 0
    empty_lines = 0
    for i in range(len(s)):
        if s[i].strip() == '':
            empty_lines += 1
        characters += len(s[i])
    print ('{:6}   line in the list\n{:6}   empty lines\n{:8.1f} average characters per line\n{:8.1f} average characters per non-empty line'.format(len(S), empty_lines, characters / (len(S)), characters / (len(S) - empty_lines)))
    
stats(S)


print ('(e.3) ')
def  list_of_words(s:list)->list:
    ''' takes a list of strings as above and returns a list of individual words with all white space and punctuation removed '''
    word_list = []
    for x in S:
        x = x.split()
        for y in x:
            word_list.append(y.strip(' ., '))
    return word_list

print(list_of_words(S))   
assert(list_of_words(S) == ['Four', 'score', 'and', 'seven', 'years', 'ago', 'our', 'fathers', 'brought', 'forth', 'on', 'this', 'continent', 'a', 'new', 'nation', 'conceived', 'in', 'liberty', 'and', 'dedicated', 'to', 'the', 'proposition', 'that', 'all', 'men', 'are', 'created', 'equal', 'Now', 'we', 'are', 'engaged', 'in', 'a', 'great', 'civil', 'war', 'testing', 'whether', 'that', 'nation', 'or', 'any', 'nation', 'so', 'conceived', 'and', 'so', 'dedicated', 'can', 'long', 'endure'])


