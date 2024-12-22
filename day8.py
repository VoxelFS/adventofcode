from collections import defaultdict


def anti_node_locations(antennas, max_x, max_y):
    unique_locations = set()
    for key, val in antennas.items():
        for p in val:
            for p2 in val:
                if p != p2:
                    dX = p[0] - p2[0]
                    dY = p[1] - p2[1]
                    anti_node1 = (p[0] + dX, p[1] + dY)
                    if 0 <= anti_node1[0] <= max_x and 0 <= anti_node1[1] <= max_y:
                        unique_locations.add(anti_node1)
    return len(unique_locations)


def all_node_locations(antennas, max_x, max_y):
    unique_locations = set()
    for key, val in antennas.items():
        for p in val:
            for p2 in val:
                if p != p2:
                    dX = p2[0] - p[0]
                    dY = p2[1] - p[1]
                    anti_node = (p[0], p[1])
                    while 0 <= anti_node[0] <= max_x and 0 <= anti_node[1] <= max_y:
                        unique_locations.add(anti_node)
                        anti_node = (anti_node[0] + dX, anti_node[1] + dY)
    return len(unique_locations)


def main():
    antenna_dict = defaultdict(list)
    with open("inputs/day8.txt", 'r') as file:
        arr = file.read().strip().split("\n")
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != ".":
                antenna_dict[arr[i][j]].append((j, i))
    max_x = len(arr[0]) - 1
    max_y = len(arr) - 1
    print(anti_node_locations(antenna_dict, max_x, max_y))
    print(all_node_locations(antenna_dict, max_x, max_y))


if __name__ == "__main__":
    main()
