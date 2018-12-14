with open('input.txt', 'r') as f:
    original_data = f.read().strip()

alphabet = "abcdefghijklmnopqrstuvwxyz"
pairs = [c + c.upper() for c in alphabet]
pairs += [c.upper() + c for c in alphabet]

def remove_polar_opposites(chain):
    for pair in pairs:
        chain = chain.replace(pair, '')
    return chain

def full_polar_removal(chain):
    previous_string = data
    current_string = data

    while True:
        current_string = remove_polar_opposites(previous_string)
        if current_string == previous_string:
            break
        previous_string = current_string
    return current_string

lengths = []

for character in alphabet:
    data = original_data
    data = data.replace(character, "")
    data = data.replace(character.upper(), "")
    lengths.append(len(full_polar_removal(data)))

print(min(lengths))
