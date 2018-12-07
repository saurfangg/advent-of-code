from collections import Counter

data = [x.strip() for x in open("input.txt").readlines()]

twos, threes = 0, 0

for id in data:
    counts = Counter(Counter(id).values())
    if 2 in counts:
        twos += 1
    if 3 in counts:
        threes += 1
print(twos*threes)
