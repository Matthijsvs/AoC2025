from get_src import *
from itertools import groupby

inp = get()

#https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-equal
def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def split(txt, n):
    for i in range(0, len(txt), n): #split string in parts of length n
        yield(int(txt[i:i + n]))

def invalid_part_a(num):
    n=str(num)
    half=len(n)//2
    return n[:half]==n[half:]

def invalid_part_b(num):
    n=str(num)
    for div in range(1,len(n)//2+1):
        opts = split(n,div)
        if all_equal(opts):
            return True

part_a=0
part_b=0
for i in inp.split(","):
    a,b=i.split("-")
    #print(i)
    for j in range(int(a),int(b)+1):
        if invalid_part_a(j):
            part_a+=int(j)
        if invalid_part_b(j):
            part_b+=int(j)

print(part_a)
print(part_b)