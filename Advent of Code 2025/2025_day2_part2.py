with open('Advent of Code 2025/Puzzle_Inputs/2025_day2_puzzle_input.txt','r') as f:
  puzzle_id_ranges = ((f.read().replace('-',' '))).strip()
  puzzle_id_ranges = puzzle_id_ranges.split(',')
  id_ranges = []
  for i in puzzle_id_ranges:
    id_ranges.append(i.split(' '))
invalid_id_total = 0
for i in id_ranges:
  for num in range(int(i[0]), int(i[1])+1): #i[0] = lowerbound, (i[1]+1) = upperbound
    num = str(num)
    for i in range(1,len(num)):
      if i == 1:
        if num[0] * len(num) == num:
          invalid_id_total += int(num)
          break
      if num[:i] * (len(num) // i) == num:
        invalid_id_total += int(num)
        break

print(invalid_id_total)
#very slow