import time

start = time.time()
with open("puzzle_inputs/2025_day5_input.txt", "r") as f:
    raw = [(num.rstrip().replace("-", " ")) for num in f]
    str_range = [num.split(" ") for num in raw[: raw.index("")]]
    num_range = [[int(num[0]), int(num[1])] for num in str_range]
    num_range.sort()
sum = 0
for idx, ranges in enumerate(num_range):
    local_max = ranges[1]
    local_min = ranges[0]
    removal_list = []
    for compare in num_range:
        if local_min <= compare[1] and local_max >= compare[0]:
            removal_list.append(compare)
            local_min = compare[0] if compare[0] <= local_min else local_min
            local_max = compare[1] if compare[1] >= local_max else local_max
    for items in removal_list:
        num_range.remove(items)
    num_range.insert(idx, [local_min, local_max])
for num in num_range:
    sum += (num[1] - num[0]) + 1

print(f"Sum: {sum}, {round(time.time() - start, 6)}")
