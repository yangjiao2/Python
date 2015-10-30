##def try_exec():
##    exec('global c; c = 3* 2')
##    print (c)
##
##
##exec('def f(x):\n  ' + input('Enter a function definition for def f(x): '))
##>> return 2 * x
##print(f(10))
##try_exec()
##print ('-' * 20)
##
##
##exec('def printing(x):\n\tprint ("====" + str(x) + "===")')
##printing('Good luck!')
##'''
##Function calls ... always include ()
##for f in (double, triple, magnitude) : print(f(5))
##'''

##Functions vs Methods
##o.m(...)     =     type(o).m(o,...
##lst = [0,1,2,3,4,5,6,7,8,9]
##
##for i in range(1,len(lst)):
##    print (lst[i - 1:])

##
##a = 1
##b = 2
##print(eval(input('enter an expression:')))
##>> a+b
##exec(input('enter a statement:'))
##>> c = a+b
##>> print (c)




##for (i,j,k) in [(1,2,3), (4,5,6), (7,8,9)] : print (i,j,k)
##
##

##
##class Luck:
##    def __init__(self, luck):
##        self.luck = luck
##a = Luck('Midterm')
##b = Luck('Midterm')
##print (a == b, a is b)
##>> False False
##
##a = Luck('Midterm')
##b = a
##print (a == b, a is b)
##>> True True
##
##a = 3
##b = 3
##print (a == b, a is b, type(a) == int, type(a) is int)
##>> True True True True
##
##x = ['a']
##y = x		# Critical: y and x share the same reference
##>> x: ['a'] y: ['a'] x is y: True x == y: True
##
##x [0] = 'z'	# Mutate x (could also append something to it)
##>> x: ['z'] y: ['z'] x is y: True x == y: True
##
##
##x = ['a']
##y = list(x)	# Critical: y refers to a new list with the same contents as x
##>> x: ['a'] y: ['a'] x is y: False x == y: True
##
##x [0] = 'z'	# Mutate x (could also append something to it: x+)
##>> x: ['z'] y: ['a'] x is y: False x == y: False
##
##is_legal = (lambda x : 0<=x<=5)
##print (is_legal(7))
##>> False
##print (is_legal(3))
##>> True


##vote does not mutated by sorted

##votes = {'Charlie' : 20, 'Able' :  10, 'Baker' : 20, 'Dog' : 15}
##for c,v in sorted(votes.items()) : print('Candidate',c,'got',v,'votes')
##
##votes = {'Charlie' : 20, 'Able' :  10, 'Baker' : 20, 'Dog' : 15}
##for c in sorted(votes) : print('Candidate',c,'got',votes[c],'votes')
##for (c,v) in sorted(votes,key=lambda t : -t[1]): pass
##>> sort in reverse order


##'a' < 'Z'
##>> False

##print(1,2,3,4,sep='--',end='\n')
##print(5,6,7,8,sep='x',end='**')

##args = 1 , 2 , 3
##def learn_star_arg(*args):
##    print (args, type(args))
##def learn_star_star_arg(**kargs):
##    print (kargs, type(kargs))
##
##
##arg = 1 , 2 , 3
##learn_star_arg(arg)
##>> ((1, 2, 3),) <class 'tuple'>
##
##learn_star_star_arg(c = 1, d = 2)
##>> {'d': 2, 'c': 1} <class 'dict'>       <---------------------------- c, d become 'c', 'd'
##
##
##arg = {'a' : 1, 'b' : 2}
##learn_star_arg(arg)
##>> ({'a': 1, 'b': 2},) <class 'tuple'>
##
##print ('\n\n\n\n\n\n')
##
d = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
d = dict( [['a', 1], ['b', 2], ['c', 3], ['d', 4], ['e', 5]] )
d = dict( [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)] )
d = dict( (['a', 1], ['b', 2], ['c', 3], ['d', 4], ['e', 5]) )
d = dict( (('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)) )
d = dict( {('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)} )

##d = dict( {['a', 1], ['b', 2], ['c', 3], ['d', 4], ['e', 5]} )
##>> unhashable
##
##
##Hashable/immutable: strings, tuples, frozenset
##mutable/unhashable: list, sets, dicts

##
##x = {k : len(k) for k in ['one', 'two', 'three', 'four', 'five']}
##print(sorted(x))
##>> ['five', 'four', 'one', 'three', 'two']

## ZIP
##z = zip( ['a','b','c','d'], (1, 2, 3), ['1st', '2nd', '3rd', '4th'] )
##print([i for i in z])
##>> [('a', 1, '1st'), ('b', 2, '2nd'), ('c', 3, '3rd')]

##result = [i for i in zip( (0, 0 ,3), {'a' : 1, 'b': 2}, 'that')]
##print (result)
##print( [i for i in zip(*result)] )
##>> [(0, 'a', 't'), (0, 'b', 'h')]
##>> [(0, 0), ('a', 'b'), ('t', 'h')]

##e = enumerate(['a','b','c','d'], 1)
##print([i for i in e])
##>> [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
##print (e)
##<enumerate object at 0x02220C38>
## same as zip object
##
##from collections import defaultdict
##letters = ['a', 'x', 'b', 'x', 'f', 'a', 'x']
##freq_map = defaultdict(int)    # int not int(); int() returns 0 (when called)
##for l in letters:
##    freq_map[l] += 1	       # in dict, exception raised if l not in d
##print(freq_map)


##letters = ['a', 'x', 'b', 'x', 'f', 'a', 'x']
##freq_dict = dict()	       # note dict only
##for l in letters:
##    freq_dict[l] = freq_dict.setdefault(l,0) + 1
##print(freq_dict)

import re
##m.span(start_index, end_index + 1)
##
##a = re.findall('\d(\d)', '33')
##>> ['3']
##a = re.match('\d(\d)', '33')
##print (a.group())
##>> '33'



##class C:
##    def __init__(self):
##        print('C object created')
##
####D = C	# C and D share the same class object
####y = D()
####>> C object created
##
##
##global_var = 0
##class C:
##    class_var = 0
##    def __init__(self,init_instance_var):
##        self.instance_var = init_instance_var
##    def bump(self,name):
##        print(name,'bumped')
##        #global_var = 100    # comment out this line or the next
##        global global_var    # comment out this line or the previous 
##        global_var += 1 
##        C.class_var += 1
##        self.instance_var += 1
##    def report(self,var):
##        print('instance referred to by ', var,
##              ': global_var =', global_var,
##              '/class_var =', C.class_var,
##              '/instance_var=', self.instance_var)

##x=C(10)
##x.report('x')
##x.bump('x')
##x.report('x')

##y = x
##print('y = x')
##y.bump('y')
##x.report('x')
##y.report('y')


##y.bump('y')
##x.report('x')
##
##instance referred to by  x : global_var = 0 /class_var = 0 /instance_var= 10
##x bumped
##instance referred to by  x : global_var = 1 /class_var = 1 /instance_var= 11
##y = x
##y bumped
##instance referred to by  x : global_var = 2 /class_var = 2 /instance_var= 12
##instance referred to by  y : global_var = 2 /class_var = 2 /instance_var= 12
##y bumped
##instance referred to by  x : global_var = 3 /class_var = 3 /instance_var= 13


##y=C(20)
##x.report('x')
##y.report('y')
##instance referred to by  x : global_var = 1 /class_var = 1 /instance_var= 11
##instance referred to by  y : global_var = 1 /class_var = 1 /instance_var= 20



##class C:
##    def __init__(self):
##        self._mv = 1
##    def _f(self):
##        return self._mv
##
##x =  C()
##print(x._mv, x._f())
##
##x =  C()
##print(x._C__mv, print(x._C__f()))

##def chunk_sum(iterable,n):
##    i = iter(iterable)
##    
##    while True:
##        sum = 0
##        for x in range(n):
##            sum += next(i)
##        yield sum
##
##import traceback
##class Logging:
##    def __init__(self, file_name, stop_exception):
##        self.file = open(file_name,'w')
##        self.stop_exception = stop_exception
##        self.count = 0
##        
##    def log(self,message):
##        self.file.write(message+'\n')
##        self.count += 1
##        
##    def __enter__(self):
##        self.log('Entered Logging context')
##        return self # so log can be called in block
##    
##    def __exit__(self, exc_type, exc_value, exc_traceback):
##        if exc_type == None:
##            self.log('Exited Logging context with no exception')
##        else:
##            self.log('Exited with exception that is ' +
##                     ('stopped here' if self.stop_exception else 'propagated'))
##            traceback.print_tb(exc_traceback,file=self.file)
##        self.log('Logged ' + str(self.count+1)+' messages')
##        self.file.close()
##        return (None if exc_type == None else self.stop_exception)
## 
##            
##with Logging('log1.txt',stop_exception=True) as now:
##    print('do some operations')
##    now.log('successfully did some operations without an exception')
##    print('do some more operations')
##    now.log('successfully did some more operations without an exception')
##    if prompt.for_bool('pretend final operations raised exception?'):
##        raise AssertionError('raised by user')
##    now.log('successfully did final operations without an exception')




######class C:
######    def __init__(self,x,y):
######        self.x = x
######        self.y = y
######    class Cinner():
######        def __init__(self,x):  self.val = x
######        def get     (self)  :  return self.val  
######    def get(self): return (self.x, self.y)
######    def x_gen(self): return C.Cinner(self.x)
######    def y_gen(self): return C.Cinner(self.y)
######
######z = C(1,2)
######a = z.x_gen()
######b = z.y_gen()
######print(z, a, b)
######print(z.get(), a.get(), b.get())