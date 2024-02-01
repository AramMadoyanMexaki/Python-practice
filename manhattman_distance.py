# Manhattan Distance point(|x1, x2|, |y1, y2|) = ∣x2−x1∣+∣y2−y1∣

class Points():
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def manhattan_distance(self):
        return abs(self.x2 - self.x1) + abs(self.y2 - self.y1)

obj = Points(5, 4, 3, 2)
print(obj.manhattan_distance())