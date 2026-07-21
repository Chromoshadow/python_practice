import sys


def odd_even(number):
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


def main():
    args = sys.argv[1:]

    if len(args) == 0:
        return
    if len(args) > 1:
        raise AssertionError("more than one argument is provided")
    try:
        number = int(args[0])
    except ValueError:
        raise AssertionError("argument is not an integer")

    odd_even(number)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
