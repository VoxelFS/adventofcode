import re


def find_mul(data) -> int:
    pattern: str = r"mul\(\d+,\d+\)"
    total: int = 0
    matches = re.findall(pattern, data)
    for match in matches:
        d_match = re.findall("(\\d+)", match)
        total += int(d_match[0]) * int(d_match[1])
    return total


def find_mul2(data) -> int:
    pattern: str = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    flag: bool = True
    total: int = 0
    matches = re.findall(pattern, data)
    for match in matches:
        if match == "don\'t()":
            flag = False
        elif match == "do()":
            flag = True
        else:
            if flag:
                d_match = re.findall("\\d+", match)
                total += int(d_match[0]) * int(d_match[1])
    return total


def main():
    total: int = 0
    total2: int = 0
    with open('inputs/day3.txt', 'r') as file:
        for line in file:
            total += find_mul(line)
            total2 += find_mul2(line)
    print(total)
    print(total2)


if __name__ == '__main__':
    main()
