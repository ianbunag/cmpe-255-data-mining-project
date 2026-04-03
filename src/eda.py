import pandas as pd

from pandas.api.types import is_numeric_dtype

def understand_features(df: pd.DataFrame, measurements: dict, descriptions: dict) -> pd.DataFrame:
    df.info()
    return pd.DataFrame({
        "Measurement Type": measurements,
        "Description": descriptions
    })

def assess_features(df: pd.DataFrame, measurements: dict) -> pd.DataFrame:
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

        duplicates = df_assessment[key].dropna().duplicated()
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

def find_central_tendency(df: pd.DataFrame, measurements: dict) -> pd.DataFrame:
    means = {}
    medians = {}
    skews = {}
    skew_directions = {}

    for key in df.columns:
        if not is_numeric_dtype(df[key]):
            medians[key] = 'N/A'
            means[key] = 'N/A'
            skews[key] = 'N/A'
            skew_directions[key] = 'N/A'
            continue

        means[key] = round(df[key].mean(), 2)
        medians[key] = round(df[key].median(), 2)
        skew = round(df[key].skew(), 2)
        skews[key] = skew

        if -0.5 <= skew <= 0.5:
            skew_directions[key] = 'Symmetrical'  # Mean = Median
        elif -1 <= skew < -0.5:
            skew_directions[key] = 'Moderately Left Skewed'  # Mean < Median
        elif skew < -1:
            skew_directions[key] = 'Highly Left Skewed'  # Mean < Median
        elif 0.5 < skew <= 1:
            skew_directions[key] = 'Moderately Right Skewed'  # Mean > Median
        elif skew > 1:
            skew_directions[key] = 'Highly Right Skewed'  # Mean > Median

    return pd.DataFrame({
        'Measurement Type': measurements,
        'Mean': means,
        'Median': medians,
        'Skewness': skews,
        'Skew Direction': skew_directions
    })