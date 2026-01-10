
def solve1() -> int:
    
    targets: list[int] = []

    with open("input1.in") as fin:
        targets = list(map(int, fin.readlines()))

    MAX_TARGET: int = max(targets)
    INF: int = 1 << 30
    STAMPS: list[int] = [1, 3, 5, 10]
    dp: list[int] = [INF] * (MAX_TARGET + 1)

    dp[0] = 0

    for target in range(1, MAX_TARGET + 1):
        for stamp in STAMPS:
            if target - stamp >= 0:
                dp[target] = min(dp[target], dp[target - stamp] + 1)

    ans: int = 0

    for target in targets:
        ans += dp[target]

    return ans


if __name__ == "__main__":

    ans1: int = solve1()
    print(f"{ans1=}")