def main():
    input_data = [float(val) for val in input().split()]
    speed, length = sorted(input_data[:-1]), input_data[-1]
    print("{} minutes".format((length / speed[3]) + (length / speed[0]) + (3 * (length / speed[2]))))

if __name__ == "__main__":
    main()