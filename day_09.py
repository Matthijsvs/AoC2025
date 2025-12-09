from get_src import *
from shapely.geometry import Point,LineString
from shapely.geometry.polygon import Polygon


sample = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""
inp = get()
coords = []
lines=[]
for i in inp.splitlines():
    x,y=i.split(",")
    coords.append(Point(int(x),int(y)))

#coords.append(coords[0])
polygon = Polygon(coords)
#print(polygon.exterior)


def dist(a,b):
    area = abs(coords[a].x-coords[b].x+1)*abs(coords[a].y-coords[b].y+1)
    return int(area)

dist_list=[]
for i in range(len(coords)):
    min_dist = 1e9
    for j in range(i + 1, len(coords)):
        distance = dist(i, j)
        dist_list.append((distance, i,j))
        if distance < min_dist:
            min_dist = distance
dist_list.sort(reverse=True)  # sort tuples by lowest distance

print(dist_list[0])
#def pass_line(pt):

Found = False
while not Found:
    area,start,end = dist_list.pop(0)
    start = coords[start]
    end = coords[end]
    t = Polygon([(start.x,start.y),(end.x,start.y),(end.x,end.y),(start.x,end.y)])
    #print(t.within(polygon),t)
    if t.within(polygon):
        Found=True
print(area)
