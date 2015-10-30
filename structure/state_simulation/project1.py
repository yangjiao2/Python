# Yang Jiao, Lab 1
# Anita Marie Gilbert, Lab 1
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import prompt
import goody
#Write a script that prompts the user to enter the name of a file representing a graph.

def build_dict(dictionary):
    # dic[key] = value
    pass
def read_graph():
    '''read_graph has an open (file) parameter; it returns the dict representing the graph'''
    
    filelist = (goody.safe_open('Enter file with graph','r','error_message',default=None)).readlines()
    raw_dic = {}
    for item in filelist:
        if item[0] in list(raw_dic.keys()):
            raw_dic[item[0] ].add(item[2])
        else:
            raw_dic[item[0] ] = ({item[2]})
    return (raw_dic)

def print_graph(dictionary):
    '''print_graph has a dict parameter (representing the graph); it returns nothing, but it prints the graph in the appropriate form '''
    print('Graph: source -> {destination} edges')
    for key, value in dictionary.items(): 
        print("{} -> {}".format(key, value))
        
def reachable(dictionary):
    '''reachable has a dict parameter (representing the graph) and a str start node in the graph 
    (technically a key in the dict; it returns a set of all the nodes reachable from it by following edges in the graph
    '''
    init_list = list(dictionary.keys())
    init_list.sort()
    
    k = prompt.for_char('Enter starting node', default=None, legal=str(init_list), error_message='Please enter one char in the range (if specified)')

    while k != 'quit':
        reached_set = set()
        lst = [k]
        lst.extend(list(dictionary[k]))
    #     a = lst[0]
        while len(lst) > 0 and lst[0] not in reached_set :
    #         popthing = lst.pop(0)
            
            for items in dictionary[lst[0]]:
                if items not in lst and items in list(dictionary.keys()):
                    lst.append(items)
                elif items not in list(dictionary.keys()):
                    reached_set.add(items)
 
                reached_set.add(lst.pop(0))
        
        print("From " +k+ " the reachable nodes are:" + str(reached_set) + '\n')
        k = prompt.for_char('Enter starting node', default=None, legal=str(init_list), error_message='Please enter one char in the range (if specified)')

# print_graph(read_graph())
reachable(read_graph())
#Read the information in the file, storing the graph in a dictionary.
#Print the graph.
#Repeatedly prompt the user for a starting node in the graph, and compute and print all the nodes that are reachable from it by following edges in the graph