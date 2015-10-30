# Yang Jiao, Lab 1
# Anita Marie Gilbert, Lab 1
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
from goody import irange

def sequence(*args):
    '''takes any number of iterables as parameters: it produces all the values 
    in the first iterable, followed by all in the second, ... , all values in the last iterable. 
    '''
    for i in args:
        yield i
    

def transform(iterable, f):
    '''takes any iterable and any function whose domain includes all the iterated values: 
    it produces transformed (by the function) values.
    '''
    yield f(iterable)


def count(iterable, predicate):
    ''' takes any iterable and any predicate function (returning bool values): 
    it produces a running count of how many values up to the one just iterated over, 
    satisfied the predicate.
    '''
    for i in iterable:
        if predicate(i):
            yield i

def chunk_sum(iterable, n):
    ''' takes any iterable and an int n: it produces a sum of the first n values, 
    the sum of the second n values, etc. If there aren't n more values in the iterable, 
    chunk_sum cannot produce the next result.
    '''
    
    index = 1
    result = 0
    iterator = iter(list(iterable))

    while True:
        a = next(iterator)
        if index == n:
            yield result + a
            result = 0
            index = 1
        else:
            result += a 
            index += 1
    


        
    

def flatten(iterable):
    '''that returns every value nested in any iterable data type
    (except for string: return strings as themselves, not their individual characters
    '''
    iterable = iter(iterable)
    for i in iterable:
        if type(i) == int or type(i) == str:
            yield  i
        else:
            for t in flatten(i):
                yield t           
             

        


         