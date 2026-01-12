
from collections import deque


def floyd_warshall(
        mat: list[str], 
        src: tuple[int, int], 
        dest: tuple[int, int]) -> int:
    
    INF: int = 1 << 30
    R: int = len(mat)
    C: int = len(mat[0])

    dp: list[list[int]] = [[INF] * C for _ in range(R)]
    dq: deque[tuple[int, int]] = deque()
    dirs: list[tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def is_invalid(y: int, x: int) -> bool:
        return min(y, x) < 0 or y >= R or x >= C or mat[y][x] == '#'


    def get_level(ch: str) -> int:
        return 0 if ch in "SE" else ord(ch) - ord('0')


    def calc_level_dist(ch: str, ch1: str) -> int:

        l: int = get_level(mat[y][x])
        l1: int = get_level(mat[y1][x1])
        d1: int = abs(l - l1)
        d2: int = 10 - d1

        return min(d1, d2) + 1

    dq.append(src)
    dp[src[0]][src[1]] = 0

    while dq:
        y, x = dq.popleft()

        for dy, dx in dirs:
            y1: int = y + dy
            x1: int = x + dx

            if is_invalid(y1, x1):
                continue
            
            add_dist: int = calc_level_dist(mat[y][x], mat[y1][x1])
            new_dist: int = dp[y][x] + add_dist

            if new_dist < dp[y1][x1]:
                dp[y1][x1] = new_dist
                dq.append((y1, x1))


    return dp[dest[0]][dest[1]]


def solve1() -> int:
    
    mat: list[str] = []

    with open("input1.in") as fin:
        mat = [s.strip() for s in fin.readlines()]

    src: tuple[int, int] = (-1, -1)
    dest: tuple[int, int] = (-1, -1)

    for y in range(len(mat)):
        for x in range(len(mat[0])):
            if mat[y][x] == 'S':
                src = (y, x)
            elif mat[y][x] == 'E':
                dest = (y, x)

    return floyd_warshall(mat, src, dest)


def solve2() -> int:
    
    mat: list[str] = []

    with open("input2.in") as fin:
        mat = [s.strip() for s in fin.readlines()]

    src: tuple[int, int] = (-1, -1)
    dest: tuple[int, int] = (-1, -1)

    for y in range(len(mat)):
        for x in range(len(mat[0])):
            if mat[y][x] == 'S':
                src = (y, x)
            elif mat[y][x] == 'E':
                dest = (y, x)

    return floyd_warshall(mat, src, dest)


if __name__ == "__main__":
    
    ans1: int = solve1()
    print(f"{ans1=}")

    ans2: int = solve2()
    print(f"{ans2=}")

