import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


point_x1 = float(input())
point_x2 = float(input())
point_y1 = float(input())
point_y2 = float(input())

print(distance(point_x1, point_x2, point_y1, point_y2))
