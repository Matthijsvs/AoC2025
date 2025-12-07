from get_src import *
inp = get_grid()

beam_count = [0]*len(inp[0])

for x in range(len(inp[0])):
    for y in range(len(inp)):
        if inp[y][x]=="S":
            beam_count[x] = 1
            break

split=0
for y in range(len(inp)):
    for x in range(len(inp[0])):
        if inp[y][x]=="^":
            if beam_count[x]>0:
                split+=1
                beam_count[x-1] += beam_count[x]
                beam_count[x+1] += beam_count[x]
                beam_count[x] =0

print(f"part_a:{split}")
print(f"part_b:{sum(beam_count)}")
