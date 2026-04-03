import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

from pandas.api.types import is_numeric_dtype
from scipy import stats
from sklearn.preprocessing import MinMaxScaler


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

def find_central_tendency(df: pd.DataFrame, measurements: dict, rounding : int | None = 2) -> pd.DataFrame:
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

        means[key] = df[key].mean()
        medians[key] = df[key].median()
        skew = df[key].skew()
        skews[key] = skew

        if rounding is not None:
            means[key] = round(means[key], rounding)
            medians[key] = round(medians[key], rounding)
            skew = round(skew, rounding)

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

def measure_variability(df: pd.DataFrame, rounding: int | None = 2) -> pd.DataFrame:
    table_columns = ['Feature', 'q1', 'q3', 'iqr', 'std_dev', 'cv', 'lower_limit', 'upper_limit']
    table_rows = []

    for key in df.columns:
        if not is_numeric_dtype(df[key]):
            continue

        v = df[key].dropna()
        q1 = np.percentile(v, 25)
        q3 = np.percentile(v, 75)
        iqr = stats.iqr(v)
        lower_limit = q1 - 1.5 * iqr
        upper_limit = q3 + 1.5 * iqr
        std_dev = np.std(v)
        cv = stats.variation(v)

        if rounding is not None:
            q1 = round(q1, rounding)
            q3 = round(q3, rounding)
            iqr = round(iqr, rounding)
            lower_limit = round(lower_limit, rounding)
            upper_limit = round(upper_limit, rounding)
            std_dev = round(std_dev, rounding)
            cv = round(cv, rounding)

        table_rows.append([
            key,
            q1,
            q3,
            iqr,
            std_dev,
            cv,
            lower_limit,
            upper_limit
        ])

    return pd.DataFrame(data=table_rows, columns=table_columns)

# Histogram guide:https://www.stratascratch.com/blog/how-to-create-a-matplotlib-histogram
def visualize_distribution(df: pd.DataFrame):
    for key in df.columns:
        if not is_numeric_dtype(df[key]):
            continue
        v = df[key].dropna()
        plt.figure(figsize=(12, 4))
        plt.subplot(1, 2, 1)
        plt.title("Histogram: " + key)
        plt.xlabel(key)
        plt.hist(v, alpha=0.6, bins=20, color='lightsalmon', edgecolor='black')

        plt.subplot(1, 2, 2)
        plt.title("Box plot: " + key)
        plt.xlabel(key)
        plt.boxplot(v)
        plt.show()

def correlate_features(df: pd.DataFrame, **kwargs):
    relevance = kwargs.get('relevance', 0.7)
    font_size = kwargs.get('font_size', None)

    corr = df.corr(numeric_only=True)
    plt.figure(figsize=(15, 10))
    plt.title('Air Quality correlation heat map')
    sns.heatmap(data=corr, annot=True, cmap='coolwarm', annot_kws={ 'size': font_size })
    plt.show()

    plt.figure(figsize=(15, 10))
    plt.title('Air Quality relevant correlation heat map')
    sns.heatmap(data=corr, annot=True, cmap='coolwarm', annot_kws={ 'size': font_size }, mask=np.abs(corr) < relevance)
    plt.show()

def scatter_plot_features(df: pd.DataFrame, scatter_plots: list):
    for keys in scatter_plots:
        plt.figure()
        sns.regplot(
            data=df,
            x=keys[0],
            y=keys[1],
            scatter_kws={'alpha': 0.5},
            line_kws={'color': 'gold'}
        )
        plt.title(f"Correlation of {keys[0]} and {keys[1]}")
        plt.show()

def line_plot_features(df: pd.DataFrame, line_plots: list):
    df_scaled = df.copy()
    features = list(set(item for lineplot in line_plots for item in lineplot))
    scaler = MinMaxScaler()
    df_scaled[features] = scaler.fit_transform(df[features])
    for keys in line_plots:
        plt.figure()
        for key in keys:
            sns.lineplot(data=df_scaled, x=df.index, y=key, label=key, alpha=0.8)

        plt.title(f"Trend between {keys[0]} and {keys[1]}")
        plt.xlabel('Index')
        plt.grid(True, alpha=0.3)
        plt.show()
