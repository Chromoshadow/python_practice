import pandas as pd
from pandas.errors import EmptyDataError, ParserError


def load(path: str) -> pd.DataFrame:
    """
    Reads a CSV file, prints and returns its dimensions.

    Parameters:
        path (str): Path to the CSV file.

    Returns:
        pandas dataframe
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df

    except FileNotFoundError:
        raise AssertionError("File not found.")
    except EmptyDataError:
        raise AssertionError("The CSV file is empty.")
    except ParserError:
        raise AssertionError("The CSV file is malformed.")
    except Exception as e:
        raise AssertionError(str(e))
