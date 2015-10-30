# Yang Jiao, Lab 1
# Anita Marie Gilbert, Lab 1
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
import goody
#from collections import Counter
from operator import itemgetter

def ordering(dict3, boolean):
    return (sorted(dict3, key = (lambda t : t[1]), reverse=boolean))

            
def print_dict (title, dict1, f = None, boolean = False):
    '''print_dict has a str title, any kind of dict, a function(default None) and bool 
    (default False)as parameters and returns nothing; but it prints the title
    followed by the dictionary in the appropriate form and order (specified by the function and bool). 
    The function determines the ordering and the bool determines whether to reverse it: 
    like the key and reverse parameters used to sort in Python. 
    This function is used to print both the voter preference dict 
    and the vote count dict for each ballot 
    '''
    if f == None:
        print(title)                
        for key, value in sorted(dict1.items()):
                print("   {} -> {}".format(key, value))
    else:
        print (title)
        sorted_dict1 = f(dict1.items(), boolean)
        for key, value in f(dict1.items(), boolean):
                print("   {} -> {}".format(key, value))

        
#     def k:
#         return t[0]    
#     for (key,value) in sorted(dict1,(key = k),reverse=boolean):
#         print("   {} -> {}".format(key, value))

    
def read_voter_preferences():
    ''' has an open (file) parameter; 
    it returns the dict representing each voter and his/her preferences: 
    dict[str] -> list[str] 
    '''
    filelist = (goody.safe_open('Enter file with voter preferences', 'r', 'No file avail. Try again.',default=None)).readlines()
    raw_dict = {}
    for line in filelist:
        splited_linelst = line.strip().split(';')
        raw_dict[splited_linelst[0]] = splited_linelst[1:]
    return raw_dict
    
def evaluate_ballot(dict1, remaining = None):
    '''has a dict of voter preference (dict[str] -> list[str] read above) 
    and a set of the remaining candidates as parameters; 
    it returns a dictionary whose keys are these candidates and 
    whose values are the number of votes they received on this ballot, 
    based on the description of instant runnoff voting: dict[str] -> int. 
    Remember to count only one vote per voter, 
    for his/her highest ranked candidate stil in the election
    '''
    
    counted_dict = {}
    for key, value in dict1.items():
        not_accessed = True
        for i in range(len(value)):
            if value[i] in remaining and value[i] in list(counted_dict.keys()) and not_accessed:
                counted_dict[value[i]] += 1
                not_accessed = False
            elif value[i] in remaining and value[i] not in list(counted_dict.keys()) and not_accessed:
                counted_dict[value[i]] = 1
                not_accessed = False
    return counted_dict

    
def remaining_candidates(dict2):
    '''has a dict as a parameter whose keys are candidates and 
    whose values are the number of votes they received (dict[str] -> int); 
    it returns a set containing all those candidates remaining in the election 
    (the one(s) receiving the fewest number of votes are absent). 
    Note that if all the candidates receive the same number of votes, 
    then this function returns an empty set
    '''
    min_vote = min((dict2.values()))
    remaining_candidates = {key for key, value in dict2.items() if value != min_vote}
    return remaining_candidates
    

if __name__== '__main__':
    dictionary = read_voter_preferences()
    candidates = (list(dictionary.values()))
    count = 1
    remain = {candidate for candidate_lst in candidates for candidate in candidate_lst}
    remaining_voter_dict = evaluate_ballot(dictionary, remain)
    print_dict("Voter Preferences:", dictionary)
    
    while min(remaining_voter_dict.values()) != max(remaining_voter_dict.values()):
        print_dict("Vote count on ballot #" + str(count) + " with candidates (alphabetically) = " + str(remain), remaining_voter_dict)
        print_dict("Vote count on ballot #" + str(count) + " with candidates (numerical) = " + str(remain), remaining_voter_dict, f = ordering, boolean = True)

        remain = remaining_candidates(remaining_voter_dict)
        remaining_voter_dict = evaluate_ballot(dictionary, remain)
        count += 1
        
    if len(remain) == 1:
        print ('Winner is', remain)
    else:
        print ('No Winner')