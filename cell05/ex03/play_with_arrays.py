def main():
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    new_array = [x + 2 for x in original_array if x > 5]
    new_set = {x + 2 for x in original_array if x > 5}
    print(f"{original_array}")
    print(f"{new_set}")

if __name__ == "__main__":
    main()
