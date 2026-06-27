import time
import heapq

start = time.time()
with open("./puzzle_inputs/2025_day9_input.txt", "r") as f:
    cords = sorted(
        [list(map(int, _.strip().split(","))) for _ in f.readlines()],
        key=lambda _: _[1],
    )
    horizontal_lines = {}
    vertical_lines = {}
    area_heap = []
    for idx, (x, y) in enumerate(cords):
        if x in vertical_lines:
            vertical_lines[x].append(y)
        else:
            vertical_lines[x] = [y]
        if y in horizontal_lines:
            heapq.heappush(horizontal_lines[y], x)
        else:
            horizontal_lines[y] = [x]
        for x2, y2 in cords[idx + 1 :]:
            area = (abs(x2 - x) + 1) * (abs(y2 - y) + 1)
            heapq.heappush(area_heap, (-area, (x, y), (x2, y2)))


def check_area(pos, pos2) -> bool:  # pos will always be the higher cord
    x1, y1 = pos
    x2, y2 = pos2
    xbox_range = (x1, x2) if x1 < x2 else (x2, x1)
    ybox_range = (y1, y2) if y1 < y2 else (y2, y1)
    h_line_keys = list(horizontal_lines.keys())
    start_ptr = h_line_keys.index(ybox_range[0])
    for k in h_line_keys[start_ptr:]:
        if k < ybox_range[1] and k > ybox_range[0]:
            line_start = heapq.nsmallest(1, horizontal_lines[k])[0]
            line_end = heapq.nlargest(1, horizontal_lines[k])[0]
            if line_start >= xbox_range[0] and line_end <= xbox_range[1]:
                return False
            if line_start <= xbox_range[0] and line_end >= xbox_range[0]:
                return False
            elif line_start <= xbox_range[1] and line_end >= xbox_range[1]:
                return False
        if k == ybox_range[1]:  # not needed for actual puzzle input just example
            bot_line_start = heapq.nsmallest(1, horizontal_lines[k])[0]
            bot_line_end = heapq.nlargest(1, horizontal_lines[k])[0]
            for x in vertical_lines.keys():
                if x >= bot_line_start and x <= bot_line_end:
                    if (
                        len(vertical_lines[x]) > 2
                    ):  # hacky fix too lazy to fix edge edge case
                        return False
                    bot_vert_line = vertical_lines[x][1]
                    if bot_vert_line == k:
                        if bot_line_start > xbox_range[0]:
                            return False
                        if bot_line_end > xbox_range[1]:
                            return False
                        if (
                            bot_line_start == xbox_range[0]
                            and bot_line_end < xbox_range[1]
                        ):
                            return False
                        if (
                            bot_line_end == xbox_range[1]
                            and bot_line_start > xbox_range[0]
                        ):
                            return False

    return True


def main():
    while area_heap:
        largest, pos, pos2 = heapq.heappop(area_heap)
        if check_area(pos, pos2):
            break

    print(-largest, pos, pos2)
    print(f"Took {(time.time() - start):.4f} seconds")


if __name__ == "__main__":
    main()
