import math

class Circle:
    def __init__(self, radius, center = None):
        self.radius = radius
        self.center = center
        if center == None:
            self.center = (radius, radius)
        self.centerx = center[0]
        self.centery = center[1]
        self.top = self.centery - self.radius
        self.bottom = self.centery + self.radius
        self.left = self.centerx - self.radius
        self.right = self.centerx + self.radius

    def update(self, center):
        self.center = center
        self.centerx = self.center[0]
        self.centery = self.center[1]
        self.top = self.centery - self.radius
        self.bottom = self.centery + self.radius
        self.left = self.centerx - self.radius
        self.right = self.centerx + self.radius

    def calculateDistance(self, point):
        return (math.sqrt((self.centerx - point[0])**2 + (self.centery - point[1])**2))
    
    def isInsideRect(self, rect):
        return (self.centerx > rect.left and self.centerx < rect.right and\
                self.centery > rect.top and self.centery < rect.bottom)

    def isAboveRect(self, rect):
        return (self.centerx > rect.left and self.centerx < rect.right and\
                self.centery < rect.top)

    def isBelowRect(self, rect):
        return (self.centerx > rect.left and self.centerx < rect.right and\
                self.centery > rect.bottom)

    def isLeftOfRect(self, rect):
        return (self.centery > rect.top and self.centery < rect.bottom and\
                self.centerx < rect.left)

    def isRightOfRect(self, rect):
        return (self.centery > rect.top and self.centery < rect.bottom and\
                self.centerx > rect.right)

    def collideRect(self, rect):
        if self.isInsideRect(rect):
            return True
        elif self.isAboveRect(rect):
            return rect.top < self.bottom
        elif self.isBelowRect(rect):
            return rect.bottom > self.top
        elif self.isLeftOfRect(rect):
            return rect.left < self.right
        elif self.isRightOfRect(rect):
            return rect.right > self.left
        else:
            topLeftDist = self.calculateDistance(rect.topleft)
            topRightDist = self.calculateDistance(rect.topright)
            bottomLeftDist = self.calculateDistance(rect.bottomleft)
            bottomRightDist = self.calculateDistance(rect.bottomright)
            return (topLeftDist < self.radius or topRightDist < self.radius or\
                    bottomLeftDist < self.radius or bottomRightDist < self.radius)

    def collideCircle(self, circle):
        dist = self.calculateDistance(circle.center)
        return (dist <= self.radius + circle.radius)
