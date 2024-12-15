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


def correct_sum(rules, lines):
    total = 0
    incorrects = []
    for i in range(len(lines)):
        line_split = lines[i].split(",")
        valid = False
        for num in line_split:
            before = rules[num]
            for j in before:
                try:
                    index = line_split.index(j)
                    if index > line_split.index(num):
                        continue
                    else:
                        valid = True
                        break
                except ValueError:
                    continue
        if valid:
            incorrects.append(line_split)
    def find_incorrect(rules1, line):
        for char in line:
            before1 = rules1[char]
            for k in before1:
                try:
                    index1 = line.index(k)
                    index2 = line.index(char)
                    if index1 > line.index(char):
                        continue
                    else:
                        return True, index1, index2
                except ValueError:
                    continue
        return False, -1, -1

    for incorrect in incorrects:
        cond = find_incorrect(rules, incorrect)
        while cond[0]:
            incorrect[cond[1]], incorrect[cond[2]] = incorrect[cond[2]], incorrect[cond[1]]
            cond = find_incorrect(rules, incorrect)
        total += int(incorrect[len(incorrect) // 2])
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
        correct_sum(rules_dict, print_line)


if __name__ == "__main__":
    main()