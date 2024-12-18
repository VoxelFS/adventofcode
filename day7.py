from itertools import product


def test_combo(nums, val, combo):
    result = nums[0]
    for i in range(1, len(nums)):
        if combo[i - 1] == "+":
            result += nums[i]
        elif combo[i - 1] == "*":
            result *= nums[i]
        elif combo[i - 1] == "|":
            result = int(f"{result}{nums[i]}")
    return result == val


def part2(nums, val):
    total = 0
    for combo in product("+*|", repeat=len(nums) - 1):
        if test_combo(nums, val, combo):
            total += val
            break
    return total


def main():
    total = 0
    total2 = 0
    with open("inputs/day7.txt", 'r') as file:
        arr = file.read().strip().split("\n")
        for a in arr:
            a = a.split(" ")
            val = int(a[0][:-1])
            nums = [int(num) for num in a[1:]]
            for combo in product("+*", repeat=len(nums) - 1):
                if test_combo(nums, val, combo):
                    total += val
                    break
            total2 += part2(nums, val)
    print(total)
    print(total2)


if __name__ == "__main__":
    main()
