from enum import Enum

import numpy as np
import pandas
from sklearn.preprocessing import PowerTransformer

from src.serialize import dump_to_file

class Transformation(Enum):
    SQRT = 'sqrt'
    LOG1P = 'log1p'
    YEO_JOHNSON = 'yeo-johnson'

def transform(df: pandas.DataFrame, transformations: dict, dump_prefix: str = '') -> pandas.DataFrame:
    transformed = df.copy()

    for feature, transformation in transformations.items():
        if transformation == Transformation.SQRT:
            transformed[feature] = np.sqrt(df[feature])
        elif transformation == Transformation.LOG1P:
            transformed[feature] = np.log1p(df[feature])
        elif transformation == Transformation.YEO_JOHNSON:
            power_transformer = PowerTransformer(method='yeo-johnson')
            transformed[feature] = power_transformer.fit_transform(df[[feature]]).ravel()
            dump_to_file(power_transformer, dump_prefix + feature)

    return transformed