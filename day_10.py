from get_src import *
from sympy import symbols, Eq, solve,linsolve,solveset

sample = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
[#####.#] (2,4,5,6) (0,1,4,5) (0,1,2,3,4,5) (1,3,5,6) (0,1,2,4,6) (1,3,6) (0,1,5,6) {49,71,32,29,52,70,63}
"""
def bitfield(n,d):
    s = bin(n)[2:].zfill(d)
    return [int(digit) for digit in s] # [2:] to chop off the "0b" part

def clean(x):
    x = x.strip("(){}")
    return list(map(int,x.split(",")))

inp = get(sample)
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
        #print(b,end="")
        for switch in range(len(b)):
            if b[switch]==1:
                #switch is touched
                for j in buttons[switch]:
                    #print(f"toggling {j}")
                    state[j]= not state[j]
        #print(state)
        if state == indicators:
            #print("-->",b)
            ans.append(sum(b))
    part_a+=min(ans)
    #--------------------------------- part b
    print(jolts,buttons)
    joltage = 0
    for j in jolts[::-1]:
        joltage = joltage * 1000 + j
    print(joltage)

    bs = []
    for x in buttons:
        y = 0
        for z in x:
            y+=1000**z
        bs.append(y)

    bs.extend([0]*10)

    x1,x2,x3,x4,x5,x6,x7,x8,x9,x10 = symbols('x0:10')

    equation = [x1*bs[0]+x2*bs[1]+x3*bs[2]+x4*bs[3]+x5*bs[4]+x6*bs[5]+x7*bs[6]- joltage]
    print(linsolve(equation,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10))
    print("-----------")

print(part_a)