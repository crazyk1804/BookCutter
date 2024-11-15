class Rect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
    def to_tuple(self):
        return self.x, self.y, self.x + self.w, self.y + self.h