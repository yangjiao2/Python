# Son Tu 82584074 and Yang Jiao 82222745  ICS 31 Lab sec 6.  Lab asst 7.

# c)  generate strings of the form "Lastname, Firstname" where the last name is randomly chosen from the surnames list and the first name is randomly chosen from either the female names list or the male names list. 

print ("c)")
from random import randint
femalelist, malelist, surlist = [], [], []
femalefile = open('femalenames.txt', 'r')
femaleread = femalefile.readlines()
malefile = open('malenames.txt', 'r')
maleread = malefile.readlines()
surfile = open('surnames.txt', 'r')
surread = surfile.readlines()

def random_names(integer:int)->list:
    '''takes an integer and returns a list of that many strings, 
    with each string a randomly generated name as described above'''
    result = []
    
    while integer > 0:
        result.append(generate_single_random_name())
        integer -= 1
    return result

def generate_single_random_name() -> str:
    '''generate a single random name—a random surname, a random choice of male or female, and a random first name'''
    result = ''
    female_or_male = 0
    female_or_male = randint(1,2)
    if female_or_male == 1:
        readfile = maleread
    else:
        readfile = femaleread
    result = (single_random_name(surread) + ", " + single_random_name(readfile))
    return result

def single_random_name(lst: list) ->str:
    '''takes one of the three name lists as a parameter and 
    returns a name chosen at random from that list'''

    index = 0
    index = randint (1, len(lst))
    namelist = lst[index].split("\t")
    name = namelist[0].capitalize()
    return name

print ("Let's print eight random names if that's fine with you! \n", random_names(8))

print ("But we want to try to make the name chosen by their popularity if possible.")

# select name based on their popularity
def single_random_name_based_on_popularity(lst: list) -> str:
    '''takes one of the three name lists as a parameter and 
        returns a name chosen based on popularity from that list'''    
    copiedlist = lst

    name_list_repeated_by_their_popularity = []
    for a_name in copiedlist:
        times = int(float(a_name.split("\t")[1]) * 1000)
        name = str(a_name.split("\t")[0])

        name_list_repeated_by_their_popularity.extend([name] * times)
        # print (name_list_repeated_by_their_popularity)
        # it print ['MARY', 'MARY', 'MARY',....'BARBARA']
    index = 0
    index = randint(1, len(name_list_repeated_by_their_popularity))
    name = name_list_repeated_by_their_popularity[index].capitalize()

    return name   
        
# same thing from above with changed funcion header
def random_names_based_on_popularity(integer:int)->list:
    '''takes an integer and returns a list of that many strings, 
    with each string a randomly generated name '''
    result = []
    
    while integer > 0:
        result.append(generate_single_random_name_based_on_popularity())
        integer -= 1
    return result

def generate_single_random_name_based_on_popularity() -> str:
    '''generate a single random name—a random surname, a random choice of male or female, and a random first name'''
    result = ''
    female_or_male = 0
    female_or_male = randint(1,2)
    if female_or_male == 1:
        readfile = maleread
    else:
        readfile = femaleread
    result = (single_random_name_based_on_popularity(surread) + ", " + single_random_name_based_on_popularity(readfile))
    return result    

print ("Let's print eight names based on popularity if that's fine with you! \n", random_names_based_on_popularity(8))

# d) cryptanalysis without the key
print ("d) \nassert (Caesar_break(Caesar_encrypt('Hello my name is Y, thanks for helping me', 5)) == 'hello my name is y thanks for helping me')")
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
    string = string.lower()
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

def Caesar_decrypt(cipher: str, num: int) -> str:
    ''' takes a string containing the ciphertext for decryption,
     returns the plaintext '''
    result = Rotate(Lowercase(cipher), -num)
    return result

def Caesar_encrypt(plain: str, num:int) -> str:
    ''' takes a string containing the plaintext for encryption,
    returns the ciphertext '''
    result = Rotate(Lowercase(plain), num)
    return result

def Caesar_break(cipher:str) ->str:
    '''takes a ciphertext string (encrypted using a Caesar cipher),
    and returns the plaintext for that string, without having the key'''
    countingList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    key = 0

    infile = open('wordlist.txt', 'r')
    readfile = infile.read()
    wordList = []

    # add words from the dictionary
    for string in readfile.split("\n"):
        #add that word to a list
        wordList.append(Lowercase(string))

    #for each word in the cipher to break
##    sentence = cipher.split()

    #for each possible letter shift
    for i in range(26):
        #grab the shifted
        plausible = Rotate(cipher, i).split()

        #for each word in the shifted
        for word in plausible:
       
            #check to see if the rotated word is in the dictionary
            if word in wordList or str(word) + "'s" in wordList:
                #if in dictionary, do what?
                countingList[i] += 1
                

            

    for ii in range(25):
        if countingList[ii] > key:
            key = countingList[ii]
            result = Caesar_decrypt(cipher, -countingList.index(key))

    return result


assert (Caesar_break(Caesar_encrypt('Hello my name is Y, thanks for helping me', 5)) == "hello my name is y, thanks for helping me")
assert (Caesar_break(Caesar_encrypt('hello resPONDER', 6)) == "hello responder")
assert (Caesar_break(Caesar_encrypt('cat dog', 8))  == 'cat dog')
