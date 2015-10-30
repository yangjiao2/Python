# Yang Jiao, Lab 1
# Anita Marie Gilbert, Lab 1
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import prompt
import goody


def read_graph():
    '''read_graph has an open (file) parameter; it returns the dict representing the graph'''
    
    filelist = (goody.safe_open('Enter file with graph','r','File does not exist. Please try again.',default=None)).readlines()
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
    
    k = prompt.for_string('Enter starting node, or "'"quit"'" to exit', default=None, is_legal=(lambda x: x in init_list), error_message='Char not in the list of graph source nodes.')

    while k != 'quit':
        reached_set = set()
        lst = [k]
#         lst.extend(list(dictionary[k]))
        while len(lst) > 0:
            if lst[0] in list(dictionary.keys()):
                for items in dictionary[lst[0]]:
                    if items not in lst and items not in reached_set and items in list(dictionary.keys()):
                        lst.append(items)
#                     elif items not in lst and items not in reached_set and items not in list(dictionary.keys()):
                    reached_set.add(items)
                reached_set.add(lst.pop(0))
        
        print("From " +k+ " the reachable nodes are:" + str(reached_set) + '\n')
        k = prompt.for_string('Enter starting node, or "'"quit"'" to exit', default=None, is_legal=(lambda x: x in init_list + ['quit']), error_message='Char not in the list of graph source nodes.')

if __name__ == '__main__':
    graph = read_graph()
    print_graph(graph)
    reachable(graph)