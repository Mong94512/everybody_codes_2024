from typing import TypeAlias

vec3t: TypeAlias = tuple[int, int, int]

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

    vis: set[vec3t] = set()

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
                    
                vis.add(vec3t(pos))


    for query in queries:
        go_mark(query) 

    return len(vis)


def solve3() -> int:

    INF: int = 1 << 30
    branches: list[list[str]] = []
    points: set[vec3t] = set()
    leaves: set[vec3t] = set()
    trunks: dict[vec3t, list[int]] = {}

    with open("input3.in") as fin:
        while line := fin.readline():
            branches.append(line.strip().split(","))


    def add_points(branch: list[str]) -> list[int]:
        #(x-hori, y-vert, z-depth)
        pos: list[int] = [0, 0, 0]

        for b in branch:
            dir: str = b[0]
            step: int = int(b[1:])

            while step:
                step -= 1
                for i, mag in enumerate(dirs[dir]):
                    pos[i] += mag
                    
                points.add(vec3t(pos))

        return pos


    def bfs(src: vec3t) -> None:
        
        que: list[vec3t] = [src]
        vis: set[vec3t] = set([src])
        step: int = -1

        while que:

            step += 1
            next_que: list[vec3t] = []

            for cur in que:
                if cur in trunks:
                    trunks[cur].append(step)

                for dir in dirs.values():
                    nei = vec3t(p + d for p, d in zip(cur, dir))
                    if nei in points and nei not in vis:
                        next_que.append(nei)
                        vis.add(nei)

            que = next_que


    for branch in branches:
        leaves.add(vec3t(add_points(branch)))

    for y in range(1, INF):
        if (0, y, 0) not in points:
            break
        trunks[(0, y, 0)] = []

    for leaf in leaves:
        bfs(leaf)

    best: int = INF

    for steps in trunks.values():
        assert len(steps) == len(leaves)
        best = min(best, sum(steps))

    return best


if __name__ == "__main__":

    ans1: int = solve1()
    print(f"{ans1=}")
    
    ans2: int = solve2()
    print(f"{ans2=}")
    
    ans3: int = solve3()
    print(f"{ans3=}")