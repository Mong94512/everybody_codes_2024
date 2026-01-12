
dirs: dict[str, list[int]] = {
    "U": [0, 1, 0],
    "D": [0, -1, 0],
    "R": [1, 0, 0],
    "L": [-1, 0, 0],
    "F": [0, 0, 1],
    "B": [0, 0, -1]
}

def solve1() -> int:

    queries: list[str] = []

    with open("input1.in") as fin:
        queries = fin.readline().strip().split(",")

    #(x-hori, y-vert, z-depth)
    pos: list[int] = [0, 0, 0]
    best: int = 0

    for q in queries:
        dir: str = q[0]
        step: int = int(q[1:])

        for i, mag in enumerate(dirs[dir]):
            pos[i] += mag * step
            best = max(best, abs(pos[i]))

    return best


def solve2() -> int:

    queries: list[list[str]] = []

    with open("input2.in") as fin:
        while line := fin.readline():
            queries.append(line.strip().split(","))

    vis: set[tuple[int, int, int]] = set()

    def go_mark(query: list[str]) -> None:
        #(x-hori, y-vert, z-depth)
        pos: list[int] = [0, 0, 0]

        for q in query:
            dir: str = q[0]
            step: int = int(q[1:])

            while step:
                step -= 1
                for i, mag in enumerate(dirs[dir]):
                    pos[i] += mag
                    
                vis.add(tuple(pos)) # type: ignore


    for query in queries:
        go_mark(query) 

    return len(vis)


if __name__ == "__main__":

    ans1: int = solve1()
    print(f"{ans1=}")
    
    ans2: int = solve2()
    print(f"{ans2=}")