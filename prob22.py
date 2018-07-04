matrix = []
min_time = 10**100
shortest_path = ""

def main():
    global matrix, min_time
    for _ in range(4):
        matrix.append([int(val) for val in input().split()])
    find_path(0, 0, matrix[0][0], "")
    print("The shortest path is {}".format(shortest_path))
    path_tiles, sum_ = find_path_tiles()
    print("Time taken is {}={} hrs".format("+".join(path_tiles), sum_))

def find_path_tiles():
    tiles = [matrix[0][0]]
    i, j = 0, 0
    for char in shortest_path:
        if char == "D":
            i += 1
            j += 1
        elif char == "B":
            i += 1
        else:
            j += 1
        tiles.append(matrix[i][j])
    return [str(val) for val in tiles], sum(tiles)

def find_path(i, j, total_time, path):
    global min_time
    global shortest_path
    if (i, j) == (3, 3):
        total_time += matrix[3][3]
        if total_time < min_time:
            min_time = total_time
            shortest_path = path
    for x, y, time in get_neighbours(i, j):
        if total_time + time < min_time:
            diry, dirx = (x-i), (y-j)
            if dirx and diry:
                dir_ = "D"
            elif dirx:
                dir_ = "R"
            else:
                dir_ = "B"
            find_path(x, y, total_time + time, path + dir_)

def get_neighbours(i, j):
    neighbours = []
    if i < 3 and j < 3:
        neighbours.append((i+1, j+1, matrix[i+1][j+1]))
    if i < 3:
        neighbours.append((i+1, j, matrix[i+1][j]))
    if j < 3:
        neighbours.append((i, j+1, matrix[i][j+1]))
    return neighbours

if __name__ == "__main__":
    main()