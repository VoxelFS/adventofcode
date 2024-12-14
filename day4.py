def xmas_count(arr):
    total = 0
    target = "XMAS"
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != "X":
                continue
            # top
            if i > 2:
                word = "".join([arr[i-x][j] for x in range(0, 4)])
                if word == target:
                    total += 1

            # bottom
            if i < (len(arr) - 3):
                word = "".join([arr[i+x][j] for x in range(0, 4)])
                if word == target:
                    total += 1

            # left
            if j > 2:
                word = "".join([arr[i][j-x] for x in range(0, 4)])
                if word == target:
                    total += 1

            # right
            if j < (len(arr) - 3):
                word = "".join([arr[i][j+x] for x in range(0, 4)])
                if word == target:
                    total += 1

            # dia top left
            if i > 2 and j > 2:
                word = "".join([arr[i-x][j-x] for x in range(0, 4)])
                if word == target:
                    total += 1

            # dia top right
            if i > 2 and j < (len(arr) - 3):
                word = "".join([arr[i-x][j+x] for x in range(0, 4)])
                if word == target:
                    total += 1

            # dia bot left
            if i < (len(arr) - 3) and j > 2:
                word = "".join([arr[i+x][j-x] for x in range(0, 4)])
                if word == target:
                    total += 1

            # dia bot right
            if i < (len(arr) - 3) and j < (len(arr) - 3):
                word = "".join([arr[i+x][j+x] for x in range(0, 4)])
                if word == target:
                    total += 1
    return total


def cross_mas_count(arr):
    total = 0
    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr[i]) - 1):
            if arr[i][j] != "A":
                continue

            m_count = 0
            s_count = 0
            top_left = arr[i-1][j-1]
            top_right = arr[i-1][j+1]
            bot_left = arr[i+1][j-1]
            bot_right = arr[i+1][j+1]
            temp_arr = [top_left, top_right, bot_right, bot_left]
            for char in temp_arr:
                if char == "M":
                    m_count += 1
                if char == "S":
                    s_count += 1
            if m_count == 2 and s_count == 2:
                if top_right != bot_left and top_left != bot_right:
                    total += 1
    return total


def main():
    arr = []
    with open("inputs/day4.txt", 'r') as file:
        for line in file:
            temp_arr = []
            for char in line:
                if char == "\n":
                    continue
                temp_arr.append(char)
            arr.append(temp_arr)
    print(xmas_count(arr))
    print(cross_mas_count(arr))


if __name__ == "__main__":
    main()
