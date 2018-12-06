from collections import defaultdict

data = open('input.txt').read().splitlines()

def parse(line):
    claim, _, dimension, offset = line.split()
    claim = claim[1:]
    x, y = dimension[:-1].split(',')
    width, height = offset.split('x')
    return int(claim), int(x), int(y), int(width), int(height)

# Carried over from Part 1
overlap = defaultdict(int)
for row in data:
    num, x, y, w, h = parse(row)
    for xi in range(w):
        for yi in range(h):
            overlap[(x+xi, y+yi)] += 1

# Part 2
all_claims = set()
overlapping_claims = set()

for line in data:
    claim, x, y , width, height = parse(line)
    all_claims.add(claim)
    for xi in range(width):
        for yi in range(height):
            xy = (x+xi, y+yi)
            if overlap[xy] > 1:
                overlapping_claims.add(claim)

print(next(f for f in all_claims - overlapping_claims))