bat_list = []
with open('Advent of Code 2025/Puzzle_Inputs/2025_day3_puzzle_input.txt','r') as f:
  for i in f:
    bat_list.append(i.rstrip())

temp_list=[]
for num in bat_list:
  num_row = []
  for i in num: num_row.append(int(i))
  temp_list.append(num_row)
sum = 0
bat_list = temp_list
for i in bat_list:
  max_idx = i.index(max(i))
  max_value = str(max(i))
  if max_idx == 0:
    sum += int(str(max(i)) + str(max(i[1:])))
    continue
  if max_idx == len(i) -1:
    sum += int(str(max(i[:max_idx])) + str(max(i)))
    continue
  left_max = int(str(max(i[:max_idx])) + max_value)
  right_max = int(max_value + str(max(i[max_idx+1:])))
  final_max = left_max if left_max >= right_max else right_max
  sum += final_max

print(sum)