from get_src import *
import math

inp = get()
nums=[]
cep_nums=[[]]
ops=[]

for i in inp.splitlines():
    if not i.startswith("*"):
        txt = i.split()
        nums.append(list(map(int,txt)))
    else:
        ops=i.split()
nums = list(map(list, zip(*nums))) #transpose

l = len(inp.splitlines()[0])
for i in range(l):
    cep = 0
    tmp=[]
    for j in inp.splitlines():
        if j[i].isdigit():
            cep = cep * 10
            cep += int(j[i])
    if cep>0:
        cep_nums[-1].append(cep)
    else:
        cep_nums.append([])


def do_math(arr):
    total=0
    for i in range(len(ops)):
        if ops[i]=="*":
            total+=math.prod(arr[i])
        elif ops[i]=="+":
            total+=sum(arr[i])
    return total

print(do_math(nums))
print(do_math(cep_nums))