with open("./puzzle_inputs/2025_day7_input_s.txt", "r") as f:
    lines: list[list[str]] = [list(line.strip()) for line in f]
    # laser_positions: list[int] = [lines[0].index("S")]
print(lines)

# init laser pos [7]
# .....|^|^|.....
# go through row . -> . -> . -> if idx in laser_positions set to "|"
# and idx not = "^"
# if laser is "^" then remove the current laser then append laser-1,laser+1
