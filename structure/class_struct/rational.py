# Yang Jiao, Lab 6
# Anita Marie Gilbert, Lab 6
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import math

class Rational:
    def _gcd (self, raw_num, raw_denom):
        '''
        (greatest common divisor) algorithm in a class method and 
        call it as needed in the __init__ method.
        '''
        num = raw_num
        denom = raw_denom
        while num%denom != 0:
            num, denom = denom, num%denom
        return (raw_num/ denom, raw_denom/ denom)

    def __rgcd__(self,second):
        result = self.__gcd__(second)
        return result
       
            
        
    def __init__(self,num = 0, denom = 1):
        if type(num) is not int or type(denom) is not int or denom == 0:
            raise AssertionError('Rational should be integers and denominator should not be zero')
        elif num == 0 and denom == 0:
            self.num = abs(num)
            self.denom = 1
        else:
            num, denom = self._gcd(num, denom)          
            self.num = int((num /abs(num))*(denom /abs(denom))* abs(num))
            self.denom = int(abs(denom))





    #===========================================================================
    # def __len__(self):
    #     ''' __len__ is the total number of characters the number takes up on the console to print.
    #     So, for 2/5 the __len__ is 3.
    #     '''
    #     return len(str(self.top)) + len(str(self.bottom)) + 1
    #===========================================================================
    
    def __lt__(self,second):
        ''' if the rational number (self) on the left is less than second rational
        number entered it returns True
        '''
        if type(self) is int:
            self = Rational(self)
 
        if type(second) is int:
            second = Rational(second)
            
        return ((self.num/self.denom - second.num/second.denom) < 0)
  
    def __rlt__(self,second):
        result = self.__lt__(second)
        return result  
 

        
    def __repr__(self):
        '''returns a string, which when passed to eval returns a newly constructed rational
        with the same value (==) to the object __repr__ was called on.
        '''
        return 'Rational(' + str(self.num) + ',' + str(self.denom) + ')'        

    def __str__(self):
        '''returns a string, with the (signed) numerator and the denominator
        (always positive) separated by a slash(/); see examples of of printing a Rational above.
        '''
        return  str(self.num) + '/' + str(self.denom) 
   
    def __mul__(self,second):

        if type(self) is int:
            self = Rational(self)
 
        if type(second) is int:
            second = Rational(second)

        if type(second) is Rational and type(self) is Rational:
            return Rational(self.num * second.num , self.denom * second.denom)
        else:
            raise TypeError('Rational.__mul__ second not Rational('+str(type(second))[8:-2]+')')
        
    def __rmul__(self,second):
        result = self.__mul__(second)
        return result
    
    def __add__(self,second):

        if type(self) is int:
            self = Rational(self)
        if type(second) is int:
            second = Rational(second)

        if type(second) is Rational and type(self) is Rational:
            if self.denom == second.denom:
                return Rational(self.num + second.num, self.denom)
            else:
                temp_self = self.num*second.denom

                temp_second = second.num*self.denom
  
                return Rational((temp_self + temp_second), self.denom*second.denom)
        else:
            raise TypeError('Rational.__add__ second not Rational('+str(type(second))[8:-2]+')')
        
    def __radd__(self, second):
        result = self.__add__(second)
        return result

        
    def __sub__(self,second):

        if type(second) is Rational and type(self) is Rational:
            result = self.__add__(-second)
            return result
        else:
            raise TypeError('Rational.__sub__ second not Rational('+str(type(second))[8:-2]+')')
  
    def __rsub__(self, second):
        result = self.__sub__(-ssecond)
        return result
        
        
    def __truediv__(self,second):
        if self is int:
            self = Rational(self)
        if second is int:
            second = Rational(second)
        if type(second) is Rational and type(self) is Rational:            
            return Rational(self.num * second.denom , self.denom * second.num)

        else:
            raise TypeError('Rational.__truediv__ second not Rational('+str(type(second))[8:-2]+')')      
   
    def __rtruediv__(self, second):
        result = self.__truediv__(second)
        return result     
    
    def __abs__(self):
        if self.num < 0:
            return Rational((-self.num),self.denom)
        else:
            return self
        
    def __pos__(self):
        return self
        
    def __neg__(self):
        return Rational(-self.num, self.denom)

        
    def __pow__(self,second):
        if type(second) != int:
            raise TypeError('Rational.__pow__ second not int('+str(type(second))[8:-2]+')')
        elif second > 0:
            return Rational(self.num**second, self.denom**second)
        else:
            return Rational(self.denom ** abs(second), self.num** abs(second))

    def approximate(self, num):
        int_part = '' if str(self.num // self.denom) >= '0' else '-'
        int_part += str(abs(self.num) // self.denom) if str(abs(self.num) // self.denom) != '0' else ''
        frac_part = '.'
        for i in range(num):
            frac_part += str((10**(i+1) * abs(self.num)) // (self.denom))[-1]
        return int_part + frac_part 

    def __setattr__(self, name, value):
        '''method so that after the num and denom instances variables are set in __init__
        trying to change them will raise the NameError exception '''

        if 'num'== name and 'num' in self.__dict__:
            raise NameError('Num has been changed')
        if 'denom' == name and 'denom' in self.__dict__:
            raise NameError('Denom has been changed')
        else:
            self.__dict__[name] = value
            
     
    def best_approximation(self, limit):
        '''Return a rational number closest to the one this method is called on, 
        subject to the requirement that its numerator and denominator contain 
        no more digits than the integer argument. 
        For example Rational(314159,100000).best_approximation(2) returns 22/7s
        '''      
        # may use approximate
        init = self.num // self.denom

        pk = init
        qk = 1
        result = Rational(1,1)
        measure = Rational(10**limit, 1)

        while (pk < (10 ** limit) - 1) and (qk < (10 ** limit) -1) :
            pk +=1    
            for qk in range(pk //  (init+1), pk //  (init-1)):

                if abs(Rational(pk, qk) - self) < measure:                   
                    measure = abs(Rational(pk, qk) - self)
                    result = Rational(pk, qk)                
        return result            
                
                
            

##print (Rational(314159,100000).best_approximation(3)) 
##    
##x = Rational(63,20)
##
##y = Rational(1,200)



