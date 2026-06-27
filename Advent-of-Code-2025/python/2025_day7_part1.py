with open("./puzzle_inputs/2025_day7_input.txt", "r") as f:
    lines: list[list[str]] = [list(line.strip()) for line in f]
    laser_positions: list[int] = [lines[0].index("S")]

split_count = 0
for row in lines[1:-1]:
    for idx, item in enumerate(row):
        if item == "^" and idx in laser_positions:
            split_count += 1
            row[idx + 1] = "|"
            row[idx - 1] = "|"
            laser_positions.remove(idx)
            if idx + 1 not in laser_positions:
                laser_positions.append(idx + 1)
            if idx - 1 not in laser_positions:
                laser_positions.append(idx - 1)

        elif idx in laser_positions:
            row[idx] = "|"
    print("".join(row), laser_positions, split_count)

print(split_count)
# not efficient at all....
