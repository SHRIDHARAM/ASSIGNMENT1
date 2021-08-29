#To find the distance between two co-ordinates when the axes are inclined.
import math

x = [int(input('enter the co-ordinates of 1st point')) for i in range(2)]
print('P1 is',x)
y = [int(input('enter the co-ordinates of 2nd point')) for i in range(2)]
print('P2 is',y)
w = math.radians(int(input('enter the angle between axes')))
print(w)

def distance(x, y, w):
    z = math.sqrt(((x[0] - y[0]) ** 2) + ((x[1] - y[1]) ** 2) + 2 * (x[0] - y[0]) * (x[1] - y[1]) * math.cos(w))
    print('the distance between two point is',z)


result = distance(x, y, w)
