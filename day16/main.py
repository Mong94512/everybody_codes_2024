

def solve1() -> str:

    wheels: list[int] = []
    bytes: list[list[str]] = []
    
    with open("input1.in") as fin:
        wheels = [int(s) for s in fin.readline().strip().split(",")]
        fin.readline()

        while line := fin.readline():
            # print(line)
            for i in range(0, len(line), 4):
                assert i + 3 <= len(line)
                if line[i] == " ":
                    continue

                while len(bytes) <= i // 4:
                    bytes.append([])

                bytes[i // 4].append(line[i : i + 3])

            # for byte in bytes:
            #     print(f"{byte=}")

    # print(f"{wheels=}")

    ans: list[str] = []

    for i, byte in enumerate(bytes):
        print(byte)
        n: int = len(byte)
        offset: int = wheels[i] * 100
        # some j where -> (j - offset) % len(byte) == 0
        # j = offset % len(byte)
        j: int = offset % n
        ans.append(byte[j])

    return " ".join(ans)


if __name__ == "__main__":

    ans1: str = solve1()
    print(f"{ans1=}")