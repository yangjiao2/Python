# Yang Jiao, Lab 1
# Anita Marie Gilbert, Lab 1
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming



import re, traceback, keyword, prompt
from collections import defaultdict

class Unique:
    def __init__(self,iterable):
        self.iterable = iterable
        
    def __iter__(self):
        class Unique_iter:
            def __init__(self,iterable):
                self.iterated = set()
                self.iterator = iter(iterable)
            
            def __next__(self):
                answer = next(self.iterator)
                while answer in self.iterated:
                    answer = next(self.iterator)
                self.iterated.add(answer)
                return answer

        return Unique_iter(self.iterable)
        
def pnamedtuple(type_name, field_names, mutable=False):
    
    def show_listing(s):
        i = 1
        for l in s.split('\n'):
            print('{num: >3} {text}'.format(num=i, text = l.rstrip()))
            i += 1
    
    m1 = re.match('[^0-9](\w*)', type_name)
    if not m1:
        raise SyntaxError('Illegal type name: '+ type_name)
    
    name = "class " + str(type_name)+ ":\n"
    if type(field_names) == list:
        if len(field_names) == 0:
            initresult = ''
        else:
            initresult =  ','.join(field_names)
    elif type(field_names) == str:
        if field_names.strip() == '':
            initresult = ''
        if ' ' in field_names and ',' not in field_names:
            initresult = ','.join(field_names.split())
        elif ',' in field_names:
            initresult = field_names
    
    if initresult == '':
        result = ''
        rawresult = []
    else:
        rawresult = initresult.split(',')
        rawresult = list(Unique(rawresult))
        for element in rawresult:
            m2 = re.match('[^0-9](\w*)', element)
            if not m2:
                raise SyntaxError('Illegal type name: '+ element)
        result = ',' + ','.join(rawresult)
    
    
                
    init_string = '    def __init__(self'+ str(result) + '):\n'
    get_string = ""
    things = ""
    with_self = ""
    
    fields = "        self._fields = " + str(rawresult) + '\n'
    for i in rawresult:
        i = i.strip()
        if len(i) != 0:
            init_string += '        self.' + str(i) + ' = ' + str(i) + '\n'
            get_string += '\n    def _get_' + str(i) + '(self):\n        return self.' + str(i) + '\n'
            things += str(i) + "={}"+","
            with_self += "self."+str(i)+","

    mut = "        self._mutable = " + str(mutable) + '\n'
    rep = '\n    def __repr__(self):\n        return "' + type_name + '('+ things[:-1] +')".format('+with_self[:-1]+')'            
    indexing = '''\n
    def __getitem__(self,index):
        if index > len(self._fields):
            raise IndexError ('Index out of the range.')
        else:
            return eval("self._get_"+ self._fields[index]+"()")'''
    
    replace = '''\n
    def  _replace (self, **kargs):
        if self._mutable:
            for k in kargs:
                if k in self.__dict__:
                    self.__dict__[k] = kargs[k]
                else:
                    raise KeyError('KeyError: ' + str(k) +' is not key')
        else:
            newresult = dict()
            for i in range(len(self._fields)):
                newresult[self._fields[i]] = (kargs[self._fields[i]] if self._fields[i] in kargs else self.__getitem__(i))           
            return ''' + type_name + '(' + ' **newresult' + ')'


    setattribute = '''\n
    def __setattr__(self, name, value):     
        if name in self.__dict__:
            if self._mutable == False:
                raise AttributeError( 'Attempted to change instance variable: ' + name)
            else:
                self.__dict__[name] = value
        else:
            self.__dict__[name] = value'''

  
 
    class_definition ='{}{}{}{}{}{}{}{}{}'.format(name,init_string,fields,mut,get_string,rep, indexing, replace, setattribute)
    print(class_definition)

    # Execute the class_definition string in a temporary name_space and

    name_space = dict(__name__='pnamedtuple_{type_name}'.format(type_name=type_name))
    try:
        exec(class_definition, name_space)
    except SyntaxError:
        
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]

