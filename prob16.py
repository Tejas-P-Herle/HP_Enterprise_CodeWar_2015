matrix = []

def main():
    global matrix
    square_dimentions = int(input())
    for _ in range(square_dimentions):
        matrix.append(input().split())

    is_one_ = False
    is_two_ = False

    for i in [i for i, char in enumerate(matrix[0]) if char == "1"]:
        if not is_one_:
            is_one_ = is_one(0, i)

    for i in [i for i, char in enumerate([row[0] for row in matrix]) if char == "2"]:
        if not is_two_:
            is_two_ = is_two(0, i)

    if is_one_ and is_two_:
        print("AMBIGUOUS")
    elif is_one_:
        print("1")
    elif is_two_:
        print("2")
    else:
        print("0")

def is_one(depth, i):
    len_matrix = len(matrix)
    if depth == len_matrix:
        return True
    start = i-1 if i != 0 else 0
    end = i+2 if i != len_matrix - 1 else len_matrix
    for i, char in enumerate(matrix[depth][start:end]):
        if char == "1" and is_one(depth+1, start + i):
            return True
    return False

def is_two(depth, i):
    len_matrix = len(matrix)
    if depth == len_matrix:
        return True
    start = i-1 if i != 0 else 0
    end = i+2 if i != len_matrix - 1 else len_matrix
    for i in [i for i, row in enumerate(matrix[start:end]) if row[depth] == "2"]:
        if is_two(depth+1, start + i):
            return True
    return False
    
if __name__ == "__main__":
    main()
