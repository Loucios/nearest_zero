# https://github.com/Loucios/nearest_zero

from solution.solution import NearestZero


def main():
    try:
        length_street = int(input())
        street = [int(house) for house in input().split()]
    except ValueError as e:
        print(f'Wrong input {e}')
        return

    nearest_zero = NearestZero(length_street, street)

    print(nearest_zero)


if __name__ == "__main__":
    main()
