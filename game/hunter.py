# Yang Jiao, Lab 6
# I certify that I written all the code in this programming assignment
#   by myself.


# A Hunter is both a Mobile_Simulton and Pulsator; it updates
#   as a Pulsator, but also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from math import atan2
from mobilesimulton import Mobile_Simulton
from prey import Prey
from pulsator import Pulsator
import functools
import model, math
from random import random
class Hunter(Pulsator,Mobile_Simulton):
    
    def __init__(self, x, y):
        Pulsator.__init__(self,x,y)
        Mobile_Simulton.__init__(self,x,y, width = 10 * 2, height = 10 * 2, angle = random()* math.pi ,speed = 5)
        
    def update(self):
        closest = None
        Pulsator.update(self)
        s = model.find(lambda x: isinstance (x,Prey) and self.distance((x._x, x._y) )< 200)
        minimum = 200
        for p in s:
            if minimum > self.distance( (p._x, p._y)):
                closest = p
                minimum =  self.distance( (p._x, p._y))
        if closest != None:
            self._angle =  atan2( closest._y - self._y, closest._x - self._x)        
        self.move()
        
    
        
        