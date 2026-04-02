from enum import Enum

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pandas.api.types import is_numeric_dtype
from sklearn.preprocessing import PowerTransformer
import seaborn as sns

PREFIX_SQRT = 'sqrt_'
PREFIX_LOG1P = 'log1p_'
PREFIX_CBRT = 'cbrt_'
PREFIX_YEO_JOHNSON = 'yeo_johnson_'

def compare_transformations(df: pd.DataFrame, columns: list[str] = []):
    df_transforms = df.copy()
    if len(columns) == 0:
        columns = df_transforms.columns

    skew = {}
    skew_sqrt = {}
    skew_log1p = {}
    skew_cbrt = {}
    skew_yeo_johnson = {}

    for feature in columns:
        if not is_numeric_dtype(df_transforms[feature]):
            skew[feature] = 'N/A'
            skew_sqrt[feature] = 'N/A'
            skew_log1p[feature] = 'N/A'
            skew_cbrt[feature] = 'N/A'
            skew_yeo_johnson[feature] = 'N/A'
            continue

        df_transforms[PREFIX_SQRT + feature] = np.sqrt(df_transforms[feature])
        df_transforms[PREFIX_LOG1P + feature] = np.log1p(df_transforms[feature])
        df_transforms[PREFIX_CBRT + feature] = np.cbrt(df_transforms[feature])
        power_transformer = PowerTransformer(method='yeo-johnson')
        df_transforms[PREFIX_YEO_JOHNSON + feature] = power_transformer.fit_transform(df_transforms[[feature]]).ravel()

        skew[feature] = round(df[feature].skew(), 2)
        skew_sqrt[feature] = round(df_transforms[PREFIX_SQRT + feature].skew(), 2)
        skew_log1p[feature] = round(df_transforms[PREFIX_LOG1P + feature].skew(), 2)
        skew_cbrt[feature] = round(df_transforms[PREFIX_CBRT + feature].skew(), 2)
        skew_yeo_johnson[feature] = round(df_transforms[PREFIX_YEO_JOHNSON + feature].skew(), 2)

    return pd.DataFrame({
        'Original': skew,
        'Square root': skew_sqrt,
        'Log transformation': skew_log1p,
        'Cube root': skew_cbrt,
        'Yeo-Johnson Transform': skew_yeo_johnson,
    })

def compare_skewness(df_original: pd.DataFrame, df_transformed: pd.DataFrame, transformations: dict):
    skew_original = {}
    skew_transformed = {}
    transformations = transformations.copy()

    for column in df_transformed.columns:
        if column in transformations:
            if isinstance(transformations[column], Enum):
                transformations[column] = transformations[column].value
        else:
            transformations[column] = 'None'

    for column in df_transformed.columns:
        if not is_numeric_dtype(df_original[column]):
            skew_original[column] = 'N/A'
            skew_transformed[column] = 'N/A'
            continue

        skew_original[column] = round(df_original[column].skew(), 2)
        skew_transformed[column] = round(df_transformed[column].skew(), 2)

    return pd.DataFrame({
        'Transformation': transformations,
        'Skewness (Original)': skew_original,
        'Skewness (Transformed)': skew_transformed
    })

def compare_distributions(df_original: pd.DataFrame, df_transformed: pd.DataFrame, columns: list[str]):
    for column in columns:
        fig, axes = plt.subplots(2, 2, figsize=(12, 8))

        plt.suptitle(column + ' diagrams', fontsize=20)
        axes[0, 0].hist(df_original[column], alpha=0.6, bins=20, color='lightsalmon', edgecolor='black')
        axes[0, 0].set_title('Histogram (Original)')
        axes[0, 0].set_xlabel(column)

        axes[0, 1].hist(df_transformed[column], alpha=0.6, bins=20, color='lightsalmon', edgecolor='black')
        axes[0, 1].set_title('Histogram (Transformed)')
        axes[0, 1].set_xlabel(column)

        df_original.plot(y=[column], ax=axes[1, 0], title='Line chart (Original)', kind='line')
        sns.regplot(data=df_original, x=df_original.index, y=column, ax=axes[1, 0], scatter=False,
                    color='lightblue')

        df_transformed.plot(y=[column], ax=axes[1, 1], title='Line chart (Log transformed)', kind='line')
        sns.regplot(data=df_transformed, x=df_transformed.index, y=column, ax=axes[1, 1], scatter=False,
                    color='lightblue')

        plt.tight_layout()
        plt.show()
