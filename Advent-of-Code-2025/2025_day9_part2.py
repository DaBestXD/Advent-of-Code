import time
import heapq

start = time.time()
with open("./puzzle_inputs/testinput.txt", "r") as f:
    cords = sorted(
        [list(map(int, _.strip().split(","))) for _ in f.readlines()],
        key=lambda _: _[1],
    )
    horizontal_lines = {}
    area_heap = []
    for idx, (x, y) in enumerate(cords):
        if y in horizontal_lines:
            heapq.heappush(horizontal_lines[y], x)
        else:
            horizontal_lines[y] = [x]
        if idx + 1 < len(cords):
            for x2, y2 in cords[idx + 1 :]:
                if x2 == x or y2 == y:
                    continue
                area = (abs(x2 - x) + 1) * (abs(y2 - y) + 1)
                heapq.heappush(area_heap, (-area, (x, y), (x2, y2)))


def check_area(pos, pos2) -> bool:  # pos will always be the higher cord
    x1, y1 = pos[0], pos[1]
    x2, y2 = pos2[0], pos2[1]
    xbox_range = (x1, x2) if x1 < x2 else (x2, x1)
    ybox_range = (y1, y2) if y1 < y2 else (y2, y1)
    for line in range(ybox_range[0] + 1, ybox_range[1]):
        if line in horizontal_lines:
            line_start = heapq.nsmallest(1, horizontal_lines[line])[0]
            line_end = heapq.nlargest(1, horizontal_lines[line])[0]
            if line_start >= xbox_range[0] and line_end <= xbox_range[1]:
                return False
            if line_start <= xbox_range[0] and line_end >= xbox_range[0]:
                return False
            elif line_start <= xbox_range[1] and line_end >= xbox_range[1]:
                return False
    return True


def main():
    local_max = 0
    while area_heap:
        largest, pos, pos2 = heapq.heappop(area_heap)
        largest = -largest
        valid_area = check_area(pos, pos2)
        local_max = largest if valid_area and largest > local_max else local_max
        if valid_area and local_max >= largest:
            break

    print(local_max, pos, pos2)
    print(f"Took {(time.time() - start):.4f} seconds")


if __name__ == "__main__":
    main()
