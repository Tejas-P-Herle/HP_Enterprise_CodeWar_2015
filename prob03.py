def main():
    # Get input
    _ = input()
    numbers = [int(num) for num in input().split()]

    # Calculate square of sum of numbers
    sq_sum_num = sum(numbers) ** 2

    # Calculate the sum of square of the numbers
    sum_num_sq = sum([num ** 2 for num in numbers])

    # Find diffrence in values
    diff = abs(sq_sum_num - sum_num_sq)

    # Print diffenece in values
    print(diff)

if __name__ == "__main__":
    main()