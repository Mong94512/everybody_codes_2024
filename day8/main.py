

def solve1() -> int:

    avai_blocks: int = 0
    
    with open("input1.in") as fin:
        avai_blocks = int(fin.readline())

    total_blocks: int = 1
    width: int = 1

    while total_blocks < avai_blocks:
        width += 2
        total_blocks += width

    extra_blocks: int = total_blocks - avai_blocks

    return width * extra_blocks


def solve2() -> int:

    MOD: int = 1111
    AVAILABLE_BLOCKS: int = 20240000
    priests: int = 0
    thickness: list[int] = [1]
    total_blocks: int = 0
    final_width: int = 0
    layer: int = 0

    with open("input2.in") as fin:
        priests = int(fin.readline())

    while True:
        width = 1 + 2 * layer
        blocks = thickness[-1] * width
        total_blocks += blocks
        final_width = width

        if total_blocks >= AVAILABLE_BLOCKS:
            break

        nxt = (thickness[-1] * priests) % MOD
        thickness.append(nxt)
        layer += 1
        

    extra_blocks: int = max(0, total_blocks - AVAILABLE_BLOCKS)
    
    return extra_blocks * final_width


if __name__ == "__main__":

    ans1: int = solve1()
    print(f"{ans1=}")

    ans2: int = solve2()
    print(f"{ans2=}")