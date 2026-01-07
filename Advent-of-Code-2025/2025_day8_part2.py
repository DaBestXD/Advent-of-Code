import time

start = time.time()
with open("./puzzle_inputs/input.txt") as f:
    coordinates = [tuple(map(int, num.strip().split(","))) for num in f.readlines()]


def get_distance(crd_one: tuple, crd_two: tuple) -> float:
    dis = (
        pow(crd_one[0] - crd_two[0], 2)
        + pow(crd_one[1] - crd_two[1], 2)
        + pow(crd_one[2] - crd_two[2], 2)
    )
    return dis


def main():
    sorted_dis = []
    junction_boxes = {}
    for idx, coord in enumerate(coordinates):
        junction_boxes[coord] = idx
        for compare in coordinates[idx + 1 :]:
            dis = get_distance(coord, compare)
            sorted_dis.append((dis, coord, compare))
    sorted_dis.sort()
    idx = 0
    while junction_boxes:
        _, first_cord, second_cord = sorted_dis[idx]
        idx += 1
        if len(junction_boxes) == 1:
            break
        if first_cord in junction_boxes:
            del junction_boxes[first_cord]
        elif second_cord in junction_boxes:
            del junction_boxes[second_cord]
    print(first_cord[0] * second_cord[0], first_cord, second_cord, idx)
    print(f"Took {round(time.time() - start, 4)} seconds")


if __name__ == "__main__":
    main()
