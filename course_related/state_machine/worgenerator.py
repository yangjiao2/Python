# Yang Jiao, Lab 1
# Anita Marie Gilbert, Lab 1
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import goody
import prompt
import random
def read_corpus(order, openfile):
    '''
     has an order statistic parameter and and open (file) parameter; 
     it returns the dict representing the corpus of words in a file (mine is 9 lines).
    '''
    dict1 = dict()
    filelist = (openfile)
    old = []
    my=goody.read_file_values(filelist)

    for i in range(order):
        old.append(next(my))
    while True:
        try:
            next_one = next(my)        
            dict1.setdefault(tuple(old), set()).add(next_one)
            old.append(next_one)
            old.pop(0)
        except:

#             print (dict1)  
            return dict1
   

    
def print_corpus(dict1):
    '''
     has a dict parameter (representing the corpus); it returns nothing, 
     but it prints the corpus in the appropriate form followed the min and max value list lengths (mine is 8 lines).
    '''
    print ('Corpus')
    for i in sorted(dict1):    
        print ('\t' + str(i) + ' can be followed by any of ' + str(dict1[i]))
    minimum = min([len(lst) for lst in dict1.values()])
    maximum = max([len(lst) for lst in dict1.values()])
    print ('min/max = ' + str(minimum) +  '/' + str( maximum))
    
    
def produce_text(dict1, lst, num):
    '''
     has a dict parameter (representing the corpus), a list parameter 
     (representing the starting words), and an int count parameter 
     (representing the number of additional words to generate); 
     it returns a list that contains the the staring words followed by the generated words. 
     Hint: use two lists (list[str]) both starting out with these starting words words. 
     The first will always contain the current n words (to be coverted to a tuple and 
     used as a key in the dict); the second will contain all the generated words. 
     Generate a random next word from the dict using the choice function in the random modulesb: 
     add it to both lists; then, drop the first word from the first list, so it remains a list of length n; 
     repeat until you have generated the required number of words. 
     Warning: you might have to stop prematurely if you generate the last n words in the text, 
     and if these words occur nowhere else. 
     That is because in this case, there is no random word to generate following them; 
     in this case append a None to the end of the list of words and immediately return that list (mine is 11 lines). 
     A slightly more elegant solution in Python uses only one list, 
     copying the last order-statistic values of it into a tuple when needed for a key to the dictionary 
     (e.g., l[-os:]; mine using this approach is 9 lines).
    '''
    text = [i for i in lst]
    while len(text) <= num + len(lst) - 1:
        r = random.randrange(len(dict1[tuple(lst)]))
        
        text.append(list(dict1[tuple(lst)])[r])
        lst.append(list(dict1[tuple(lst)])[r])
        lst.pop(0)
    return text
    
def final_script():
    ''' a script at the bottom of this module that calls these functions to solve the problem. (mine is 8 lines). 
    '''
    order_stat = prompt.for_int('Enter order statistic', default=None, is_legal=(lambda x : True), error_message='It is not an integer.s')
    dictionary = read_corpus(order_stat,goody.safe_open('Enter file to process', 'r', 'No file avail. Try again.',default=None))
    print_corpus(dictionary)
    print ('Enter ' + str(order_stat) + ' words to start with')
    starting_words = []
    for i in range(order_stat):
        starting_words.append(prompt.for_string('Enter word ' + str(i+1) , default=None, is_legal=(lambda x : True), error_message=''))
    number = prompt.for_int('Enter # of words to generate', default=None, is_legal=(lambda x : True), error_message='an int, but not a legal value')
    print ('Random text = ' + str(produce_text(dictionary, starting_words, number)))
    
if __name__ == '__main__':
    final_script()
    