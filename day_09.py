from get_src import *
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

inp = get()
coords = []
for i in inp.splitlines():
    x,y=i.split(",")
    coords.append(Point(int(x),int(y)))

polygon = Polygon(coords)
with open('day_09.svg', 'w') as f:
    f.write(polygon._repr_svg_())

def dist(a,b):
    area = (abs(coords[a].x-coords[b].x)+1)*(abs(coords[a].y-coords[b].y)+1)
    return int(area)

dist_list=[]
for i in range(len(coords)):
    min_dist = 1e9
    for j in range(i + 1, len(coords)):
        distance = dist(i, j)
        dist_list.append((distance, i,j))
        if distance < min_dist:
            min_dist = distance
dist_list.sort(reverse=True)  # sort tuples by biggest area

print(dist_list[0][0])

while True:
    area,start,end = dist_list.pop(0)
    start = coords[start]
    end = coords[end]
    t = Polygon([(start.x,start.y),(end.x,start.y),(end.x,end.y),(start.x,end.y)])

    if polygon.covers(t):
        print(area)
        break
