# press F5 to copy this to a day file
from get_src import *
inp = get()

n = 50
part_a = 0
part_b = 0
for i in inp.splitlines():
    d = i[0]
    l = int(i[1:])
    if d == "L":
        l *= -1
    prev_n = n
    n = n + l

    while n < 0:
        if prev_n != 0:
            part_b += 1
        prev_n = n
        n += 100

    while n > 100:
        part_b += 1
        n -= 100

    if n == 0 or n == 100:
        part_a += 1
        part_b += 1
        n = 0

print(part_a)
print(part_b)
