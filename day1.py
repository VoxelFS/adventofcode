from collections import Counter


def get_count(left: list[int], right: list[int]) -> int:
    left.sort()
    right.sort()
    count: int = 0
    for i in range(len(left)):
        distance: int = abs(left[i] - right[i])
        count += distance
    return count


def get_freq(left: list[int], right: list[int]) -> int:
    count: int = 0
    right_freq: dict[int, int] = Counter(right)
    for num in left:
        try:
            freq: int = right_freq[num]
            count += num * freq
        except KeyError:
            continue
    return count


def main():
    left: list[int] = []
    right: list[int] = []
    with open('inputs/day1.txt', 'r') as file:
        for line in file:
            s: list[str] = line.split("   ")
            left.append(int(s[0]))
            right.append(int(s[1].rstrip("\n")))
    print(get_count(left, right))
    print(get_freq(left, right))


if __name__ == "__main__":
    main()
