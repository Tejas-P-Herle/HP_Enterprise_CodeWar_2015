def main():
    try:
        print(eval(input()))
    except SyntaxError:
        print("INVALID INPUT")

if __name__ == "__main__":
    main()