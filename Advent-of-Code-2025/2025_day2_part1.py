with open('Advent of Code 2025/Puzzle_Inputs/2025_day2_puzzle_input.txt','r') as f:
  puzzle_id_ranges = f.read().replace('-',' ')
  puzzle_id_ranges = puzzle_id_ranges.split(',')
  id_ranges = []
  for i in puzzle_id_ranges:
    id_ranges.append(i.split(' '))
#id_ranges = [[1,11]]
invalid_id_total = 0
for i in id_ranges:
  for num in range(int(i[0]), int(i[1])+1): #i[0] = lowerbound, (i[1]+1) = upperbound
    num = str(num)
    if len(num) % 2 == 0:
      midpoint = int(len(num) / 2)
      if num[:midpoint] == num[midpoint:]:
        invalid_id_total += int(num)


print(invalid_id_total)