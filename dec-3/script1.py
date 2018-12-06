from collections import defaultdict

data = open('input.txt').read().splitlines()

def parse(line):
    claim, _, dimension, offset = line.split()
    claim = claim[1:]
    x, y = dimension[:-1].split(',')
    width, height = offset.split('x')
    return int(claim), int(x), int(y), int(width), int(height)


overlap = defaultdict(int)
for line in data:
    claim, x, y, width, height = parse(line)
    for xi in range(width):
        for yi in range(height):
            overlap[(x+xi, y+yi)] += 1

print(len([v for k,v in overlap.items() if v > 1]))