from get_src import *
inp = get()

n = 50                  #start position
part_a = 0
part_b = 0
for i in inp.splitlines():
    d = i[0]            #direction of step
    l = int(i[1:])      #length of step
    if d == "L":
        l *= -1
    prev_n = n
    n = n + l

    while n < 0:
        if prev_n != 0:     #underflow starting from zero, don't count again
            part_b += 1
        prev_n = n
        n += 100

    while n > 100:          #overflow ends on 100, don't count again
        part_b += 1
        n -= 100

    if n == 0 or n == 100:
        part_a += 1
        part_b += 1
        n = 0

print(part_a)
print(part_b)
