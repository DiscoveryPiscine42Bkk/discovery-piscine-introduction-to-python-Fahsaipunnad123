import sys

def main():
    if len(sys.argv) != 3:
        print("none")
        return

    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        print(list(range(start, end + 1)))
    except ValueError:
        print("none")

if __name__ == "__main__":
    main()