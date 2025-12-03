from get_src import *
import re

sample = """987654321111111
811111111111119
234234234234278
818181911112111
"""


def get_jolts(s,max):
    #we take this battery
    opts=[]
    maxnum=0
    for i in range(9,0,-1):
        print(f"start with {i}")
        start = [m.start() for m in re.finditer(str(i), s)]
        for j in start:
            if j<=len(s)-max:
                print(f"begin with the {i} on position {j}")

    opts=list(opts)
    opts.sort(reverse=True)
    print(opts)

    for i in opts:
        if len(i)==max:
            print(i,len(i))
            return int(i)



inp = get(sample)
part_a=0
for i in inp.splitlines():
    part_a+=get_jolts(i,12)
    """max1=0
    j = list(i)
    j.sort(reverse=True)
    while j:
        largest=j.pop(0)
        pos = i.index(largest)
        for n in range(pos+1,len(i)):
            t = int(i[pos]+i[n])

            if t>max1:
                max1=t
    part_a+=max1
    """

print()
print(part_a)