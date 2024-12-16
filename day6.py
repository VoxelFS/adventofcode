def get_unique(map_arr, start):
    unique_locations = {start}
    y, x = start
    direction = "^"
    while True:

        if direction == "^":
            unique_locations.add((y, x))
            if y > 0:
                if map_arr[y-1][x] == "#":
                    direction = ">"
                else:
                    y -= 1
            else:
                break

        if direction == ">":
            unique_locations.add((y, x))
            if x < len(map_arr[y]) - 1:
                if map_arr[y][x+1] == "#":
                    direction = "V"
                else:
                    x += 1
            else:
                break

        if direction == "V":
            unique_locations.add((y, x))
            if y < len(map_arr) - 1:
                if map_arr[y+1][x] == "#":
                    direction = "<"
                else:
                    y += 1
            else:
                break

        if direction == "<":
            unique_locations.add((y, x))
            if x > 0:
                if map_arr[y][x-1] == "#":
                    direction = "^"
                else:
                    x -= 1
            else:
                break

    print(len(unique_locations))


def get_loops(map_arr, start):
    y, x = start
    direction = "^"
    counter = 0
    valid = True
    while True:

        if counter >= 100000:
            print("inf loop!")
            valid = False
            break

        if direction == "^":
            counter += 1
            if y > 0:
                if map_arr[y-1][x] == "#":
                    direction = ">"
                else:
                    y -= 1
            else:
                break

        if direction == ">":
            counter += 1
            if x < len(map_arr[y]) - 1:
                if map_arr[y][x+1] == "#":
                    direction = "V"
                else:
                    x += 1
            else:
                break

        if direction == "V":
            counter += 1
            if y < len(map_arr) - 1:
                if map_arr[y+1][x] == "#":
                    direction = "<"
                else:
                    y += 1
            else:
                break

        if direction == "<":
            counter += 1
            if x > 0:
                if map_arr[y][x-1] == "#":
                    direction = "^"
                else:
                    x -= 1
            else:
                break
        counter += 1
    return valid


def main():
    total = 0
    with open("inputs/day6.txt", 'r') as file:
        arr = file.read().strip().split("\n")
        start = (0, 0)
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == "^":
                    start = (i, j)
                    break
        # get_unique(arr, start)
        full_map = [list(a) for a in arr]
        for i in range(len(full_map)):
            for j in range(len(full_map)):
                if full_map[i][j] == "#" or full_map[i][j] == "^":
                    continue
                full_map[i][j] = "#"
                if not get_loops(full_map, start):
                    total += 1
                full_map[i][j] = "."
        print(total)


if __name__ == "__main__":
    main()
