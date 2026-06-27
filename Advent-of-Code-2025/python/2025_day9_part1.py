import time

start = time.time()
with open("./puzzle_inputs/2025_day9_input.txt", "r") as f:
    rectangle_corners = [
        list(map(int, cord.rstrip().split(","))) for cord in f.readlines()
    ]


def main():
    max = 0
    for idx, (x, y) in enumerate(rectangle_corners):
        for x2, y2 in rectangle_corners[idx + 1 :]:
            area = (abs(x2 - x) + 1) * (abs(y2 - y) + 1)
            max = area if area > max else max
    print(max)
    print(f"Took {(time.time() - start):.4f} seconds")


if __name__ == "__main__":
    main()
