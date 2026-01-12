
from collections import deque


def read_mat(filename: str) -> list[str]:

    with open(filename) as fin:
        return list(map(lambda x : x.strip(), fin.readlines()))


def get_src_dest(mat: list[str]) -> tuple[list[tuple[int, int]], tuple[int, int]]:
    
    srcs: list[tuple[int, int]] = []
    dest: tuple[int, int] = (-1, -1)

    for y in range(len(mat)):
        for x in range(len(mat[0])):
            if mat[y][x] == 'S':
                srcs.append((y, x))
            elif mat[y][x] == 'E':
                dest = (y, x)

    return srcs, dest


def floyd_warshall(
        mat: list[str], 
        srcs: list[tuple[int, int]], 
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

        l: int = get_level(ch)
        l1: int = get_level(ch1)
        d1: int = abs(l - l1)
        d2: int = 10 - d1

        return min(d1, d2) + 1


    for y, x in srcs:
        dp[y][x] = 0
        dq.append((y, x))

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

    mat = read_mat("input1.in")
    srcs, dest = get_src_dest(mat)

    return floyd_warshall(mat, srcs, dest)


def solve2() -> int:
    
    mat = read_mat("input2.in")
    srcs, dest = get_src_dest(mat)

    return floyd_warshall(mat, srcs, dest)


def solve3() -> int:
    
    mat = read_mat("input3.in")
    srcs, dest = get_src_dest(mat)

    return floyd_warshall(mat, srcs, dest)


if __name__ == "__main__":
    
    ans1: int = solve1()
    print(f"{ans1=}")

    ans2: int = solve2()
    print(f"{ans2=}")

    ans3: int = solve3()
    print(f"{ans3=}")
