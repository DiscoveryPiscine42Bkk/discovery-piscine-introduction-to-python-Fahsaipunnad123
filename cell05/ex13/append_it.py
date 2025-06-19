import sys

def main():
    if len(sys.argv) == 1:
        print("none")
        return

    printed = False
    for arg in sys.argv[1:]:
        if not arg.endswith("ism"):
            print(arg + "ism")
            printed = True

    if not printed:
        print("none")

if __name__ == "__main__":
    main()
