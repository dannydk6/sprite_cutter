import numpy as np
from collections import namedtuple

Point = namedtuple("Point","y x")

class Rectangle(object):
    def __init__(self, spritePlot):
        curY = spritePlot[:,0]
        curX = spritePlot[:,1]
        maxHeight = np.max(curY)
        minHeight = np.min(curY)
        maxWidth = np.max(curX)
        minWidth = np.min(curX)
        self.spritePlot = spritePlot
        self.maxHeight = maxHeight
        self.minHeight = minHeight
        self.maxWidth = maxWidth
        self.minWidth = minWidth
        self.width = maxWidth - minWidth
        self.height = maxHeight - minHeight
    def __repr__(self):
        return f"Rectangle(\
        \n\tminW={self.minWidth},\
        \n\tmaxW={self.maxWidth},\
        \n\tminH={self.minHeight},\
        \n\tmaxH={self.maxHeight}\n\t)"
    def __eq__(self, other):
        return self.minWidth == other.minWidth \
               and self.minHeight == other.minHeight \
               and self.maxHeight == other.maxHeight \
               and self.maxWidth == other.maxWidth

    def __lt__(self, other):
        return self.minWidth < other.minWidth \
                and self.height_overlaps(other)
                
    def height_overlaps(self, other):
        if ((self.minHeight <= other.maxHeight and self.maxHeight >= other.maxHeight) or 
            (self.maxHeight >= other.minHeight and self.minHeight <= other.maxHeight)):
            return True
        return False

    @property
    def area(self):
        return f"{self.width}x{self.height}"