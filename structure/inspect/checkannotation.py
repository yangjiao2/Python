# Yang Jiao, Lab 6
# Anita Marie Gilbert, Lab 6
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

from goody import type_as_str
import inspect

from goody import irange, type_as_str

from collections import defaultdict
from goody import type_as_str
class Bag:
    def __init__(self,values=[]):
        self.counts = defaultdict(int)
        for v in values:
            self.counts[v] += 1
    
    def __str__(self):
        return 'Bag('+', '.join([str(k)+'['+str(v)+']' for k,v in self.counts.items()])+')'

    def __repr__(self):
        param = []
        for k,v in self.counts.items():
            param += v*[k]
        return 'Bag('+str(param)+')'

    def __len__(self):
        return sum(self.counts.values())
        
    def unique(self):
        return len(self.counts)
        
    def __contains__(self,v):
        return v in self.counts
    
    def count(self,v):
        return self.counts[v] if v in self.counts else 0

    def add(self,v):
        self.counts[v] += 1
    
    def remove(self,v):
        if v in self.counts:
            self.counts[v] -= 1
            if self.counts[v] == 0:
                del self.counts[v]
        else:
            raise ValueError('Bag.remove('+str(v)+'): not in Bag')
        
    def __eq__(self,right):
        if type(right) is not Bag or len(self) != len(right):
            return False
        else:
            for i in self.counts:
                # check not it to avoid creating count of 0 via defaultdict
                if i not in right or self.counts[i] != right.counts[i]:
                    return False
            return True
        
    @staticmethod
    def _gen(x):
        for k,v in x.items():
            for i in range(v):
                yield k  
                
    def __iter__(self):
        return Bag._gen(dict(self.counts))
    
    #define this method to implement the check annotation protocol
    def __check_annotation__(self, check, param, value, check_history):
        for value in self.counts:
            check(param, annot, value, check_history+'Bag value check: '+str(annot))


    

class Check_All_OK:
    """
    Check_ALl_OK implements __check_annotation__ by checking whether all the
      annotations passed to its constructor are OK; the first one that
      fails (raises AssertionError) prints its problem, with a list of all
      annotations being tried at the end of the check_history.
    """
       
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_All_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value,check_history):
        for annot in self._annotations:
            check(param, annot, value, check_history+'Check_All_OK check: '+str(annot)+' while trying: '+str(self)+'\n')


class Check_Any_OK:
    """
    Check_Any_OK implements __check_annotation__ by checking whether at least
      one of the annotations passed to its constructor is OK; if all fail 
      (raise AssertionError) this classes raises AssertionError and prints its
      failure, along with a list of all annotations tried followed by the check_history.
    """
    
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_Any_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value, check_history):
        failed = 0
        for annot in self._annotations: 
            try:
                check(param, annot, value, check_history)
            except AssertionError:
                failed += 1
        if failed == len(self._annotations):
            assert False, repr(param)+' failed annotation check(Check_Any_OK): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history                 
'''
 when the decorated f is called, Python calls Check_Annotations.__call__ in the decorator, 
 which can both check the annotations and compute/return the decorated function f: the original one written. 
'''
class Check_Annotation():
    # must be True for checking to occur
    checking_on  = True
  
    # self._checking_on must also be true for checking to occur
    def __init__(self,f):
        self._f = f
        self.checking_on = True
        if self.checking_on:
            pass
        

    # Check whether param's annot is correct for value, adding to check_history
    #    if recurs; defines many local function which use it parameters.  
    def check(self,param,annot,value,check_history=''):
        ''' remember the function being decorated and initialize a per-function name that helps controls annotation checking; 
        it also starts on: for a function call to check its annotation, both checking_on and its per-function name must be True
        '''
        # Define local functions for checking, list/tuple, dict, set/frozenset,
        #   lambda/functions, and str (str for extra credit)
        # Many of these local functions called by check, call check on their
        #   elements (thus are indirectly recursive)

        # Decode annotation and check it 
        
        # self is to make it an object later
        # para, is the x
        # annot is the type of x
        # value is the real value of x
        # check history is the record of all things that have gone through
        
        check = ''
        if annot == None:
            pass
        
        elif isinstance(annot, type):
            try: 
                assert type(value) == annot, "'" + str(param) + "'" + " failed annotation check(wrong type): value = " + str(value) + " was type " + str(type(value)) + " ...should be type "+ str(annot) + '\n' + check_history
            except:
                raise 
            
        elif type_as_str(annot) == 'list':
           
            try: 
                assert type(value) == list, "'" + str(param) + "'" + " failed annotation check(wrong type): value = " + str(value) + " was type " + str(type(value)) + " ...should be type "+ str(annot)
                if len(annot) <= 1:
                    for num in range(len(value)):
                        check = 'list[' + str(num) + '] check: ' + str(annot)  + '\n'    
                        self.check(param,annot[0],value[num],check_history+check) 
                else:
                    
                    assert len(annot) == len(value) , "'" + str(param) + "'" + " failed annotation check (wrong number of elements): value = " + str(value) + " annotation had " + str(len(annot)) +  " elements " + str([type(i) for i in annot])
                    for num in range(len(value)):
                        check = 'list[' + str(num) + '] check: ' + str(annot)  + '\n'
                        self.check(param,annot[num],value[num],check_history+check), str(check)           
            except:
                raise 
            
        elif type_as_str(annot) == 'tuple':
            try: 
                assert type(value) == list, "'" + str(param) + "'" + " failed annotation check(wrong type): value = " + str(value) + " was type " + str(type(value)) + " ...should be type "+ str(annot)
                if len(annot) <= 1:
                    for num in range(len(value)):
                        check = 'tuple[' + str(num) + '] check: ' + str(annot)  + '\n'    
                        self.check(param,annot[0],value[num],check_history+check) 
                else:
                    
                    assert len(annot) == len(value) , "'" + str(param) + "'" + " failed annotation check (wrong number of elements): value = " + str(value) + " annotation had " + str(len(annot)) +  " elements " + str([type(i) for i in annot])
                
                    for num in range(len(value)):
                        check = 'tuple[' + str(num) + '] check: ' + str(annot)  + '\n'    
                        assert self.check(param,annot[num],value[num],check_history+check), str(check)           
            except:
                raise 
  
            
        elif type_as_str(annot) == 'dict':
            try:
                assert type(value) == dict, "'" + str(param) + "'" + " failed annotation check(wrong type): value = " + str(value) + " was type " + str(type(value)) + " ...should be type "+ str(annot)
                dictype = dict()
                for k in value:
                    dictype[type(k)] = type(value[k])
                assert len(annot) == 1, "'" + str(param) + "'" + 'annotation inconsistency: dict should have 1 item but had ' + str(len(value)) + ' annotation = {' + (str(dictype))
                if len(annot) == 1:
                    for k_value, v_value in value:
                        for k_annot, v_annot in annot:
                            check = '\n dict key check: ' + str(k_annot)
                            self.check(param,k_annot,k_value,check_history+check)
                            check = '\n dict value check: ' + str(v_annot)
                            self.check(param,v_annot,v_value,check_history+check)
            except:
                raise
            
        elif type_as_str(annot) == 'set':
            try: 
                assert type(value) == set,  "'" + str(param) + "'" + " failed annotation check(wrong type): value = " + str(value) + " was type " + str(type(value)) + " ...should be type "+ str(annot)
                assert len(annot) == 1, "'" + str(param) + "'" + 'annotation inconsistency: set should have 1 value but have ' + str(len(annot)) + " annotation =" + str({type(i) for i in annot})
                for num in range(len(value)):
                    check = 'set value check: ' + str(annot)  + '\n'  
                    self.check(param,annot[0],value[num],check_history+check)  
            except:
                raise 
        
        elif type_as_str(annot) == 'frozenset':
            try: 
                assert type(value) == frozenset,  "'" + str(param) + "'" + " failed annotation check(wrong type): value = " + str(value) + " was type " + str(type(value)) + " ...should be type "+ str(annot)
                assert len(annot) == 1, "'" + str(param) + "'" + 'annotation inconsistency: frozenset should have 1 value but have ' + str(len(annot)) + " annotation =" + str({type(i) for i in annot})
                for num in range(len(value)):
                    check = 'frozenset value check: ' + str(annot)  + '\n'  
                    self.check(param,annot[0],value[num],check_history+check)  
            except:
                raise 
        
        elif inspect.isfunction(annot):
            try: 
                assert len(annot.__code__.co_varnames) == 1, "'" + str(param) + "'" + 'annotation inconsistency: predicate should have 1 parameter but had ' + str(len(annot.__code__.co_varnames)) + ' predicate = ' + str(annot) 
                
                assert annot(value) == False,  "'" + str(param) + "'" + " failed annotation check(wrong type): value = " + str(value) + '\n  predict = ' + str(annot) 
            except AssertionError:
                raise
            except Exception as msg:
                raise AssertionError ("'" + str(param) + "'" + "annotation predicate (" + str(annot) + ") raised exception \n  exception = " + str(msg) )
         
        elif type_as_str(annot) == 'str':

            assert type(value) == str
            
                     
        else: 

            try:
                annot.__check_annotation__(self, check, param, value,check_history)
            except AttributeError as msg:
                raise AssertionError( "'" + str(param) + "'" + ' annotation undecipherable: ' + str(value))
            except  AssertionError as msg:
                raise 
            except Exception as msg:
                raise AssertionError ("'" + str(param) + "'" + "annotation predicate (" + str(annot) + ") raised exception \n  exception = " + str(msg) )

                       
                
    # Return decorated function call, checking present parameter/return
    #   annotations if required
    def __call__(self, *args, **kargs):
        ''' intercepts each call to the decorated function and decides (and implements) annotation checking, 
        both for parameters and returned results, if they are specified; 
        if annotation checking succeeds, this method returns the result of calling the decorated function. 
        '''

        # Return a dictionary of the parameter/argument bindings (actually an
        #    ordereddict, in the order parameters occur in the function's header)
        def param_arg_bindings():
            f_signature  = inspect.signature(self._f)
            
            bound_f_signature = f_signature.bind(*args,**kargs)
            for param in f_signature.parameters.values():
                if param.name not in bound_f_signature.arguments:
                    bound_f_signature.arguments[param.name] = param.default
            return bound_f_signature.arguments

        check_history = ''
        
        for k, v in self._f.__annotations__.items():
            annot = v
            
        if self.checking_on and Check_Annotation(self._f).checking_on:
            result = self._f(*args, **kargs)
            print ('--------------------------------------------------------------------------------')
            for line in [item for item in inspect.getsourcelines(self._f)]:
                print ('    ' + str(line))
            print ('--------------------------------------------------------------------------------')
            for param, value in  param_arg_bindings().items():

                
                if 'return' in self._f.__annotations__:
                    annot['_return'] = result
                    
                else:
                    self.check(param,annot,value, check_history)
#                 try:
#                     self.check(param,annot,value, check_history)
#                 except AssertionError as msg:                                      
#                     raise AssertionError('Line number: '+ str(inspect.getsourcelines(self._f))+' ' + str(msg))
            return self._f(*args, **kargs)
        else:
            return self._f(*args, **kargs)
            
            
      
        
        
        # If annotation checking is turned off at the class or function level
        #   just return the result of calling the decorated function
        
        # On first AssertionError, print the source lines of the function and reraise 

            # Check the annotation for every parameter (if there is one)
                    
            # Compute/remember the value of the decorated function
            
            # If the return has an annotation, check it
            
            # Return the decorated answer

  

