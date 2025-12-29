combo = []
with open('Advent of Code 2025/Puzzle_Inputs/2025_day1_puzzle_input.txt', 'r') as file:
  for line in file:
    combo.append(line.rstrip())

value = 50
zero = 0
for i in combo:
  direction = -1 if i[0] == 'L' else 1
  turnNum = int(i[1:])
  absValue = turnNum + value
  value += (direction *turnNum)
  if value >= 100 or value <= 0:
    value %=100
  if value ==0:
    zero +=1

print(f'Num zeros: {zero}')