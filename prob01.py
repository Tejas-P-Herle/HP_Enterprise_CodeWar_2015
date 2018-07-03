def main():
    # Get input
    length, breadth, depth = [float(val) for val in input().split()]

    # Print volume
    print(length * breadth * depth)

if __name__ == "__main__":
    main()