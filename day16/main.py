
from collections import defaultdict
from functools import cache, reduce
import sys
# from typing import Counter

# fout = open("sandbox.out", "w")

def read_input(filename: str) -> tuple[list[int], list[list[str]]]:

    wheel_mags: list[int] = []
    bytes: list[list[str]] = []
    
    with open(filename) as fin:
        wheel_mags = [int(s) for s in fin.readline().strip().split(",")]
        fin.readline()

        while line := fin.readline():
            for i in range(0, len(line), 4):
                if line[i] in " \n":
                    continue

                assert i + 3 <= len(line)

                while len(bytes) <= i // 4:
                    bytes.append([])

                bytes[i // 4].append(line[i : i + 3])

    return wheel_mags, bytes


def solve1() -> str:

    wheel_mags, bytes = read_input("input1.in")
    ans: list[str] = []

    for i, byte in enumerate(bytes):
        n: int = len(byte)
        offset: int = wheel_mags[i] * 100
        j: int = offset % n
        ans.append(byte[j])

    return " ".join(ans)


def solve2() -> int:

    wheel_mags, bytes = read_input("input2.in")
    target_pull: int = 2_024_202_420_24
    
    vis: set[str] = set()
    path: list[tuple[str, int]] = []
    ans: int = 0

    while target_pull > 0:
    
        cfreq: dict[str, int] = defaultdict(int)
        score: int = 0
        poss: str = ""

        for i, byte in enumerate(bytes):
            offset: int = wheel_mags[i] * (len(path) + 1)
            j: int = offset % len(byte)
            poss += str(j) + ","
            cfreq[byte[j][0]] += 1
            cfreq[byte[j][2]] += 1

        if poss in vis:
            for i, ps in enumerate(path):
                if ps[0] == poss:
                    path = path[i:]
                    break
            break
        
        for freq in cfreq.values():
            score += max(0, freq - 2)

        ans += score
        path.append((poss, score))
        vis.add(poss)
        target_pull -= 1

    if target_pull <= 0:
        return ans
    
    cy_len: int = target_pull // len(path)
    rem: int = target_pull % len(path)
    ans += reduce(lambda acc, x : acc + x[1], path, 0) * cy_len

    for i in range(rem):
        ans += path[i][1]

    return ans


def solve3() -> tuple[int, int]:
    
    sys.setrecursionlimit(1_000_00)
    wheel_mags, bytes = read_input("input3.in")
    MAX_PULL: int = 256
    INF: int = 1 << 30

    def calc_score(pull: int, delta: int) -> int:

        score: int = 0
        cfreq: dict[str, int] = defaultdict(int)

        for i, byte in enumerate(bytes):
            j: int = (pull * wheel_mags[i] - delta) % len(byte)
            b: str = byte[j]
            cfreq[b[0]] += 1
            cfreq[b[2]] += 1

        for freq in cfreq.values():
            score += max(0, freq - 2)

        return score

    @cache
    def dfs(pull: int, delta: int) -> tuple[int, int]:
        if pull > MAX_PULL:
            return 0, 0

        cur_best: list[int] = [-INF, INF]

        for d in range(-1, 2, 1):
            score: int = calc_score(pull, delta + d)
            other_best: tuple[int, int] = dfs(pull + 1, delta + d)

            cur_best[0] = max(cur_best[0], other_best[0] + score)
            cur_best[1] = min(cur_best[1], other_best[1] + score)

        return tuple[int, int](cur_best)

    return dfs(1, 0)


if __name__ == "__main__":

    ans1: str = solve1()
    print(f"{ans1=}")

    ans2: int = solve2()
    print(f"{ans2=}")

    ans3: tuple[int, int] = solve3()
    print(f"{ans3=}")