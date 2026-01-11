
from collections import defaultdict


def mark_rune_v1(mat: list[list[str]], ty: int, tx: int) -> int:
    
    R: int = 8
    C: int = 8

    mpy: dict[int, set[str]] = defaultdict(set[str])
    mpx: dict[int, set[str]] = defaultdict(set[str])
    is_found: int = 0

    for dy in range(R):
        for dx in range(C):
            y: int = ty + dy
            x: int = tx + dx
            if mat[y][x] not in ".?*":
                mpy[y].add(mat[y][x])
                mpx[x].add(mat[y][x])
                
    for dy in range(4):
        for dx in range(4):
            y: int = ty + dy + 2
            x: int = tx + dx + 2

            if mat[y][x] != '.':
                continue

            stu: set[str] = mpy[y] & mpx[x]

            if len(stu) != 1:
                continue

            mat[y][x] = next(iter(stu))
            is_found = 1

    return is_found


def mark_rune_v2(mat: list[list[str]], ty: int, tx: int) -> int:

    R: int = 8
    C: int = 8

    is_found: int = 0
    has_pair: set[str] = set()

    def is_has_pair(point: tuple[int, int]) -> bool:
        y, x = point
        return mat[y][x] in has_pair

    for dy in range(4):
        for dx in range(4):
            y: int = ty + dy + 2
            x: int = tx + dx + 2
            if mat[y][x] != '.':
                has_pair.add(mat[y][x])

    for dy in range(4):
        for dx in range(4):
            y: int = ty + dy + 2
            x: int = tx + dx + 2

            if mat[y][x] != '.':
                continue
            
            vert: list[tuple[int, int]] = [
                (ty, x),
                (ty + 1, x),
                (ty + 6, x),
                (ty + 7, x)
            ]

            hori: list[tuple[int, int]] = [
                (y , tx),
                (y ,tx + 1),
                (y ,tx + 6),
                (y ,tx + 7)
            ]

            vert = list(filter(lambda p : not is_has_pair(p), vert))
            hori = list(filter(lambda p : not is_has_pair(p), hori))

            if len(vert) != 1 or len(hori) != 1:
                continue

            y1, x1 = vert[0]
            y2, x2 = hori[0]

            if mat[y1][x1] != '?':
                y1, y2 = y2, y1
                x1, x2 = x2, x1

            if mat[y1][x1] != '?' or mat[y2][x2] == '?':
                continue

            is_found = 1
            mat[y1][x1] = mat[y2][x2]
            mat[y][x] = mat[y2][x2]
            has_pair.add(mat[y][x])

    return is_found


def make_runeword(mat: list[list[str]], ty: int, tx: int) -> str:

    ans: str = ""
    
    for dy in range(4):
        for dx in range(4):

            y: int = ty + dy + 2
            x: int = tx + dx + 2

            if not mat[y][x].isalpha():
                return ""

            ans += mat[y][x]

    return ans


def calc_runeword_power(rune_word: str) -> int:

    power: int = 0

    for i, rune in enumerate(rune_word, start = 1):
        base: int = ord(rune) - ord('A') + 1
        power += base * i

    return power


def solve1() -> str:

    mat: list[list[str]] = []

    with open("input1.in") as fin:
        mat = [list(s.strip()) for s in fin.readlines()]

    mark_rune_v1(mat, 0, 0)
    return make_runeword(mat, 0, 0)



def solve2() -> int:

    def solve_queries(mats: list[list[list[str]]]) -> int:

        ans: int = 0

        for mat in mats:
            mark_rune_v1(mat, 0, 0)
            ans += calc_runeword_power(make_runeword(mat, 0, 0))

        mats.clear()
        return ans
            

    ans: int = 0
    
    with open("input2.in") as fin:

        mats: list[list[list[str]]] = []

        while line := fin.readline():
            if line == "\n":
                ans += solve_queries(mats)
                continue

            for i, s in enumerate(line.strip().split(" ")):
                while len(mats) <= i:
                    mats.append([])
                mats[i].append(list(s))

        ans += solve_queries(mats)
            
    return ans


def solve3() -> int:

    mat: list[list[str]] = []
    ans: int = 0
    
    with open("input3.in") as fin:
        mat = [list(line.strip()) for line in fin.readlines()]

    while True:
        is_found: int = 0
        
        for ty in range(0, len(mat) - 2, 6):
            for tx in range(0, len(mat[0]) - 2, 6):
                is_found |= mark_rune_v1(mat, ty, tx)
        
        for ty in range(0, len(mat) - 2, 6):
            for tx in range(0, len(mat[0]) - 2, 6):
                is_found |= mark_rune_v2(mat, ty, tx)
        
        if not is_found:
            break

    for ty in range(0, len(mat) - 2, 6):
        for tx in range(0, len(mat[0]) - 2, 6):
            ans += calc_runeword_power(make_runeword(mat, ty, tx))

    return ans


if __name__ == "__main__":
    
    ans1: str = solve1()
    print(f"{ans1=}")

    ans2: int = solve2()
    print(f"{ans2=}")

    ans3: int = solve3()
    print(f"{ans3=}")