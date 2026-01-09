import time
import heapq

start = time.time()
with open("./puzzle_inputs/input.txt") as f:
    coordinates = [tuple(map(int, num.strip().split(","))) for num in f.readlines()]


def get_distance(crd_one: tuple, crd_two: tuple) -> float:
    dis = (
        (crd_one[0] - crd_two[0]) ** 2
        + (crd_one[1] - crd_two[1]) ** 2
        + (crd_one[2] - crd_two[2]) ** 2
    )
    return dis


def main():
    sorted_dis = []
    for idx, coord in enumerate(coordinates):
        for compare in coordinates[idx + 1 :]:
            dis = get_distance(coord, compare)
            heapq.heappush(sorted_dis, (dis, {coord, compare}))
    cir = []
    _, c = heapq.heappop(sorted_dis)
    cir.append(c)
    while sorted_dis:
        merge = False
        _, c = heapq.heappop(sorted_dis)
        for k in cir:
            if c & k:
                k |= c
                merge = True
        if not merge:
            cir.append(c)
        for idx, k in enumerate(cir):
            for p in cir[idx + 1 :]:
                if k & p:
                    k |= p
                    cir.remove(p)
        if len(cir[0]) == len(coordinates):
            c1, c2 = c
            print(f"{c1[0] * c2[0]}")
            break
    print(f"Took {round(time.time() - start, 4)} seconds")


if __name__ == "__main__":
    main()
