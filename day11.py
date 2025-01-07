from collections import Counter, defaultdict


def get_stones(stones_arr):
    stones = [int(stone) for stone in stones_arr]
    for i in range(25):
        temp_stones = []
        for stone in stones:
            if stone == 0:
                temp_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                s = str(stone)
                temp_stones.append(int(s[:len(s) // 2]))
                temp_stones.append(int(s[len(s) // 2:]))
            else:
                temp_stones.append(stone * 2024)
        stones = temp_stones
    print(len(stones))


def get_stones_cache(stones_arr):
    stones = Counter([int(stone) for stone in stones_arr])
    for i in range(75):
        temp_stones = defaultdict(int)
        for key, val in stones.items():
            if key == 0:
                temp_stones[1] += val
            elif len(str(key)) % 2 == 0:
                temp_stones[int(str(key)[:len(str(key)) // 2])] += val
                temp_stones[int(str(key)[len(str(key)) // 2:])] += val
            else:
                temp_stones[key * 2024] += val
        stones = temp_stones
    print(sum(stones.values()))


def main():
    with open("inputs/day11.txt", 'r') as file:
        arr = file.read().strip().split(" ")
    get_stones(arr)
    get_stones_cache(arr)


if __name__ == "__main__":
    main()
