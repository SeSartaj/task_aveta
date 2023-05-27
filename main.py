from cat_mouse import catAndMouse


def main():
    queries = int(input("Enter the number of queries (1-100): "))

    if not (1 <= queries <= 100):
        raise ValueError("Number of queries should be between 1 and 100 (inclusive)")

    for _ in range(queries):
        x, y, z = map(int, input("Enter the positions of Cat A, Cat B, and Mouse C: ").split())
        result = catAndMouse(x, y, z)
        print(result)


if __name__ == "__main__":
    main()
