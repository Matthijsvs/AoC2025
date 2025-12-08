from get_src import *
import math

inp = get()

coords = []
for i in inp.splitlines():
    x,y,z=list(map(int,i.split(",")))
    coords.append(Point3(x,y,z))

def dist(a,b):
    d = math.sqrt((coords[b].x - coords[a].x)**2 + (coords[b].y - coords[a].y)**2 + (coords[b].z - coords[a].z)**2)
    return d

#build distance list
dist_list=[]

for i in range(len(coords)):
    min_dist = 1e9
    for j in range(i+1,len(coords)):
        distance = dist(i, j)
        dist_list.append((distance, i, j))
        if distance<min_dist:
            min_dist=distance
dist_list.sort()    #sort tuples by lowest distance


#every junction is its own group
groups=[[x] for x in range(len(inp.splitlines()))]

def make_connection():
    i = dist_list.pop(0)    #take current lowest distance
    _, a, b = i
    x_product = coords[a].x * coords[b].x
    for x in range(len(groups)):
        j = groups[x]
        if a in j and b in j:
            break
        elif a in j:
            for y in groups:
                if b in y:
                    j.extend(y)
                    groups.remove(y)
                    break
            break
        elif b in j:
            for y in groups:
                if a in y:
                    j.extend(y)
                    groups.remove(y)
                    break
            break
    return x_product

#first connect 1000 junctions:
for i in range(1000):
    make_connection()
group_size = [len(x) for x in groups]
group_size.sort(reverse=True)
print(math.prod(group_size[:3]))

#continue until all junctions are connected
while len(groups)>1:
    sum_b = make_connection()
print(sum_b)
