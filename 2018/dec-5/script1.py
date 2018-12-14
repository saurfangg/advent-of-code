with open('input.txt', 'r') as f:
    data = f.read().strip()

alphabet = "abcdefghijklmnopqrstuvwxyz"
pairs = [c + c.upper() for c in alphabet]
pairs += [c.upper() + c for c in alphabet]

def remove_polar_opposites(chain):
    for pair in pairs:
        chain = chain.replace(pair, '')
    return chain

def full_polar_removal(chain):
    original_chain = data
    reduced_chain = data

    while True:
        reduced_chain = remove_polar_opposites(original_chain)
        if reduced_chain == original_chain:
            break
        original_chain = reduced_chain
    
    return reduced_chain

print(len(full_polar_removal(data)))