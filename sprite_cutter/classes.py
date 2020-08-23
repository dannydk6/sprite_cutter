import numpy as np
from collections import namedtuple
import numpy as np
from numba import int32, float32    # import the types
from numba.experimental import jitclass

spec = [
    ('maxHeight', int32),           # a simple scalar field
    ('maxWidth', int32),  
    ('minHeight', int32),  
    ('minWidth', int32),  
    ('width', int32),  
    ('height', int32),   
]



Point = namedtuple("Point","y x")

@jitclass(spec)
class Rectangle(object):
    def __init__(self, spritePlot):
        curY = spritePlot[:,0]
        curX = spritePlot[:,1]
        maxHeight = np.max(curY)
        minHeight = np.min(curY)
        maxWidth = np.max(curX)
        minWidth = np.min(curX)
        #self.spritePlot = spritePlot
        self.maxHeight = maxHeight
        self.minHeight = minHeight
        self.maxWidth = maxWidth
        self.minWidth = minWidth
        self.width = maxWidth - minWidth
        self.height = maxHeight - minHeight
    # def __repr__(self):
    #     return f"Rectangle(\
    #     \n\tminW={self.minWidth},\
    #     \n\tmaxW={self.maxWidth},\
    #     \n\tminH={self.minHeight},\
    #     \n\tmaxH={self.maxHeight}\n\t)"
    # def __eq__(self, other):
    #     return self.minWidth == other.minWidth \
    #            and self.minHeight == other.minHeight \
    #            and self.maxHeight == other.maxHeight \
    #            and self.maxWidth == other.maxWidth

    # def __lt__(self, other):
    #     return self.minWidth < other.minWidth \
    #             and self.height_overlaps(other)
                
    def height_overlaps(self, other):
        if ((self.minHeight <= other.maxHeight and self.maxHeight >= other.maxHeight) or 
            (self.maxHeight >= other.minHeight and self.minHeight <= other.maxHeight)):
            return True
        return False

    #@property
    #def area(self):
    #    return f"{self.width}x{self.height}"