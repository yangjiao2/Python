# Yang Jiao, Lab 6
# Anita Marie Gilbert, Lab 6
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

class Bag:

 
    def __init__(self, parameter):
        '''has one parameter, an iterable of values that initalize the bag. 
        Writing Bag(['d','a','b','d','c','b','d']) construct a bag with one 'a', 
        two 'b', one 'c', and three 'd'
        '''
        self.para = parameter
        self.dict = dict()
        for item in parameter:
            self.dict[item] = self.dict.setdefault(item, 0) + 1

        
     
    def __repr__(self):
        '''returns a string, which when passed to eval returns a newly constructed 
        rational with the same value (==) to the object __repr__ was called on. 
        For example, for the Bag in the discussion of __init__ the __repr__ method 
        would print its result as Bag(['a', 'c', 'b', 'b', 'd', 'd', 'd']). 
        Bags like sets are not sorted, so these 7 values can appear in any order.
        '''
        return 'Bag(' + str(self.para) + ')'
 
    def __str__(self):
        '''returns a string that more compactly shows a bag. 
        For example, for the Bag in the discussion of __init__ the __str__ 
        method would print its result as Bag(a[1], c[1], b[2], d[3]). 
        Bags like sets are not sorted, so these 7 values can appear in any order.
        '''
        result = 'Bag('
        for k in self.dict:
            result += str(k) + '[' + str(self.dict[k]) + '], '
        return result[:-2] + ')'  
 
    def __len__(self):
        ''' returns the total number of values in the Bag. 
        For example, for the Bag in the discussion of __init__ the __len__ method would return 7.
        '''
        return sum(list(self.dict.values()))
        
    def __contains__(self, arg):
        ''' returns whether or not its argument is in the Bag.
        '''
        return (arg in list(self.dict.keys()))
     
 
    def count(self, arg):
        ''' returns the number of times its argument is in the Bag:
         0 if the argument is not in the Bag.
         '''
        return self.dict[arg]
 
    def add(self, item):
        ''' adds its argument to the Bag: if that value is already in the Bag, 
        its count is incremented by 1; if it is not, it is added to the Bag with a count of 1.
        '''
        self.dict[item] = self.dict.setdefault(item, 0) + 1
        
 
    def remove(self, item):
        ''' removes its argument from the Bag: if that value is already in the Bag, 
        its count is decremented by 1 (and if the count reduces to 0 it is removed from the dict; 
        if it is not in the Bag, throw a ValueError exception, with an appropriate message that 
        includes the value that could not be removed.
        '''
        self.dict[item] = self.dict.setdefault(item, 0) - 1
        
 
    def __iter__(self):
        ''' that returns an object on which next can be called to produce every value in the Bag: 
        all len of them.
        '''
#         self.iterdict = iter(self.dict)
        def __gen(d):
            for k in d:
                c = d[k]
                yield k*c
        return __gen(self.dict)




