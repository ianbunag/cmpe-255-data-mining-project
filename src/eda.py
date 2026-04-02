import pandas
import pandas as pd


def understand_features(df: pandas.DataFrame, measurements: dict, descriptions: dict) -> pd.DataFrame:
    df.info()
    return pd.DataFrame({
        "Measurement Type": measurements,
        "Description": descriptions
    })

def assess_features(df: pandas.DataFrame, measurements: dict) -> pd.DataFrame:
    df_assessment = df.copy()
    df_assessment = df_assessment.map(lambda row: row.strip().lower() if isinstance(row, str) else row)

    df_null_counts = {}
    df_null_percentages = {}
    df_duplicates = {}
    df_duplicate_percentages = {}

    for key in df_assessment.columns.tolist():
        null_count = df_assessment[key].isna().sum()
        df_null_counts[key] = null_count

        null_percentage = round((null_count / len(df_assessment)) * 100, 2)
        df_null_percentages[key] = null_percentage

        duplicates = df_assessment[key].duplicated()
        duplicate_count = duplicates.sum()
        df_duplicates[key] = duplicate_count

        duplicate_percentage = round((duplicate_count / len(df_assessment)) * 100, 2)
        df_duplicate_percentages[key] = duplicate_percentage

    return pd.DataFrame({
        'Null Count': df_null_counts,
        'Null Percentage': df_null_percentages,
        'Measurement Type': measurements,
        'Duplicate Count': df_duplicates,
        'Duplicate Percentage': df_duplicate_percentages
    })
