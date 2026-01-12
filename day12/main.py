
def solve1() -> int:
    
    mat: list[str] = []

    with open("input1.in") as fin:
        mat = [s.strip() for s in fin.readlines()]

    R: int = len(mat)
    C: int = len(mat[0])

    catas: list[tuple[int, int]] = []
    ans: int = 0

    for y in range(R):
        if mat[y][1].isalpha():
            catas.append((y, 1))

    for y2 in range(R):
        for x2 in range(C):
            if mat[y2][x2] == 'T':
                for y1, x1 in catas:
                    dif: int = y1 - y2 + x2 - x1
                    if dif % 3 == 0:
                        seg_num: int = ord(mat[y1][x1]) - ord('A') + 1
                        shooting_pow: int = dif // 3
                        ans += seg_num * shooting_pow

    return ans


def solve2() -> int:
    
    mat: list[str] = []

    with open("input2.in") as fin:
        mat = [s.strip() for s in fin.readlines()]

    R: int = len(mat)
    C: int = len(mat[0])

    catas: list[tuple[int, int]] = []
    ans: int = 0

    for y in range(R):
        if mat[y][1].isalpha():
            catas.append((y, 1))

    for y2 in range(R):
        for x2 in range(C):
            if mat[y2][x2] in "TH":
                mag: int = 2 if mat[y2][x2] == 'H' else 1
                for y1, x1 in catas:
                    dif: int = y1 - y2 + x2 - x1
                    if dif % 3 == 0:
                        seg_num: int = ord(mat[y1][x1]) - ord('A') + 1
                        shooting_pow: int = dif // 3
                        rank: int = seg_num * shooting_pow * mag
                        ans += rank

    return ans


def solve3() -> int:
    
    INF: int = 1 << 55
    targets: list[tuple[int, int]] = []

    with open("input3.in") as fin:
        while s := fin.readline().strip():
            x, y = map(int, s.split(" "))
            targets.append((x, y))


    def case_up(x2: int, y2: int, x1: int, y1: int) -> tuple[int, int]:

        dx: int = x2 - x1
        dy: int = y2 - y1

        if dx % 2 or dy % 2:
            return INF, INF
        
        px: int = dx // 2
        py: int = dy // 2

        if px != py:
            return INF, INF
        
        return px, (y1 + 1) * px

    
    def case_flat(x2: int, y2: int, x1: int, y1: int) -> tuple[int, int]:
        if (x2 - x1) % 2:
            return INF, INF
        
        t: int = (x2 - x1) // 2
        p: int = y2 - t - y1

        if t <= p or t > 2 * p:
            return INF, INF

        return t, (y1 + 1) * p


    def case_down(x2: int, y2: int, x1: int, y1: int) -> tuple[int, int]:
        if (x2 - x1) % 2:
            return INF, INF
        
        t: int = (x2 - x1) // 2

        if (y2 - y1) % 3:
            return INF, INF

        p: int = (y2 - y1) // 3

        if t < 2 * p:
            return INF, INF

        return t, (y1 + 1) * p


    ans: int = 0

    while targets:

        next_targets: list[tuple[int, int]] = []

        for x2, y2 in targets:

            best: tuple[int, int] = (INF, INF)

            for x1, y1 in [(0, 0), (0, 1), (0, 2)]:
                up = case_up(x2, y2, x1, y1) 
                flat = case_flat(x2, y2, x1, y1)
                down = case_down(x2, y2, x1, y1)
                best = min(best, up, flat, down)

            if best[0] == INF:
                next_targets.append((x2 - 1, y2 - 1))
            else:
                ans += best[1]

        targets = next_targets

    return ans


if __name__ == "__main__":
    
    ans1: int = solve1()
    print(f"{ans1=}")

    ans2: int = solve2()
    print(f"{ans2=}")

    ans3: int = solve3()
    print(f"{ans3=}")