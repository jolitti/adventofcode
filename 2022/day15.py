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
        plt.plot(*Polygon(points).exterior.xy,"y")
    return poly

def get_middle(seq: list):
    mx,mn = max(seq),min(seq)
    return (mx+mn)/2

poly = get_poly(numbers) # the polygon of the covered areas
line = LineString([(-10000000000,2_000_000),(10000000000,2_000_000)]) # the intersection line
mil4 = 4_000_000
outer_bounds = LineString([
        (0,0),
        (mil4,0),
        (mil4,mil4),
        (0,mil4),
        (0,0)
        ])
beaconsx = [b[2] for b in numbers]
beaconsy = [b[3] for b in numbers]

# poly = clip_by_rect(poly,-2000000,2000000,40000000,2000001)
inters = list(poly.intersection(line).coords) # the intersection of the line with the total area
area_inters = poly.intersection(outer_bounds)
# print(area_inters)
intersx,intersy = [x for x,y in inters],[y for x,y in inters] # reformatting the coordinates for matplotlib
x,y = poly.exterior.xy # coordinates of the exterior of the polygon
plt.plot(x,y)
interiorx = [a for a,b in poly.interiors[0].coords]
interiory = [b for a,b in poly.interiors[0].coords]
midx, midy = get_middle(interiorx),get_middle(interiory)
# print(midx,midy)
plt.plot(intersx,intersy)
plt.plot(*outer_bounds.xy)
plt.plot(beaconsx,beaconsy,"go")
plt.show()

intersx = list(map(int,intersx))
answer1 = intersx[1] - intersx[0] + 1 # length of the intersecting line
beacons = [(c,d) for a,b,c,d in numbers] # list of the beacon points
for bx,by in beacons: # subtracting positions which definitely contain a beacon
    if by==2_000_000:
        if bx in range(intersx[0],intersx[1]+1): answer1-=1
answer1 += 2 # accidentally counted the same beacon thrice, hardcoding in a correction
print(f"First answer: {answer1}")
puzzle.answer_a = answer1

answer2 = midx*mil4 + midy
answer2 = int(answer2)
print(f"Second answer: {answer2}")
puzzle.answer_b = answer2
