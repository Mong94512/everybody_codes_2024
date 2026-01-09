from io import TextIOWrapper
from typing import List


def parse_plans(fin: TextIOWrapper) -> List[List[str]]:

    plans: List[List[str]] = []

    while s := fin.readline():
        if s == "\n":
            break

        plan = s.strip().split(",")
        plan.insert(0, plan[0][0]) 
        plan[1] = plan[1][2:]   
        plans.append(plan)

    return plans


def parse_track(fin: TextIOWrapper) -> str:

    rect: List[str] = [s.strip() for s in fin.readlines()]
    dy_dx: List[tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    track: str = ""
    y: int = 0
    x: int = 0
    ptr: int = 0
    vis: set[tuple[int, int]] = set()

    def is_valid(y: int, x: int) -> bool:
        return (
            0 <= y < len(rect) 
                and 
            0 <= x < len(rect[y]) 
                and 
            rect[y][x] != ' ' 
                and 
            (y, x) not in vis
        )

    while True:
        while True:
            y1: int = y + dy_dx[ptr][0]
            x1: int  = x + dy_dx[ptr][1]
            if is_valid(y1, x1):
                y, x = y1, x1
                break

            ptr = (ptr + 1) % len(dy_dx)

        track += rect[y][x]
        vis.add((y, x))
        
        if rect[y][x] == 'S':
            break

    return track


def solve1() -> str:

    plans: List[List[str]] = []

    with open("input1.in") as fin:
        plans = parse_plans(fin)

    def calc_score(
        plan: List[str], 
        power: int = 10, 
        total_segment: int = 10) -> tuple[int, str]:
    
        score: int = 0
        ptr: int = 1

        for _ in range(total_segment):
            match plan[ptr]:
                case "+":
                    power += 1
                case "-":
                    power = max(0, power - 1)

            score += power
            ptr = max(1, (ptr + 1) % len(plan))

        return (score, plan[0])
    
    ranks: List[tuple[int, str]] = [calc_score(plan) for plan in plans]
    ranks.sort(reverse = True)
    ans: str = ""

    for _, name in ranks:
        ans += name

    return ans


def solve2() -> str:

    track: str = ""
    plans: List[List[str]] = []

    with open("input2.in") as fin:
        plans = parse_plans(fin)
        track = parse_track(fin)

    def calc_score(plan: List[str]) -> tuple[int, str]:

        def update_power(power: int, t: str, p: str) -> int:
            if t == "+":
                return power + 1
            if t == "-":
                return max(0, power - 1)
            if p == "+":
                return power + 1
            if p == "-":
                return max(0, power - 1)
            return power

        power: int = 10
        ptr: int = 1
        score: int = 0

        for _ in range(10):
            for t in track:
                power = update_power(power, t, plan[ptr])
                score += power
                ptr = max(1, (ptr + 1) % len(plan))

        return (score, plan[0])
    
    ranks: List[tuple[int, str]] = [calc_score(plan) for plan in plans]
    ranks.sort(reverse = True)
    ans: str = ""

    for _, name in ranks:
        ans += name

    return ans


def solve3() -> int:

    track: str = ""
    enemy: str = ""

    with open("input3.in") as fin:
        enemy = "".join(parse_plans(fin)[0])
        track = parse_track(fin)

    def calc_score(plan: str) -> int:

        def update_power(power: int, t: str, p: str) -> int:
            if t == "+":
                return power + 1
            if t == "-":
                return max(0, power - 1)
            if p == "+":
                return power + 1
            if p == "-":
                return max(0, power - 1)
            return power
        
        power: int = 10
        ptr: int = 1
        score: int = 0
        psc: int = 0
        st: list[tuple[int, int]] = []
        rem: int = 2024
        
        while rem > 0:

            sc: int = 0

            for t in track:
                power = update_power(power, t, plan[ptr])
                sc += power
                ptr = max(1, (ptr + 1) % len(plan))
            
            delta: int = sc - psc
            score += sc
            psc = sc
            rem -= 1

            if st and (ptr, delta) in st:
                st = st[st.index((ptr, delta)):]
                break

            st.append((ptr, delta))

        ptr = 1 % len(st)

        while rem:
            psc += st[ptr][1]
            score += psc
            rem -= 1
            ptr = (ptr + 1) % len(st)
        
        return score
    
    target: int = calc_score(enemy)
    avai: dict[str, int] = {"+" : 5, "-" : 3, "=" : 3}

    def dfs(path: str) -> int:
        if len(path) == 12:
            return 1 if calc_score(path) > target else 0

        got: int = 0

        for op, rem in avai.items():
            if rem:
                avai[op] -= 1
                got += dfs(path + op)
                avai[op] += 1

        return got

    return dfs("A")


if __name__ == "__main__":
    ans1 = solve1()
    print(f"{ans1=}")

    ans2 = solve2()
    print(f"{ans2=}")

    ans3 = solve3()
    print(f"{ans3=}")

    print("Ayoooo!")
