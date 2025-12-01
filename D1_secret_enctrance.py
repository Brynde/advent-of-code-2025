with open('./advent-of-code-2025/D1_input.txt', 'r') as f:
    rotations_raw = f.read()

rotations = [r.strip() for r in rotations_raw.split() if r.strip()]
dial = 50
counter = 0
for rotation in rotations:
    if rotation[0] == 'R':
        steps = int(rotation[1:])
        dial = (dial + steps) % 100
    else:
        steps = int(rotation[1:])
        dial = (dial - steps) % 100

    if dial == 0:
        counter += 1

print(counter)