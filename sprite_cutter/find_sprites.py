import copy
import numpy as np
from .classes import Rectangle, Point

def colors_match(color, bgColor):
    return np.all(color == bgColor)

def findContiguous(image, point, bgColor, margin=1):
    visited   = {}
    unvisited = [p for p in neighbors(point, image, margin) if not colors_match(image[p], bgColor)]
    #print(unvisited)
    while len(unvisited) > 0:
        currentPoint = unvisited.pop(0)
        currentColor = image[currentPoint]

        if not colors_match(currentColor, bgColor):
            unvisited += [p for p in neighbors(currentPoint, image, margin) if
                visited.get(p) is None and p not in unvisited and not colors_match(image[p], bgColor)]
            #print(unvisited)
            visited[currentPoint] = 1

    return visited

def neighbors(point, image, margin=1):
    points = []
    if margin > 0:
        for m in range(1, margin+1):
            # direct neighbors
            # -x
            if (point.x > 0):
                points.append(Point(point.y, point.x - m))
            # +x
            if (point.x < image.shape[1] - m):
                points.append(Point(point.y, point.x + m))
            # -y
            if (point.y > 0):
                points.append(Point(point.y - m,point.x))
            # +y
            if (point.y < image.shape[0] - m):
                points.append(Point(point.y + m,point.x))

            # diagonal neighbors
            # -x, -y
            if (point.x > 0 and point.y > 0):
                points.append(Point(point.y - m,point.x - m))

            # -x, +y
            if (point.x > 0 and point.y < image.shape[0] - m):
                points.append(Point(point.y + m,point.x - m))

            # +x, -y
            if (point.x < image.shape[1] - m and point.y > 0):
                points.append(Point(point.y - m,point.x + m))

            # +x, +y
            if (point.x < image.shape[1] - m and point.y < image.shape[0] - m):
                points.append(Point(point.y + m,point.x + m))            
    return points

def find_sprites(image, backgroundColor, margin=3):
    workingImage = copy.deepcopy(image)
    contLoop = True
    spriteRectangles = []
    visited = {}
    for y in range(0, workingImage.shape[0]):
        for x in range(0, workingImage.shape[1]):
            point = Point(y,x)
            color = workingImage[point]
            
            if not colors_match(color, backgroundColor) and visited.get(point) is None:
                #print(f"Found a sprite starting at ({point.x},{point.y})")
                spriteDict = findContiguous(workingImage, Point(y,x), backgroundColor, margin)
                if len(spriteDict) > 0:
                    visited = {**visited, **spriteDict}
                    spritePlot = np.array(list(spriteDict.keys()))
                else:
                    visited[point] = 1
                    spritePlot = np.array([point])
                #print(spritePlot)
                spriteRectangle = Rectangle(spritePlot)
                #print(f"The identified sprite has an area of {spriteRectangle.area}")
                spriteRectangles.append(spriteRectangle)
    print(f"Found {len(spriteRectangles)} sprites.")
    return spriteRectangles