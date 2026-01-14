# from collections import defaultdict
# import itertools


def calc_manhat_dist(lhs: tuple[int, ...], rhs: tuple[int, ...]) -> int:

    ans: int = 0

    for u, v in zip(lhs, rhs):
        ans += abs(u - v)

    return ans


def mst(mat: list[str]) -> int:

    R: int = len(mat)
    C: int = len(mat[0])
    points: list[tuple[int, ...]] = []

    for y in range(R):
        for x in range(C):
            if mat[y][x] == '*':
                points.append((y, x))

    n: int = len(points)
    edges: list[tuple[int, ...]] = []
    pars: list[int] = [i for i in range(n)]

    def to_root(node: int) -> int:

        while node != pars[node]:
            pars[node] = pars[pars[node]]
            node = pars[node]

        return node


    for u in range(n):
        for v in range(u + 1, n):
            edges.append( ( calc_manhat_dist(points[u], points[v]), u, v) )

    edges.sort()
    ans: int = len(points)

    for d, u, v in edges:
        u = to_root(u)
        v = to_root(v)
        if u != v:
            ans += d
            pars[u] = v

    return ans


def solve1() -> int:

    mat: list[str] = []

    with open("input1.in") as fin:
        mat = [s.strip() for s in fin.readlines()]

    return mst(mat)


def solve2() -> int:

    mat: list[str] = []

    with open("input2.in") as fin:
        mat = [s.strip() for s in fin.readlines()]

    return mst(mat)


if __name__ == "__main__":

    ans1: int = solve1()
    print(f"{ans1=}")
    
    ans2: int = solve2()
    print(f"{ans2=}")
