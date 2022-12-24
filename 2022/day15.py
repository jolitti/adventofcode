from aocd import numbers
from aocd.models import Puzzle
from shapely import Polygon, LineString
from shapely.ops import unary_union, clip_by_rect
import matplotlib.pyplot as plt

puzzle = Puzzle(year=2022,day=15)

def get_poly(sequence: list[list[numbers]]) -> Polygon:
    poly = Polygon()
    for a,b,c,d in sequence:
        dist = abs(a-c) + abs(b-d)
        points = [(a,b-dist),(a-dist,b),(a,b+dist),(a+dist,b)]
        poly = unary_union([poly,Polygon(points)])
    return poly

poly = get_poly(numbers) # the polygon of the covered areas
line = LineString([(-10000000000,2_000_000),(10000000000,2_000_000)]) # the intersection line
# poly = clip_by_rect(poly,-2000000,2000000,40000000,2000001)
inters = list(poly.intersection(line).coords) # the intersection of the line with the total area
intersx,intersy = [x for x,y in inters],[y for x,y in inters] # reformatting the coordinates for matplotlib
x,y = poly.exterior.xy # coordinates of the exterior of the polygon
plt.plot(x,y)
plt.plot(intersx,intersy)
plt.show()

intersx = list(map(int,intersx))
answer1 = intersx[1] - intersx[0] + 1 # length of the intersecting line
beacons = [(c,d) for a,b,c,d in numbers] # list of the beacon points
for bx,by in beacons: # subtracting positions which definitely contain a beacon
    if by==2_000_000:
        if bx in range(intersx[0],intersx[1]+1): answer1-=1
print(answer1)
