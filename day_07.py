import copy
from get_src import *

inp = get_grid()

beams=[]
for x in range(len(inp[0])):
    for y in range(len(inp)):
        if inp[y][x]=="S":
            beams.append(Point(x,y))
            start=Point(x,y)
            break

beam_count = [0]*len(inp[0])
beam_count[start.x]=1
split=0
for y in range(len(inp)):
    new_count = copy.deepcopy(beam_count)
    for x in range(len(inp[0])):

        if inp[y][x]=="^":
            if beam_count[x]>0:
                split+=1
                new_count[x-1] += new_count[x]
                new_count[x+1] += new_count[x]
                new_count[x] =0
    beam_count=new_count

print(f"part_a:{split}")
print(f"part_b:{sum(beam_count)}")
