ordered_strings = []

def main():
    input_count = int(input())
    strings = []

    for i in range(input_count):
        strings.append(input())

    for string in strings:
        insert_in_ordered_list(find_int(string), string)

    print("\n".join([pair[1] for pair in ordered_strings]))

def insert_in_ordered_list(value, string):
    if not ordered_strings:
        ordered_strings.append((value, string))
        return
    for i in range(len(ordered_strings)):
        if value < ordered_strings[i][0]:
            ordered_strings.insert(i, (value, string))
            return
    ordered_strings.append((value, string))

def find_int(string):
    start = -1
    for i, char in enumerate(string):
        if char.isdigit():
            if start == -1:
                start = i
        elif not char.isdigit() and start != -1:
            return int(string[start:i])
    return int(string[start:])


if __name__ == "__main__":
    main()