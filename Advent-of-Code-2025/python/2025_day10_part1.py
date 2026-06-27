import time

start = time.time()
with open("./puzzle_inputs/2025_day10_input.txt", "r") as f:
    formatted_lines = [
        [
            [
                False if n == "." else True
                for n in i[0].replace("[", "").replace("]", "")
            ],  # lights
            [
                set(map(int, _.replace(")", "").replace("(", "").split(",")))
                for _ in i[1:-1]
            ],  # button inputs
            list(
                map(int, i[-1].replace("}", "").replace("{", "").split(","))
            ),  # joltage reqs
        ]
        for i in [m.strip().split(" ") for m in f.readlines()]
    ]


def least_turns(l_pos, bpresses, inputs, count) -> int:
    count += 1
    for c in bpresses:
        for i in inputs:
            if (c ^ i) in inputs:
                print(count, c ^ i, l_pos, inputs)
                return count
            c ^= i
    return least_turns(l_pos, bpresses, inputs, count)


def conf_m(end_state: list[int], inputs: list[int]) -> int:
    l_pos = {idx for idx, i in enumerate(end_state) if i}
    bpresses = []
    for i in inputs:
        bpresses.append((l_pos ^ i))
    count = 1
    t = least_turns(l_pos, bpresses, inputs, count)
    return t


def main() -> None:
    total = 0
    for lights, inputs, _ in formatted_lines:
        total += conf_m(lights, inputs)
    print(total)


if __name__ == "__main__":
    main()
    print(f"Took {(time.time() - start):.4f} seconds")
