from collections import deque


def total_score(arr, point):
    q = deque([point])
    seen = {point}
    top = 0
    while q:
        cX, cY = q.popleft()
        for nX, nY in [(cX + 1, cY), (cX - 1, cY), (cX, cY + 1), (cX, cY - 1)]:
            if nX < 0 or nX > len(arr[0]) - 1 or nY < 0 or nY > len(arr) - 1:
                continue
            if int(arr[nX][nY]) != int(arr[cX][cY]) + 1:
                continue
            if (nX, nY) in seen:
                continue
            seen.add((nX, nY))
            if int(arr[nX][nY]) == 9:
                top += 1
            else:
                q.append((nX, nY))
    return top


def total_rating(arr, point):
    q = deque([point])
    top = 0
    while q:
        cX, cY = q.popleft()
        for nX, nY in [(cX + 1, cY), (cX - 1, cY), (cX, cY + 1), (cX, cY - 1)]:
            if nX < 0 or nX > len(arr[0]) - 1 or nY < 0 or nY > len(arr) - 1:
                continue
            if int(arr[nX][nY]) != int(arr[cX][cY]) + 1:
                continue
            if int(arr[nX][nY]) == 9:
                top += 1
            else:
                q.append((nX, nY))
    return top


def main():
    total = 0
    rating_total = 0
    with open("inputs/day10.txt", 'r') as file:
        arr = file.read().strip().split("\n")
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "0":
                point = (i, j)
                total += total_score(arr, point)
                rating_total += total_rating(arr, point)
    print(total)
    print(rating_total)


if __name__ == "__main__":
    main()
