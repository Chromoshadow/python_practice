import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load


def main():
    gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life = load("life_expectancy_years.csv")

    year = "1900"

    common = gdp.index.intersection(life.index)
    data = pd.DataFrame({
        "GDP": gdp.loc[common, year],
        "Life": life.loc[common, year],
    }).dropna()

    data = data[data["GDP"] > 0]

    fig, ax = plt.subplots(figsize=(10, 10))

    ax.scatter(data["GDP"], data["Life"])
    ax.set_xscale("log")
    ax.set_title(year)
    ax.set_xlabel("Gross domestic product")
    ax.set_ylabel("Life expectancy")
    ax.set_xlim(left=data["GDP"].min() * 0.9)
    ax.xaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f"{x/1000:g}k")
    )

    plt.show()


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
