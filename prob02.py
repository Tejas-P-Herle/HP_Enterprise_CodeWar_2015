def main():
    # Get input
    temp_farenheat = float(input())

    # Calculate degree celsius
    temp_celsius = (5/9) * (temp_farenheat - 32)

    # Print temperature in degree celsius
    print(temp_celsius)

if __name__ == "__main__":
    main()