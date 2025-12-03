from get_src import *

def get_jolts(battery_list, max):
    curr_num = ""                           #result
    battery_list_remaining=battery_list     #battery list from last chosen number
    while len(curr_num)<max:
        todo=max-len(curr_num)              #number of digits we still need

        biggest_number = list(battery_list_remaining[:len(battery_list_remaining)+1-todo])
        biggest_number.sort(reverse=True)
        next = battery_list_remaining.index(biggest_number[0])
        curr_num+=battery_list_remaining[next]

    return int(curr_num)



inp = get()
part_a=0
part_b=0
for i in inp.splitlines():
    part_a += get_jolts(i, 2)
    part_b += get_jolts(i,12)

print(part_a)
print(part_b)