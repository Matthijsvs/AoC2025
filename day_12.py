from get_src import *

regions = []
shapes=[]
inp = get()
for i in inp.splitlines():
    if "x" in i:
        size,packs = i.split(":")
        x,y=size.split("x")
        packs = list(map(int,packs.split()))
        regions.append((int(x),int(y),packs))
    elif ":" in i:
        shapes.append([])
    elif i:
        shapes[-1].append(list(i))

part_a=0
for i in regions:
    #print(i)
    x,y,size=i
    #print(f"we have a {x}x{y}={x*y} grid")
    needed=0
    for j in range(len(size)):
        if size[j]>0:
            #print(f"we need {size[j]} of shape {j}")
            blocks=0
            for yz in range(len(shapes[j])):
                blocks+=shapes[j][yz].count("#")
            #print(f"shape{j} has {blocks} ")
            needed += blocks*size[j]
    #print(f"we need to have {needed} blocks")
    if needed <= x*y*0.85:
        part_a+=1
print(part_a)