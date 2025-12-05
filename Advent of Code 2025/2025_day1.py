combo = []
with open('dialcombos.txt', 'r') as file:
  for line in file:
    combo.append(line.rstrip())
sample_1 = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82']
pointer = 50 #starting value
zeroCounter = 0
for i in sample_1:
  direction = -1 if i[0] == 'L' else 1
  stepAmount = int(i[1:]) 
  absMove = pointer + stepAmount
  if absMove >= 100 and direction > 0:
    zeroCounter += absMove // 100

  if pointer - stepAmount <= 0 and direction < 0:
    #single rotation check only increment if non zero number 
    if stepAmount < 100 and pointer !=0:
      zeroCounter +=1
    #multi rotation check
    if stepAmount >= 100:
      if pointer - (stepAmount % 100) > 0:
        zeroCounter += stepAmount // 100
      else:
        zeroCounter += (stepAmount//100)
        if(pointer != 0):
          zeroCounter+=1

  pointer = (pointer +(direction * stepAmount)) % 100

print(f'Num zeros: {zeroCounter}')

#correct 6695



