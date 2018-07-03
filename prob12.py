def main():
    _ = input()
    data = [float(val) for val in input().split()]

    max_val = find_max_val(data.copy())

    if max_val:
        print("Profit: " + str(max_val))
    else:
        print("Loss: " + str(find_min_val(data)))

def find_max_val(data):
    if not data:
        return None
    _max = max(data)
    _min = min(data)
    if data.index(_max) > data.index(_min):
        return _max - _min
    else:
        data.remove(_max)
        return find_max_val(data)

def find_min_val(data):
    _max = max(data)
    data.remove(_max)
    return _max - max(data)


if __name__ == "__main__":
    main()