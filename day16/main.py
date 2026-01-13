
from collections import defaultdict
from functools import reduce
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


def solve2(target_pull: int) -> int:

    wheel_mags, bytes = read_input("input2.in")
    
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


if __name__ == "__main__":

    ans1: str = solve1()
    print(f"{ans1=}")

    ans2: int = solve2(2_024_202_420_24)
    print(f"{ans2=}")