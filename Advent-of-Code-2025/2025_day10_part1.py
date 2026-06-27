import time

start = time.time()
with open("./puzzle_inputs/2025_day10_input_s.txt", "r") as f:
    lines = [m.strip().split(" ") for m in f.readlines()]
    formatted_lines = [
        [
            [
                0 if n == "." else 1 for n in i[0].replace("[", "").replace("]", "")
            ],  # lights
            [
                list(map(int, _.replace(")", "").replace("(", "").split(",")))
                for _ in i[1:-1]
            ],  # button inputs
            i[-1],  # joltage reqs
        ]
        for i in lines
    ]


def conf_m(end_state: list[int], inputs: list[int]) -> int:
    start_pos = [0] * len(end_state)
    print(end_state)
    print(inputs)
    return


def main() -> None:
    for lights, inputs, _ in formatted_lines:
        conf_m(lights, inputs)


if __name__ == "__main__":
    main()
    print(f"Took {(time.time() - start):.4f} seconds")
