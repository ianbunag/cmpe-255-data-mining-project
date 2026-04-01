import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype
from sklearn.preprocessing import PowerTransformer

PREFIX_SQRT = 'sqrt_'
PREFIX_LOG1P = 'log1p_'
PREFIX_CBRT = 'cbrt_'
PREFIX_YEO_JOHNSON = 'yeo_johnson_'

def compare_transformations(df: pd.DataFrame):
    df_transforms = df.copy()

    skew = {}
    skew_sqrt = {}
    skew_log1p = {}
    skew_cbrt = {}
    skew_yeo_johnson = {}

    for feature in df_transforms.columns:
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
