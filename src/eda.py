import pandas
import pandas as pd


def understand_features(df: pandas.DataFrame, measurements: dict, descriptions: dict) -> pd.DataFrame:
    df.info()
    return pd.DataFrame({
        "Measurement Type": measurements,
        "Description": descriptions
    })
