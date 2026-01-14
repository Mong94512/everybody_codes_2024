#TRUE AND REAL!!

from collections import defaultdict


INF = 1 << 30

def bfs(mat: list[str], que: list[tuple[int, int]]) -> list[list[int]]:

    R: int = len(mat)
    C: int = len(mat[0])
    step: int = -1
    dists: list[list[int]] = [[INF] * C for _ in range(R)]

    def is_valid(y: int, x: int) -> bool:
        return (
            0 <= y < R 
                and 
            0 <= x < C 
                and 
            dists[y][x] == INF 
                and 
            mat[y][x] != '#'
        )


    while que:
        step += 1
        next_que: list[tuple[int, int]] = []

        for y, x in que:
            dists[y][x] = step
            for dy, dx in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                y1: int = y + dy
                x1: int = x + dx
                if is_valid(y1, x1):
                    next_que.append((y1, x1))

        que = next_que

    return dists
 

def solve12(filename: str) -> int:

    mat: list[str] = []

    with open(filename) as fin:
        mat = [s.strip() for s in fin.readlines()]

    R: int = len(mat)
    C: int = len(mat[0])
    step: int = -1
    ans: int = -1
    vis: set[tuple[int, int]] = set()
    que: list[tuple[int, int]] = []

    def is_src(y: int, x: int) -> bool:
        return (min(y, x) == 0 or y == R - 1 or x == C - 1) and mat[y][x] == '.'

    for y in range(R):
        for x in range(C):
            if is_src(y, x):
                que.append((y, x))

    dists = bfs(mat, que)
    ans: int = -1

    for y in range(R):
        for x in range(C):
            if mat[y][x] == 'P':
                ans = max(ans, dists[y][x])

    assert ans != -1

    return ans


def solve3() -> int:
    
    mat: list[str] = []

    with open("input3.in") as fin:
        mat = [s.strip() for s in fin.readlines()]

    R: int = len(mat)
    C: int = len(mat[0])
    acc_dists: dict[tuple[int, int], int] = defaultdict(int)

    for y in range(R):
        for x in range(C):
            if mat[y][x] == 'P':
                dists = bfs(mat, [(y, x)])
                for y1 in range(R):
                    for x1 in range(C):
                        if mat[y1][x1] == '.' and dists[y1][x1] != INF:
                            acc_dists[(y1, x1)] += dists[y1][x1]

    best: int = INF

    for dist in acc_dists.values():
        best = min(best, dist)

    return best

if __name__ == "__main__":

    ans1: int = solve12("input1.in")
    print(f"{ans1=}")
    
    ans2: int = solve12("input2.in")
    print(f"{ans2=}")

    ans3: int = solve3()
    print(f"{ans3=}")