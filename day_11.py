from get_src import *
import math

sample = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""
inp = get()

class Cave():
    def __init__(self, n):
        self.name = n
        self.neigbors = []
        self.isend = (n == "out")
        self.isstart = (n == "svr")

    def add(self, n):
        self.neigbors.append(n)

    def visit(self, listing, end,maxdepth):
        # we are the end of the line, this route is valid
        if self.name==end:
            return 1

        if self.isstart and len(listing) > 0:
            return 0

        if self in listing:
            return 0

        # still not finished, visit all neighbours:
        g = 0
        newlist = []
        newlist.extend(listing)
        newlist.append(self)
        if len(newlist)<maxdepth:
            for n in self.neigbors:
                g += n.visit(newlist, end,maxdepth)
        return g

    def lpr(self, l):
        for i in l:
            print(i, end=',')
        print(self.name)

    def __repr__(self):
        return str(self.name)


cavelist = {}
for line in inp.splitlines():
    start,l = line.split(":")
    l = l.split(" ")
    if start not in cavelist:
        cavelist[start] = Cave(start)
    for end in l:
        if end and end not in cavelist:
            cavelist[end] = Cave(end)

for line in inp.splitlines():
    start,l = line.split(":")
    l = l.split(" ")
    for end in l:
        if end:
            cavelist[start].add(cavelist[end])

print(cavelist["you"].visit([],"out",10))   #PART A
p=[]
p.append(cavelist["svr"].visit([], "fft",12))
p.append(cavelist["fft"].visit([], "dac",18))
p.append(cavelist["dac"].visit([], "out",10))
print(math.prod(p)) #part b