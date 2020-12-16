
import argparse


def print_steps(first: int, second: int) -> None:
    row, col = 0, 0
    while col < second - 1:
        print(row, col)
        col += 1
    while row < first - 1:
        print(row, col)
        row += 1
    while col > 0:
        print(row, col)
        col -= 1
    while row > 0:
        print(row, col)
        if row == 1:
            col += 1
            break
        row -= 1
    print(row, col)


def main() -> None:
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='integers for the snail')

    args = parser.parse_args()

    int_vars = vars(args)['integers']

    if len(int_vars) != 2:
        raise Exception('Your have to add 2 integers! for example `python snail_game.py 3 3`')

    print_steps(int_vars[0], int_vars[1])


if __name__ == '__main__':
    main()
