from collections import defaultdict


def middle_sum(rules, lines):
    total = 0
    for i in range(len(lines)):
        line_split = lines[i].split(",")
        valid = True
        for num in line_split:
            before = rules[num]
            for j in before:
                try:
                    index = line_split.index(j)
                    if index > line_split.index(num):
                        continue
                    else:
                        valid = False
                        break
                except ValueError:
                    continue
        if valid:
            total += int(line_split[len(line_split) // 2])

    print(total)


def main():
    arr = []
    with open("inputs/day5.txt", 'r') as file:
        arr = file.read().strip().split("\n")
        spacer = arr.index("")
        print_line = arr[spacer+1:]
        rules = arr[:spacer]

        rules_dict = defaultdict(list)
        for rule in rules:
            split = rule.split("|")
            rules_dict[split[0]].append(split[1])

        middle_sum(rules_dict, print_line)


if __name__ == "__main__":
    main()