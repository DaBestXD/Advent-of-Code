import math
#combine all combos into one string
combo = ''
with open('dialcombos.txt', 'r') as file:
  for line in file:
    combo += line.rstrip()

string_combo = 'R1000L1000L50R1L1L1R1R100R1'
#'L68L30R48L5R60L55L1L99R14L82'
#
direction = ''
dial = []
value = 50 #starting value
count = 0
for i in range(0,100):
  dial.append(i)
clean_list = []
charToNum = ''
for i in range(0,len(combo)):
  char = string_combo[i]
  if (char == 'R' or char =='L'):
    clean_list.append((char))
    charToNum = ''
  else:
    charToNum += char
    if i + 1 < len(string_combo):
      if string_combo[i +1] == 'R' or string_combo[i +1] == 'L':
        clean_list.append(int(charToNum))
    else:
      clean_list.append(int(charToNum))


for i in clean_list:
  if type(i) is str:
    direction = i
    continue
  movement = i if direction == 'R' else -i
  total_move = movement + value
  if total_move > len(dial) - 1:
    count += math.ceil(i / len(dial))
    total_move = dial[((total_move) % len(dial))]
  if direction == "L":
    if value <= i:
      count += math.ceil(i / len(dial))
      if value == 0:
        count -=1
      total_move = dial[((total_move) % len(dial))]
  value = dial[total_move]

  print(f'Currently at {dial[value]}, {direction}:{i}, zeros: {count}, total move {total_move}')

print(f'total zero count: {count}')