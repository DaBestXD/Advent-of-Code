import math
import time

start = time.time()
# with open("./puzzle_inputs/2025_day8_input.txt") as f:
with open("./puzzle_inputs/2025_day8_input_s.txt") as f:
    coordinates = [tuple(map(int, num.strip().split(","))) for num in f.readlines()]


def distance(coord_one: tuple, coord_two: tuple) -> float:
    dis = round(
        math.sqrt(
            pow(coord_one[0] - coord_two[0], 2)
            + pow(coord_one[1] - coord_two[1], 2)
            + pow(coord_one[2] - coord_two[2], 2)
        ),
        2,
    )
    return dis


def main():
    temp = []
    # coordinate? Aot reference😼
    for coord in coordinates:
        distances = {}
        for compare in coordinates:
            if coord != compare:
                dis = distance(coord, compare)
                distances[dis] = sorted((coord, compare))
        sorted_dis = {leng: distances[leng] for leng in sorted(distances.keys())}
        temp.append(sorted_dis)
    # very readable! great variable names!
    shortest_ten = sorted(
        set([(num, tuple(outer[num])) for outer in temp for num in outer.keys()])
    )[:10]
    # for i in shortest_ten:
    #     print(i)
    print(len(shortest_ten))
    circuits = []
    while True:
        start_len = (circuits).copy()
        for dis, i in shortest_ten:
            set_i = set(i)
            connected = False
            if not circuits:
                circuits.append(set_i)
                continue
            for idx, k in enumerate(circuits):
                set_k = set(k)
                if set_k.intersection(set_i):
                    circuits[idx] = set_k.union(set_i)
                    connected = True
                    break
            if not connected:
                circuits.append(set_i)
        for idx, cir in enumerate(circuits):
            for comp in circuits:
                if cir & comp and cir != comp:
                    circuits[idx] = cir | comp
                    try:
                        circuits.remove(comp)
                    except ValueError:
                        pass
        if circuits == start_len:
            break
    total = 1
    for cir in sorted(circuits, key=len, reverse=True)[:5]:
        print(cir)
        total *= len(cir)
    print(total)
    print(f"Took {round(time.time() - start, 4)} seconds")


if __name__ == "__main__":
    main()
