from collections import defaultdict


def read_edges(filename: str) -> dict[str, list[str]]:
    
    edges: dict[str, list[str]] = defaultdict(list)

    with open(filename) as fin:
        while line := fin.readline().strip():
            u, vstr = line.split(":") 
            edges[u] = vstr.split(",")

    return edges


def calc_dp(edges: dict[str, list[str]], src: str, MAX_DAY: int) -> int:

    dp: dict[tuple[str, int], int] = {}

    def dfs(cur: str, day: int) -> int:
        if day == MAX_DAY:
            return 1

        if (cur, day) in dp:
            return dp[(cur, day)]
        
        way: int = 0

        for nei in edges[cur]:
            way += dfs(nei, day + 1)

        dp[(cur, day)] = way
        return way
    
    return dfs(src, 0)


def solve1() -> int:

    edges: dict[str, list[str]] = read_edges("input1.in")
    MAX_DAY: int = 4

    return calc_dp(edges, "A", MAX_DAY)


def solve2() -> int:

    edges: dict[str, list[str]] = read_edges("input2.in")
    MAX_DAY: int = 10

    return calc_dp(edges, "Z", MAX_DAY)


def solve3() -> int:

    edges: dict[str, list[str]] = read_edges("input3.in")
    MAX_DAY: int = 20

    scores: list[int] = []

    for src in edges.keys():
        scores.append(calc_dp(edges, src, MAX_DAY))

    scores.sort()

    return scores[-1] - scores[0]


if __name__ == "__main__":

    ans1: int = solve1()
    print(f"{ans1=}")

    ans2: int = solve2()
    print(f"{ans2=}")
    
    ans3: int = solve3()
    print(f"{ans3=}")