
from collections import defaultdict


def solve1() -> int:
    
    mat: list[str] = []

    with open("input1.in") as fin:
        mat = [s.strip() for s in fin.readlines()]

    R: int = len(mat)
    C: int = len(mat[0])

    catas: list[tuple[int, int]] = []
    ans: int = 0

    for y in range(R):
        if mat[y][1].isalpha():
            catas.append((y, 1))

    for y2 in range(R):
        for x2 in range(C):
            if mat[y2][x2] == 'T':
                for y1, x1 in catas:
                    dif: int = y1 - y2 + x2 - x1
                    if dif % 3 == 0:
                        seg_num: int = ord(mat[y1][x1]) - ord('A') + 1
                        shooting_pow: int = dif // 3
                        ans += seg_num * shooting_pow

    return ans


if __name__ == "__main__":
    
    ans1: int = solve1()
    print(f"{ans1=}")