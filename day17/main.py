# from collections import defaultdict
# import itertools

from functools import reduce
import heapq


class Uf:
    def __init__(self, n: int, max_dist: int = 1 << 30):
        self.max_dist = max_dist
        self.n = n
        self.pars = [i for i in range(n)]
        self.ranks = [1] * n
        self.dists = [0] * n


    def to_root(self, node: int) -> int:

        while node != self.pars[node]:
            self.pars[node] = self.pars[self.pars[node]]
            node = self.pars[node]

        return node


    def unite(self, u: int, v: int, dist: int) -> bool:
        u = self.to_root(u)
        v = self.to_root(v)

        if u == v or dist > self.max_dist:
            return False

        self.pars[u] = v
        self.ranks[v] += self.ranks[u]
        self.dists[v] += self.dists[u] + dist

        self.ranks[u] = 0
        self.dists[u] = 0
        
        return True


    def topk_size(self, k: int) -> list[int]:

        assert k <= self.n
        min_heap: list[int] = []

        for i in range(self.n):
            size: int = self.ranks[i] + self.dists[i]
            heapq.heappush(min_heap, size)

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap


def calc_manhat_dist(lhs: tuple[int, ...], rhs: tuple[int, ...]) -> int:

    ans: int = 0

    for u, v in zip(lhs, rhs):
        ans += abs(u - v)

    return ans


def mst(mat: list[str], max_dist: int = 1 << 30) -> Uf:

    R: int = len(mat)
    C: int = len(mat[0])
    points: list[tuple[int, ...]] = []

    for y in range(R):
        for x in range(C):
            if mat[y][x] == '*':
                points.append((y, x))

    n: int = len(points)
    uf: Uf = Uf(n, max_dist)
    edges: list[tuple[int, ...]] = []

    for u in range(n):
        for v in range(u + 1, n):
            edges.append( ( calc_manhat_dist(points[u], points[v]), u, v) )

    edges.sort()

    for d, u, v in edges:
        uf.unite(u, v, d)

    return uf


def solve1() -> int:

    mat: list[str] = []

    with open("input1.in") as fin:
        mat = [s.strip() for s in fin.readlines()]

    return mst(mat).topk_size(1)[0]


def solve2() -> int:

    mat: list[str] = []

    with open("input2.in") as fin:
        mat = [s.strip() for s in fin.readlines()]

    return mst(mat).topk_size(1)[0]


def solve3() -> int:

    mat: list[str] = []

    with open("input3.in") as fin:
        mat = [s.strip() for s in fin.readlines()]

    top3_size: list[int] = mst(mat, 5).topk_size(3)

    return reduce(lambda acc, x : acc * x, top3_size, 1)


if __name__ == "__main__":

    ans1: int = solve1()
    print(f"{ans1=}")
    
    ans2: int = solve2()
    print(f"{ans2=}")
    
    ans3: int = solve3()
    print(f"{ans3=}")
