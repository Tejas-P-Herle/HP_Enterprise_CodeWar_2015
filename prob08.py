from math import sqrt

MIN_TRIPLET_SUM = 12

def main():
    triplet_sum = int(input())

    if triplet_sum < MIN_TRIPLET_SUM:
        print("INVALID INPUT")
        return -1

    min_diff = None
    triplet = None
    a = 1
    b = 1
    diff = None
    while True:
        while True:
            b += 1
            if b == triplet_sum - 5:
                break
            c_sq = a*a + b*b
            c = sqrt(c_sq)
            if c - int(c) != 0:
                continue
            if c > triplet_sum - 5:
                break
            diff = abs(triplet_sum - (a+b+c))
            if not min_diff or diff < min_diff:
                min_diff = diff
                triplet = (a, b, int(c))
            if min_diff == 0:
                break
        if a >= triplet_sum - 5 or min_diff == 0:
            break
        a += 1
        b = a
    print("Pythagorean triplet: " + " ".join([str(val) for val in triplet]))
    print(sum(triplet))
                

if __name__ == "__main__":
    main()