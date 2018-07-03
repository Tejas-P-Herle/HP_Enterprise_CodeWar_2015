def main():
    string = list(input())
    shift = int(input())

    for char in string:
        if char.isalpha():
            if char.islower():
                diff = 97
            elif char.isupper():
                diff = 65
            char = ord(char)
            char = (char - diff) + shift
            while char < 0:
                char = 26 + char
            if char > 25:
                char = char % 26

            char += diff
            char = chr(char)
        print(char, end="")
    print()

if __name__ == "__main__":
    main()