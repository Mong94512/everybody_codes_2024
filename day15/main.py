
dirs: list[tuple[int, int]] = [(0, -1), (0, 1), (1, 0), (-1, 0)]


def solve1() -> int:

    mat: list[str] = []

    with open("input1.in") as fin:
        while s := fin.readline().strip():
            mat.append(s)

    R: int = len(mat)
    C: int = len(mat[0])

    que: list[tuple[int, int]] = [(0, mat[0].index('.'))]
    vis: set[tuple[int, int]] = set([que[-1]])
    step: int = -1

    def is_valid(y: int, x: int) -> bool:
        return (
            0 <= y < R 
                and 
            0 <= x < C 
                and 
            (y, x) not in vis 
                and 
            mat[y][x] != '#'
        )

    while que:

        step += 1
        next_que: list[tuple[int, int]] = []
        
        for y, x in que:
            if mat[y][x] == 'H':
                return step * 2

            for dy, dx in dirs:
                if is_valid(y + dy, x + dx):
                    next_que.append((y + dy, x + dx))
                    vis.add(next_que[-1])

        que = next_que

    return -1


def solve2() -> int:

    mat: list[str] = []

    with open("input2.in") as fin:
        while s := fin.readline().strip():
            mat.append(s)

    R: int = len(mat)
    C: int = len(mat[0])
    herbs: list[str] = []

    for y in range(R):
        for x in range(C):
            if mat[y][x].isalpha():
                herbs.append(mat[y][x])

    herbs = list(set(herbs))
    vis: set[tuple[int, int, int]] = set()
    que: list[tuple[int, int, int]] = []

    que.append((0, mat[0].index('.'), 0))
    vis.add(que[-1])
    step: int = -1

    target: tuple[int, int, int] = (
        0, 
        mat[0].index('.'), 
        (2 ** len(herbs)) - 1 
    )

    def is_valid(y: int, x: int) -> bool:
        return (
            0 <= y < R 
                and 
            0 <= x < C 
                and 
            mat[y][x] not in "#~"
        )


    def get_herb_id(herb: str) -> int:
        return 0 if herb not in herbs else 1 << herbs.index(herb)


    while que:
        step += 1
        next_que: list[tuple[int, int, int]] = []

        for y, x, mask in que:
            if (y, x, mask) == target:
                return step
            
            for dy, dx in dirs:
                y1: int = y + dy
                x1: int = x + dx
                if not is_valid(y1, x1):
                    continue

                mask1: int = mask | get_herb_id(mat[y1][x1])

                if (y1, x1, mask1) not in vis:
                    next_que.append((y1, x1, mask1))
                    vis.add((y1, x1, mask1))

        que = next_que

    return -1


def solve3() -> int:

    mat: list[str] = []

    with open("input3.in") as fin:
        while s := fin.readline().strip():
            mat.append(s)

    R: int = len(mat)
    C: int = len(mat[0])
    herbs: list[str] = []

    for y in range(R):
        for x in range(C):
            if mat[y][x].isalpha():
                herbs.append(mat[y][x])

    herbs = list(set(herbs))



    return -1


if __name__ == "__main__":

    ans1: int = solve1()
    print(f"{ans1=}")
    
    ans2: int = solve2()
    print(f"{ans2=}")
    
    # ans3: int = solve3()
    # print(f"{ans3=}")