import math

def getDirection(loc1, loc2):
    rel = (loc2[0] - loc1[0], -(loc2[1] - loc1[1]))
    return math.degrees(math.atan2(rel[1], rel[0])) % 360

def getDistance(loc, loc2):
    return math.sqrt((loc[0] - loc2[0])**2 + (loc[1] - loc2[1])**2)

def isRight(d):
    return d >= 315 and d <= 360 or d >= 0 and d < 45

def isUp(d):
    return d >= 45 and d < 135

def isLeft(d):
    return d >= 135 and d < 225

def isDown(d):
    return d >= 225 and d < 315
