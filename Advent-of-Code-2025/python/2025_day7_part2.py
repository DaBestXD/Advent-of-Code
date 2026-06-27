import time

start = time.time()
with open("./puzzle_inputs/2025_day7_input.txt", "r") as f:
    lines: list[list[str]] = [list(line.strip()) for line in f]
    laser_positions = [0] * len(lines[0])
    laser_positions[lines[0].index("S")] = 1

for k, row in enumerate(lines):
    for idx, item in enumerate(row):
        if item == "^" and laser_positions[idx] > 0:
            if laser_positions[idx] > 1:
                laser_positions[idx - 1] += laser_positions[idx]
                laser_positions[idx + 1] += laser_positions[idx]
            else:
                laser_positions[idx - 1] += 1
                laser_positions[idx + 1] += 1
            laser_positions[idx] = 0
print(sum(laser_positions))
# :/ didnt like this one... looked up solution....
# .......|....... cur paths = 1
# .......|.......
# ......|^|...... cur paths = 2
# ......|.|......
# .....|^|^|..... cur paths = 4
# .....|.|.|.....
# ....|^|^|^|.... cur paths = 10
# ....|.|.|.|....
# ...|^|^|||^|...
# ...|.|.|||.|...
# ..|^|^|||^|^|..
# ..|.|.|||.|.|..
# .|^|||^||.||^|.
# .|.|||.||.||.|.
# |^|^|^|^|^|||^|
# |.|.|.|.|.|||.|
