with open("puzzle_inputs/2025_day5_input.txt", "r") as f:
    raw = [(num.rstrip().replace("-", " ")) for num in f]
    empty = raw.index("")
    num_range = [num.split(" ") for num in raw[:empty]]
    food_ids = [int(num) for num in raw[empty + 1 :]]

count = 0
for i in food_ids:
    for j in num_range:
        if int(j[0]) <= i <= int(j[1]):
            count += 1
            break
print(count)
