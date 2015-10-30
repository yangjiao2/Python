# Yang Jiao, Lab 1
# Anita Marie Gilbert, Lab 1
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import goody
from collections import defaultdict
def read_ndfa():
    ''' has an open (file) parameter; 
    it returns the dict representing the non-deterministic finite automaton; 
    hint: I used splicing and the zip function to build the inner dicts, and 
    I called the setdefault function for the inner dict (alternatively I could have built them as defaultdicts: 
    see the standard collections module) (mine is 9 lines).
    '''
#     filelist = (goody.safe_open('Enter file with finite automaton', 'r', 'No file avail. Try again.',default=None)).readlines()
    filelist= open('ndfaendin01.txt', 'r').readlines()

    raw_dict = dict()
    for line in filelist:
        raw_lst = line.strip().split(';')
        inner_dict = dict()
        for i in range (1, int(len(raw_lst)), 2):
            inner_dict.setdefault(raw_lst[i], set()).add(raw_lst[i+1])

#                 inner_dict.setdefault(key, set()).add(value) 

#         inner_dict[key].add((value) for key in raw_lst[1::2] for value in raw_lst[2::2])

        raw_dict[raw_lst[0]] = inner_dict
    print (raw_dict)
    return raw_dict

def print_ndfa(dict1):
    ''' has a dict parameter (representing the ndfa); 
    it returns nothing, but it prints the ndfa in the appropriate form (mine is 4 lines).
    '''
    print ('Non-Deterministic Finite Automaton:')


    for outer_key in dict1.keys():       
        print("   " + outer_key + " transitions: " + str([i for i in zip(list(dict1[outer_key].keys()), list(dict1[outer_key].values()))]))






def process():
    ''' has a dict parameter (representing the ndfa), 
    a str parameter (representing the start-state), 
    and a list parameter (representing a list of str inputs); 
    it returns a list that contains the start-state followed by tuples 
    that show the input and resulting st of states after each transition. 
    For the example shown above, process returns the following list.
    '''

def illegal_input():
    '''
    Finally, if an input is illegal (is not the key in some transition for the current state), 
    just ignore it (mine is 11 lines).
    '''
def interpret():
    ''' has a list parameter (the result produced by process; 
    it returns nothing, but it prints the results of processing a ndfa on an input. 
    See how it prints the list shown above in the output further above (mine is 5 lines).
    '''
    
def final_script():
    '''Write a script at the bottom of this module that 
    calls these functions to solve the problem. 
    Note that the script loops over the lines in the second file (mine is 7 lines). 
    '''
dictionary = read_ndfa()
print_ndfa(dictionary)