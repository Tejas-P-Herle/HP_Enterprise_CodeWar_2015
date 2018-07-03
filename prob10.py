matrix = []

def main():
    dimentions = [int(val) for val in input().split()]
    for _ in range(dimentions[0]):
        matrix.append(input().split())
    indexes = find_dollar()
    print("\n".join([" ".join(row) for row in replace_dollars(indexes)]))

def replace_dollars(indexes):
    resultant_matrix = []
    for i in range(len(matrix)):
        resultant_matrix.append([])
        for j in range(len(matrix[i])):
            if i in [point[0] for point in indexes] or j in [point[1] for point in indexes]:
                resultant_matrix[i].append("$")
            else:
                resultant_matrix[i].append(matrix[i][j])
    return resultant_matrix

def find_dollar():
    indexes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "$":
                indexes.append((i, j))
    return indexes

if __name__ == "__main__":
    main()