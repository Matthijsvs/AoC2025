from get_src import *
from shapely.geometry.polygon import Polygon

inp = get()
coords = []
for i in inp.splitlines():
    x,y=list(map(int,i.split(",")))
    coords.append(Point(x,y))

polygon = Polygon(coords)
#with open('day_09.svg', 'w') as f:
#    f.write(polygon._repr_svg_())

def calc_area(a, b):
    area = (abs(a.x-b.x)+1)*(abs(a.y-b.y)+1)
    return int(area)

area_list=[]
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        start=coords[i]
        end =coords[j]
        area_list.append((calc_area(start, end), start, end))
area_list.sort(reverse=True)  # sort tuples by biggest area

print(area_list[0][0])

while True:
    area,start,end = area_list.pop(0)
    t = Polygon([(start.x,start.y),(end.x,start.y),(end.x,end.y),(start.x,end.y)])

    if polygon.covers(t):
        print(area)
        break
