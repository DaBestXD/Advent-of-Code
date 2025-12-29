file_path = 'Advent of Code 2025/Puzzle_Inputs/'
sample = '2025_day3_sample_input.txt'
real = '2025_day3_puzzle_input.txt'
dataset = sample
bat_list = []
with open(f'{file_path}{dataset}','r') as f:
  for i in f:
    bat_list.append([int(num) for num in i.rstrip()])

sum = 0
for bat_row in bat_list:
  digits = []
  starting_idx = 0
  for i in range(0,12):
    test = 0
    for idx in range(0,len(bat_row)):
      if test < bat_row[idx] and idx + (12-len(digits)) <= len(bat_row):
        starting_idx = idx
        test = bat_row[idx]
    digits.append(str(test))
    bat_row = bat_row[starting_idx+1:]
    #TODO change from creating copy to slicing og list
  sum += int(''.join(digits))

print(sum) 






