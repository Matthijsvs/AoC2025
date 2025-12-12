from get_src import *
from pulp import *

def bitfield(n,d):
    s = bin(n)[2:].zfill(d)
    return [int(digit) for digit in s] # [2:] to chop off the "0b" part

def clean(x):
    x = x.strip("(){}")     #returns a python list of a string between brackets
    return list(map(int,x.split(",")))

inp = get()
part_a=0
part_b=0
for i in inp.splitlines():
    buttons = i.split(" ")
    indicators = [True if x =="#" else False for x in buttons.pop(0)[1:-1]]
    jolts = clean(buttons.pop(-1))
    #--------------------------------- part a
    buttons = list(map(clean, buttons))

    m = 2**len(buttons)
    ans = []
    for possib in range(m):
        state = [False for x in indicators]
        b = bitfield(possib, len(buttons))
        for switch in range(len(b)):
            if b[switch]==1:     #switch is touched
                for j in buttons[switch]:
                    state[j]= not state[j]  #toggle state
        if state == indicators:
            ans.append(sum(b))  #array of 0/1 so sum is equal to number of 1 bits
    part_a+=min(ans)
    #--------------------------------- part b
    prob = LpProblem("The_Button_Problem", LpMinimize)
    butt = [f"B{x}" for x in range(len(buttons))]
    button_vars = LpVariable.dicts("Press", butt, 0, 300, LpInteger)
    prob += (
        lpSum([button_vars[i] for i in butt]), "total presses")
    t = []
    for j in range(len(jolts)):
        ex = []
        for b in buttons:
            if j in b:
                ex.append(f"B{buttons.index(b)}")
        prob += (lpSum([1 * button_vars[i] for i in ex]) == jolts[j], f"requiredJolts{j}")
    prob.solve()
    part_b+=int(value(prob.objective))
    print("-------------------")
print(part_a)
print(part_b)
