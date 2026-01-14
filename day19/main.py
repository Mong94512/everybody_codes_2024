
def read_input(filename: str) -> tuple[str, list[list[str]]]:

    rots: str = ""
    mat: list[list[str]] = []

    with open(filename) as fin:
        rots = fin.readline().strip()
        fin.readline()
        mat = [list(s.strip()) for s in fin.readlines()]

    return rots, mat


def apply_rotation(mat: list[list[str]], rots: str, rot_i: int = 0) -> int:

    R: int = len(mat)
    C: int = len(mat[0])
    dys: list[int] = [0, -1, -1, -1, 0, 1, 1, 1]
    dxs: list[int] = [-1, -1, 0, 1, 1, 1, 0, -1]

    for y in range(1, R - 1, 1):
        for x in range(1, C - 1, 1):
            sign: int = -1 if rots[rot_i] == "L" else 1
            rot_i = (rot_i + 1) % len(rots)
            keep: str =  mat[y][x - 1]

            for i in range(1, 8, 1):
                ti: int = (i * sign) % 8
                y1: int = y + dys[ti]
                x1: int = x + dxs[ti]
                keep, mat[y1][x1] = mat[y1][x1], keep

            mat[y][x - 1] = keep

    return rot_i


def solve1() -> str:

    rots, mat = read_input("input1.in")
    apply_rotation(mat, rots)

    for row in mat:
        if "<" in row:
            return "".join(row[row.index(">") + 1 : row.index("<")])

    return ""


def solve2() -> str:

    rots, mat = read_input("input2.in")

    for _ in range(100):
        apply_rotation(mat, rots)

    for row in mat:
        if "<" in row:
            return "".join(row[row.index(">") + 1 : row.index("<")])
        
    return ""


def solve3() -> str:

    rots, mat = read_input("input3.in")
    
    for rep in range(1 << 100):
        apply_rotation(mat, rots)

        if rep % 3:
            continue

        for row in mat:
            if ">" not in row or "<" not in row:
                continue

            begin_x: int = row.index(">")
            end_x: int = row.index("<")
            size: int = end_x - begin_x - 1

            if size <= 0 or size > 23:
                continue

            maybe: list[str] = row[begin_x + 1 : end_x]
            cover: str = "28"
            ci: int = 0
            ok: bool = True

            for i, ch in enumerate(maybe):
                if ch.isdigit():
                    continue

                if ci == len(cover):
                    ok = False
                    break
                maybe[i] = cover[ci]
                ci += 1

            if ci == 2 and ok:
                return "".join(maybe)

    return ""


if __name__ == "__main__":

    ans1: str = solve1()
    print(f"{ans1=}")
    
    ans2: str = solve2()
    print(f"{ans2=}")
    
    ans3: str = solve3()
    print(f"{ans3=}")