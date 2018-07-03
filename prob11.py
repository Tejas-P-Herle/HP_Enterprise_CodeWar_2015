from math import sqrt


def main():
    pts = input().split()
    pts = [(float(x), float(y)) for x, y in zip(pts[::2], pts[1::2])]
    
    if slope(pts[0][0], pts[1][0], pts[0][1], pts[1][1]) == slope(pts[1][0], pts[2][0], pts[1][1], pts[2][1]):
        print("Collinear.")
        return
    dist_ab = distance(pts[0][0], pts[1][0], pts[0][1], pts[1][1])
    dist_bc = distance(pts[1][0], pts[2][0], pts[1][1], pts[2][1])
    dist_ca = distance(pts[0][0], pts[2][0], pts[0][1], pts[2][1])

    if (dist_ab == dist_bc == dist_ca):
        print("Equilateral triangle.")
    elif (dist_ab == dist_bc or dist_ab == dist_ca or dist_bc == dist_ca):
        print("Isosceles triangle.")
    else:
        print("Scalene traingle.")

def slope(x1, x2, y1, y2):
    return (y2 - y1) / (x2 - x1)

def distance(x1, x2, y1, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if __name__ == "__main__":
    main()