import time

start = time.time()
with open("./puzzle_inputs/2025_day9_input.txt", "r") as f:
    rectangle_corners = [
        list(map(int, cord.strip().split(","))) for cord in f.readlines()
    ]


def main():
    max = 0
    for idx, cord in enumerate(rectangle_corners):
        x = cord[0]
        y = cord[1]
        if idx + 1 < len(rectangle_corners):
            for i in rectangle_corners:
                if cord != i:
                    x2 = i[0]
                    y2 = i[1]
                    area = (abs(x2 - x) + 1) * (abs(y2 - y) + 1)
                    max = area if area > max else max
    print(max)


if __name__ == "__main__":
    main()
