matrix = []
dictionary = None
matches = []

def main():
    global matrix, dictionary

    for _ in range(int(input())):
        matrix.append(input().split())

    dictionary = []
    for _ in range(int(input())):
        dictionary.append(input())
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            neighbours = get_neighbours(i, j)
            for x, y, char in neighbours:
                new_str = matrix[i][j] + char
                if any([word.startswith(new_str) for word in dictionary]):
                    find_matches(i + (x-i), j + (y-j), new_str, x-i, y-j)

    print(len(matches))
    print("\n".join(matches))

def find_matches(i, j, string, dirx, diry):
    global matches
    i, j = i + dirx, j + diry
    if i == len(matrix) or j == len(matrix):
        return
    new_str = string + matrix[i][j]
    if new_str in dictionary and new_str not in matches:
        matches.append(new_str)
        return
    if any([word.startswith(new_str) for word in dictionary]):
        find_matches(i, j, new_str, dirx, diry)

def get_neighbours(i, j):
    neighbours = []
    start_i = i-1 if i != 0 else 0
    start_j = j-1 if j != 0 else 0
    end_i = i+2 if i != len(matrix) - 1 else len(matrix)
    end_j = j+2 if j != len(matrix) - 1 else len(matrix)
    for x in range(start_i, end_i):
        for y in range(start_j, end_j):
            if (x, y) == (i, j):
                continue
            neighbours.append((x, y, matrix[x][y]))
    return neighbours
    
if __name__ == "__main__":
    main()

