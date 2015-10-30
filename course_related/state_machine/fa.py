# Yang Jiao, Lab 1
# Anita Marie Gilbert, Lab 1
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

#     Write a script that prompts the user to enter the name of a file representing a finite automaton: indicating its states and input->state transitions.
#     Read the information in the file, storing it in a dictionary.
#     Print the finite automaton.
#     Prompt the user for to enter the name of a file storing the start-state and inputs to process (each line in the file contains this combination).
#     Repeatedly process these lines computing the results of the finite automaton on each input, and then display the results.

import goody
def read_fa ():
    ''' has an open (file) parameter; 
    it returns the dict representing the finite automaton; 
    hint: I used splicing and the zip function to build the inner dicts. (mine is 6 lines).
    '''
    filelist = (goody.safe_open('Enter file with finite automaton', 'r', 'No file avail. Try again.',default=None)).readlines()


    inner_dict = dict()
    for line in filelist:
        raw_lst = line.strip().split(';')

        inner_dict.setdefault(raw_lst[0],dict(zip(raw_lst[1::2], raw_lst[2::2])))

    return(inner_dict)


def print_fa(dictionary):
    ''' has a dict parameter (representing the fa); 
    it returns nothing, but it prints the fa in the appropriate form (mine is 4 lines).
    '''
    print ('Finite Automaton')
    for outer_key in dictionary.keys():
        print("   " + outer_key + " transitions: " + str([i for i in zip(list(dictionary[outer_key].keys()), list(dictionary[outer_key].values()))]))
    
def process(dictionary, state, inputs):
    ''' has a dict parameter (representing the fa), 
    a str parameter (representing the start-state), 
    and a list parameter (representing a list of str inputs); 
    it returns a list that contains the start-state followed by tuples that 
    show the input and resulting state after each transition. 
    For the example shown above, process returns the following list.
    ['even', ('1', 'odd'), ('0', 'odd'), ('1', 'even'), ('1', 'odd'), ('0', 'odd'), ('1', 'even')]
    '''
    result = [state]
#     print("inputs", set(list[dictionary.values()][0]))
    for a_input in inputs:       
        for k,v in dictionary[state].items():
            if k[0] == a_input:
                state = (v)

            elif a_input not in set(result[0] for lst in dictionary.values() for result in lst):
                state = None
        result.append((a_input, state))
    return result


def interpret(process_lst):
    '''has a list parameter (the result produced by process; 
    it returns nothing, but it prints the results of processing a fa on an input. 
    See how it prints the list shown above in the output further above. 
    Also see the Sample Interaction below to see how it prints input errors 
    (in the last example) (mine is 9 lines).
    '''
    print ('\nStarting new simulation')
    print ('Start state = ' + process_lst[0])
    for tuples in process_lst[1:]:
        print ('Input = ' + tuples[0] + ';' +  (' new state = ' + str(tuples[1]) if tuples[1] != None else ' illegal input; terminated'))
    print ('Stop state = ' + str(process_lst[-1][1]))
            
def final_script():
    ''' at the bottom of this module that calls these functions to solve the problem. 
    Note that the script loops over the lines in the second file (mine is 7 lines).   
    '''
    fa = read_fa ()
    print_fa(fa)
    filelist = (goody.safe_open('Enter file with start-state and input', 'r', 'No file avail. Try again.',default=None)).readlines()
    for line in filelist:
        line_lst = line.strip().split(';')
        result = process(fa, line_lst[0], line_lst[1:])
        interpret(result)
        
if __name__ == '__main__':
    final_script()