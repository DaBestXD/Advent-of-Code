file_path = 'Advent of Code 2025/Puzzle_Inputs/'
sample = '2025_day4_sample_input.txt'
real = '2025_day4_puzzle_input.txt'
dataset = real
with open(f'{file_path}{dataset}','r') as f:
    row = [row.rstrip() for row in f]
    paper_tower = {k:v for (k,v) in zip(range(0,len(row)),row)}
    del row
total = 0
tower_edge = len(paper_tower[0])
tower_bottom = len(paper_tower.keys())
coordinates = []
foo = []
def edge(column:int) -> slice:
    #left most edge
    if column == 0:
        return slice(column,column+2)
    #right most edge
    elif column+1 == tower_edge:
        return slice(column-1,column+1)
    return slice(column-1,column+2)
while True:
    temptotal = 0
    for row in paper_tower:
        for column, i in enumerate(paper_tower[row]):
            if paper_tower[row][column] == '@':
                column_slice = edge(column)
                paper_counter = 0 
                #only check right if not at the right most edge
                if column+1 < len(paper_tower):
                    if paper_tower[row][column + 1] == '@':
                        paper_counter += 1
                #only check left if not at left most edge
                if column - 1 >= 0 :
                    if paper_tower[row][column - 1] == '@':
                        paper_counter += 1
                #only check above if not at the top
                if row > 0:
                    #print([x for x in paper_tower[row - 1][column_slice]])
                    paper_counter += sum(x == '@' for x in paper_tower[row - 1][column_slice])
                #only check row below if not at the bottom
                if row+1 < tower_bottom:
                    #print([x for x in paper_tower[row + 1][column_slice]])
                    paper_counter += sum(x == '@' for x in paper_tower[row + 1][column_slice])
                foo.append(paper_counter)
                if paper_counter < 4:
                    coordinates.append([row, column])
                    temptotal +=1
    for i in coordinates:
        temp = [num for num in paper_tower[i[0]]]
        temp[i[1]] = '.'
        paper_tower.update({i[0] : ''.join(temp)})
    total += temptotal
    #if total + temptotal == total, no change occured break and print total
    if total + temptotal == total:
        print(total)
        break


