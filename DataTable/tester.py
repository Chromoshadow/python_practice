# from load_csv import load
# print(load("life_expectancy_years.csv"))

# -----------------------------------------------------

import argparse
from load_csv import load


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    print(load(args.path))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
