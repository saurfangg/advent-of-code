

data = [x.strip() for x in open("input.txt").readlines()]

for x in data:
    for y in data:
        difference = [i for i, j in zip(x,y) if i == j]
        if len(y) - len(difference) == 1:
            print("".join(difference))
            break