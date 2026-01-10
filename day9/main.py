
def read_input(filename: str) -> tuple[list[int], list[int]]:

    targets: list[int] = []
    stamps: list[int] = []

    with open(filename) as fin:
        while s := fin.readline():
            if s == "\n":
                break
            targets.append(int(s.strip()))

        stamps = [int(s) for s in fin.readline().split(", ")]

    return targets, stamps


def solve_dp(targets: list[int], stamps: list[int]):

    MAX_TARGET: int = max(targets)
    INF: int = 1 << 30
    dp: list[int] = [INF] * (MAX_TARGET + 1)
    dp[0] = 0

    for target in range(1, MAX_TARGET + 1):
        for stamp in stamps:
            if target - stamp >= 0:
                dp[target] = min(dp[target], dp[target - stamp] + 1)

    return dp


def solve1() -> int:

    targets, stamps = read_input("input1.in")
    ans: int = 0
    dp: list[int] = solve_dp(targets, stamps)

    for target in targets:
        ans += dp[target]

    return ans


def solve2() -> int:

    targets, stamps = read_input("input2.in")
    ans: int = 0
    dp: list[int] = solve_dp(targets, stamps)

    for target in targets:
        ans += dp[target]

    return ans


def solve3() -> int:

    INF = 1 << 30
    targets, stamps = read_input("input3.in")
    ans: int = 0
    dp = solve_dp(targets, stamps)

    for target in targets:

        half: int = target // 2
        best: int = INF

        for delta in range(-100, 101, 1):
            lhs: int = half + delta
            rhs: int = target - lhs

            if min(lhs, rhs) < 0 or max(lhs, rhs) > target:
                continue

            if abs(lhs - rhs) > 100:
                continue

            best = min(best, dp[lhs] + dp[rhs])

        assert(best != INF)
        ans += best

    return ans


if __name__ == "__main__":

    ans1: int = solve1()
    print(f"{ans1=}")

    ans2: int = solve2()
    print(f"{ans2=}")

    ans3: int = solve3()
    print(f"{ans3=}")