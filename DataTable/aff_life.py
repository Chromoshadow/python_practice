import argparse
import matplotlib.pyplot as plt
from load_csv import load


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    df = load(args.path)

    df.set_index("country").loc["France"].plot()
    plt.title("France life expectancy")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
