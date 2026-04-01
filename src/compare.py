import numpy as np
import pandas as pd
from pandas.core.dtypes.common import is_numeric_dtype
from sklearn.preprocessing import PowerTransformer

def compare_transformations(df: pd.DataFrame):
    df_sqrt = df.copy()
    df_log1p = df.copy()
    df_cbrt = df.copy()
    df_yeo_johnson = df.copy()
    df_yeo_johnson_inverse = df.copy()

    skew = {}
    skew_sqrt = {}
    skew_log1p = {}
    skew_cbrt = {}
    skew_yeo_johnson = {}
    skew_yeo_johnson_inverse = {}

    for feature in df.columns:
        if not is_numeric_dtype(df[feature]):
            skew[feature] = 'N/A'
            skew_sqrt[feature] = 'N/A'
            skew_log1p[feature] = 'N/A'
            skew_cbrt[feature] = 'N/A'
            skew_yeo_johnson[feature] = 'N/A'
            skew_yeo_johnson_inverse[feature] = 'N/A'
            continue

        df_sqrt[feature] = np.sqrt(df[feature])
        df_log1p[feature] = np.log1p(df[feature])
        df_cbrt[feature] = np.cbrt(df[feature])
        power_transformer = PowerTransformer(method='yeo-johnson')
        df_yeo_johnson[feature] = power_transformer.fit_transform(df[[feature]])
        df_yeo_johnson_inverse[feature] = power_transformer.inverse_transform(df_yeo_johnson[[feature]])

        skew[feature] = round(df[feature].skew(), 2)
        skew_sqrt[feature] = round(df_sqrt[feature].skew(), 2)
        skew_log1p[feature] = round(df_log1p[feature].skew(), 2)
        skew_cbrt[feature] = round(df_cbrt[feature].skew(), 2)
        skew_yeo_johnson[feature] = round(df_yeo_johnson[feature].skew(), 2)
        skew_yeo_johnson_inverse[feature] = round(df_yeo_johnson_inverse[feature].skew(), 2)

    return pd.DataFrame({
        'Original': skew,
        'Square root': skew_sqrt,
        'Log transformation': skew_log1p,
        'Cube root': skew_cbrt,
        'Yeo-Johnson Transform': skew_yeo_johnson,
        'Yeo-Johnson Inverse Transform': skew_yeo_johnson_inverse
    })
