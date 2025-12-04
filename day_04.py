from get_src import *

inp = get_grid()
max_x = len(inp[0])
max_y = len(inp)

def get_remove_list():
    l=[]
    for x in range(len(inp[0])):
        for y in range(len(inp)):
            if inp[y][x]=="@":
                blocked = 0
                for d in dirs8:
                    newx=x+d[0]
                    newy=y+d[1]
                    if newy>=0 and newy<max_y and newx >= 0 and newx<max_x:
                        if inp[newy][newx]=="@":
                            blocked=blocked+1
                if blocked<4:
                    l.append(Point(x,y))
    return l

def do_remove(l):
    for i in l:
        inp[i.y][i.x]="_"


part_a=len(get_remove_list())
print(part_a)

part_b=0
amount=1
while amount>0:
    l = get_remove_list()
    amount = len(l)
    part_b+=amount
    #print(f"remove {amount}")
    do_remove(l)

print(part_b)