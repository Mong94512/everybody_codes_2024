
def solve_1_2(filename: str) -> int:
    
    targets: list[int] = []
    stamps: list[int] = []

    with open(filename) as fin:
        while s := fin.readline():
            if s == "\n":
                break
            targets.append(int(s.strip()))

        stamps = [int(s) for s in fin.readline().split(", ")]

    MAX_TARGET: int = max(targets)
    INF: int = 1 << 30
    dp: list[int] = [INF] * (MAX_TARGET + 1)
    dp[0] = 0

    for target in range(1, MAX_TARGET + 1):
        for stamp in stamps:
            if target - stamp >= 0:
                dp[target] = min(dp[target], dp[target - stamp] + 1)

    ans: int = 0

    for target in targets:
        ans += dp[target]

    return ans


if __name__ == "__main__":

    ans1: int = solve_1_2("input1.in")
    print(f"{ans1=}")

    ans2: int = solve_1_2("input2.in")
    print(f"{ans2=}")