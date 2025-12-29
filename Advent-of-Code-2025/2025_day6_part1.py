import time

start = time.time()
with open("./puzzle_inputs/2025_day6_input.txt", "r") as f:
    rows = [row.strip().split() for row in f]
    columns = []
    for idx in range(0, len(rows[0])):
        column = []
        for i in rows:
            column.append(i[idx])
        columns.append(column)
total = 0
for nums in columns:
    operator = nums[-1]
    sum = int(nums[0])
    for i in nums[1:]:
        if i.isdigit():
            sum = eval(f"{sum} {operator} {i}")
    total += sum

print(total)
