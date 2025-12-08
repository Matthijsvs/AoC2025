from get_src import *
import math

inp = get()

coords = []
for i in inp.splitlines():
    x,y,z=i.split(",")
    coords.append((int(x),int(y),int(z)))

def dist(a,b):
    d = math.sqrt((coords[b][0] - coords[a][0])**2 + (coords[b][1] - coords[a][1])**2 + (coords[b][2] - coords[a][2])**2)
    return d

pairs = []
dist_list=[]
for i in range(len(coords)):
    min_dist = 1e9
    p = -1
    for j in range(i+1,len(coords)):
        if i!=j:
            s = dist(i,j)
            dist_list.append((s,i,j))
            if s<min_dist:
                min_dist=s
                p = j
    if i!=j:
        pairs.append((i,p))
dist_list.sort()


groups=[[x] for x in range(len(inp.splitlines()))]
conns=0
while conns<1000:
    i = dist_list.pop(0)
    distance,a,b=i
    for x in range(len(groups)):
        j = groups[x]
        if a in j and b in j:
            conns+=1
            break
        elif a in j:
            for y in groups:
                if b in y:
                    j.extend(y)
                    groups.remove(y)
                    break
            conns += 1
            break
        elif b in j:
            for y in groups:
                if a in y:
                    j.extend(y)
                    groups.remove(y)
                    break
            conns += 1
            break
sizes=[]
for j in groups:
    sizes.append(len(set(j)))
sizes.sort(reverse=True)
print(math.prod(sizes[:3]))

#continue until list is empty
while len(groups)>1:
    i = dist_list.pop(0)
    distance,a,b=i
    sum_b=coords[a][0]*coords[b][0]
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

print(sum_b)
