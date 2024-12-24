def checksum(line):
    curr_index = 0
    ordered_block = []
    for i in range(len(line)):
        if i % 2 == 0:
            ordered_block += [str(curr_index)] * int(line[i])
            curr_index += 1
        else:
            ordered_block += ["."] * int(line[i])
    l = ordered_block.index(".")
    r = len(ordered_block) - 1
    while l != r:
        ordered_block[l], ordered_block[r] = ordered_block[r], "."
        try:
            while ordered_block[l] != ".":
                l += 1
        except IndexError:
            break
        while ordered_block[r] == ".":
            r -= 1
    last_instance = len(ordered_block) - 1 - ordered_block[::-1].index(".")
    first_instance = ordered_block.index(".")
    fixed = ordered_block[:first_instance] + ordered_block[last_instance+1:][::-1]
    total = 0
    for i in range(len(fixed)):
        total += i * int(fixed[i])
    print(total)


def main():
    with open("inputs/day9.txt", "r") as file:
        line = file.read().strip()
    checksum(line)


if __name__ == "__main__":
    main()