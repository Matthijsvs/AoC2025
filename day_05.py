from get_src import *


def merge_ranges(ranges):
    #https://codereview.stackexchange.com/questions/21307/consolidate-list-of-ranges-that-overlap?rq=1
    ranges = iter(sorted(ranges))
    current_start, current_stop = next(ranges)
    for start, stop in ranges:
        if start > current_stop:
            # Gap between segments: output current segment and start a new one.
            yield current_start, current_stop
            current_start, current_stop = start, stop
        else:
            # Segments adjacent or overlapping: merge.
            current_stop = max(current_stop, stop)
    yield current_start, current_stop

inp = get()
fresh=[]
part_a=0
for i in inp.splitlines():
    if "-" in i:
        start,end=i.split("-")
        fresh.append((int(start),int(end)))
    else:
        if i:
            ingredient=int(i)
            for j in fresh:
                start,end=j
                if ingredient>=start and ingredient<=end:
                    part_a+=1
                    break

print(part_a)
t2 = merge_ranges(fresh)
part_b = 0
for start,stop in t2:
    part_b+=stop-start+1
print(part_b)