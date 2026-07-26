import argparse
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load


def parse_population(x):
    """
    Convert a population value with an metric suffix into a numeric value.

    Supported suffixes:
        - 'k': thousand (1e3)
        - 'M': million (1e6)
        - 'G': billion (1e9)

    If the input is missing (NaN or None), it is returned unchanged.

    Args:
        x: A population value as a string or numeric type. Examples include
           "500", "2.5k", "3M", "1.2G", or NaN.

    Returns:
        float: The parsed numeric value.
        NaN/None: Returned unchanged if the input is missing.
    """

    multipliers = {
        "k": 1e3,
        "M": 1e6,
        "B": 1e9
    }

    if pd.isna(x):
        return (x)
    x = str(x).strip()
    suffix = x[-1]
    if suffix in multipliers:
        return float(x[:-1]) * multipliers[suffix]
    else:
        return float(x)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    df = load(args.path)

    for col in df.columns[1:]:
        df[col] = df[col].apply(parse_population)

    df = df.set_index("country")

    ax = df.loc[["France", "Belgium"], "1800":"2050"].T.plot()
    ax.set_title("Population projection")
    ax.set_xlabel("Year")
    ax.set_ylabel("Population")

    ax.yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f"{x/1e6:.0f} M")
    )

    plt.show()


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
