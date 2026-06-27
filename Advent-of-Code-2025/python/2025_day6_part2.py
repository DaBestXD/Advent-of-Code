with open("./puzzle_inputs/2025_day6_input.txt", "r") as f:
    temp: list[list[str]] = [list(n.replace("\n", "")) for n in f]
    divisors: list[list[int, str]] = [
        [idx, op] for idx, op in enumerate(temp[-1]) if op != " "
    ]
    formatted_list = []
    for row_len in range(0, len(temp[0])):
        column = []
        for i in temp[:-1]:
            column.append(i[row_len])
        formatted_list.append(column)
    opps = []
    for idx, num in enumerate(formatted_list):
        clean_num = "".join(num).replace(" ", "")
        if clean_num.isdigit():
            opps.append(clean_num)
        else:
            opps.append(divisors[0][1])
            divisors.pop(0)
        if idx + 1 == len(formatted_list):
            opps.append(divisors[0][1])
    temp = ""
    sum = 0
    for num in opps:
        if num.isdigit():
            temp += num + " "
        else:
            opperator = num
            sum += eval(temp.rstrip().replace(" ", opperator))
            temp = ""
    print(sum)
