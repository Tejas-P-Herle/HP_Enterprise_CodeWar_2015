def main():
    input()
    pts = [int(val) for val in input().split()]
    lines = [(pts[i*4], pts[i*4+1], pts[i*4+2], pts[i*4+3]) for i in range(len(pts)//4)]
    buffer = []
    for i in range(len(lines)):
        line_1 = lines[i]
        for j in range(i, len(lines)):
            line_2 = lines[j]
            buffer += find_intersection(*line_1, *line_2)

    print(len(buffer))
    print("\n".join([row[0] + " " + row[1] for row in buffer]))

def points_in_line(x, y, x1, y1, x2, y2, x3, y3, x4, y4):
    if ((x <= max(x1, x2) and x >= min(x3, x4))
        and (y <= max(y1, y2) and y >= min(y3, y4))):
        return True
    return False

def find_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    if (x1, y1, x2, y2) == (x3, y3, x4, y4):
        return []
    m1 = (y2-y1)/(x2-x1)
    m2 = (y4-y3)/(x4-x3)

    if m1 == m2:
        return []
    b1 = y1-m1*x1
    b2 = y3-m2*x3
    if m1 - m2:
        x = (b2 - b1) / (m1 - m2)
    else:
        return []
    y = m1 * x + b1
    if points_in_line(x, y, x1, y1, x2, y2, x3, y3, x4, y4):
        return [(str(x), str(y))]
    return []

if __name__ == "__main__":
    main()
