
def make_rune_word(mat: list[list[str]]) -> str:
    R: int = len(mat)
    C: int = len(mat[0])
    ans: str = ""

    for dy in range(4):
        for dx in range(4):
            ty, tx = dy + 2, dx + 2

            yst: set[str] = set()
            xst: set[str] = set()

            for y in range(R):
                if mat[y][tx] != ".":
                    yst.add(mat[y][tx])

            for x in range(C):
                if mat[ty][x] != ".":
                    xst.add(mat[ty][x])

            who: set[str] = yst & xst
            assert len(who) == 1

            mat[ty][tx] = next(iter(who))
            ans += mat[ty][tx]

    return ans


def calc_rune_word_power(rune_word: str) -> int:

    power: int = 0

    for i, rune in enumerate(rune_word, start = 1):
        base: int = ord(rune) - ord('A') + 1
        power += base * i

    return power


def solve1() -> str:

    mat: list[list[str]] = []

    with open("input1.in") as fin:
        mat = [list(s.strip()) for s in fin.readlines()]

    return make_rune_word(mat)


def solve2() -> int:

    def solve_queries(mats: list[list[list[str]]]) -> int:

        ans: int = 0

        for mat in mats:
            rune_word: str = make_rune_word(mat)
            ans += calc_rune_word_power(rune_word)

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



if __name__ == "__main__":
    
    ans1: str = solve1()
    print(f"{ans1=}")

    ans2: int = solve2()
    print(f"{ans2=}")