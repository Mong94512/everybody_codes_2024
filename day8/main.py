

def solve1() -> int:

    total_block: int = 0
    
    with open("input1.in") as fin:
        total_block = int(fin.readline())

    # print(f"{total_block=}")

    block: int = 1
    width: int = 1

    while block < total_block:
        width += 2
        block += width
    

    missing: int = block - total_block

    print(f"{total_block=} {block=} {missing=} {width=}")

    return width * missing


if __name__ == "__main__":
    # print("Ayooo!")

    ans1: int = solve1()
    print(f"{ans1=}")