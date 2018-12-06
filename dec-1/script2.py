import itertools

data = [int(x) for x in open("input.txt").readlines()]

frequency = 0
seen = {0}

for num in itertools.cycle(data):
    frequency += num
    if frequency in seen:
        print(frequency); break
    seen.add(frequency)
