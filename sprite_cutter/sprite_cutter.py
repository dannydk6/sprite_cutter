import os
import copy
from skimage import io, color
import scipy.stats
import numpy as np
from pathlib import Path
from .classes import Rectangle, Point

def new_path_name(sheet_path):
    return f"sprites/{sheet_path.split('.png')[0].split('sheets/')[1]}"

def remove_bgColor(img, bgColor):
    new_img = copy.deepcopy(img)
    new_img[np.where( np.all(new_img == bgColor, axis=-1) )] = np.array([0,0,0,0])
    return new_img

def subset_image(image, rect):
    if rect.width <= 0 and rect.height <= 0:
        return image[rect.minHeight, rect.minWidth].reshape(1,1,4)
    elif rect.width == 0 and rect.height > 0:
        return image[rect.minHeight:rect.maxHeight+1,rect.minWidth]
    elif rect.width > 0 and rect.height == 0:
        return image[rect.minHeight,rect.minWidth:rect.maxWidth+1]
    else:
        return image[rect.minHeight:rect.maxHeight+1,rect.minWidth:rect.maxWidth+1]

def add_boxes(image, spriteRectangles, color=None):
    if color is None:
        color = np.array([255,60,60,255]) # cyan
    print(color)
    wimage = copy.deepcopy(image)
    for i, rect in enumerate(spriteRectangles):
        if rect.width > 0 and rect.height > 0:
            wimage[rect.minHeight:rect.maxHeight+1,rect.minWidth] = color
            wimage[rect.minHeight:rect.maxHeight+1,rect.maxWidth] = color
            wimage[rect.minHeight,rect.minWidth:rect.maxWidth+1] = color
            wimage[rect.maxHeight,rect.minWidth:rect.maxWidth+1] = color        
    return wimage

def add_space(subimg, w, h):
    subimg = copy.deepcopy(subimg)
    sides = w - subimg.shape[1]
    if sides % 2 == 0:
        chunk1 = sides//2
        chunk2 = sides//2
    else:
        chunk1 = sides//2
        chunk2 = sides//2 + 1
    left = h - subimg.shape[0]
    newsub = np.append(np.zeros((left,subimg.shape[1],4)),subimg, axis=0)
    newsub = np.append(np.zeros((newsub.shape[0], chunk1,4)), newsub, axis=1)
    newsub = np.append(newsub, np.zeros((newsub.shape[0], chunk2,4)), axis=1)
    return newsub