import math
def circle(radious):
    area = math.pi * radious * radious
    circumference = 2 * math.pi * radious
    return round(area,2),round(circumference,2)

print(circle(3))