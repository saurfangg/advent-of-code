import re
from collections import Counter

lines = [line.strip() for line in open('input.txt')]
lines.sort()

guards = {}

current_guard, start_time, end_time = 0, 0, 0

for line in lines:
    value = re.findall("\d+", line)
    if "Guard" in line:
        current_guard = int(value[-1])
    elif "falls asleep" in line:
        start_time = int(value[-1])
    elif "wakes up" in line:
        end_time = int(value[-1])
        for i in range(start_time, end_time):
            guards.setdefault(current_guard, []).append(i)

guard_id = max(guards, key=lambda x: len(guards[x]))
count = Counter(guards[guard_id])
minute = count.most_common()[0][0]
print(guard_id * minute)