# This file contains enumerations for better auto-completion and code readability.
# Enums are not used because they are class instances and do not print actual values.

from typing import TypedDict


class Measurements(TypedDict):
    nominal: str
    ordinal: str
    interval: str
    ratio: str


measurements: Measurements = {
    'nominal': 'nominal',  # Values with no order, e.g. names
    'ordinal': 'ordinal',  # Values with order, but the distance isn't fixed, e.g. Low, High, Medium
    'interval': 'interval',  # Values with order and equal distances, but no true zero, e.g. Temperature in C or F.
    'ratio': 'ratio'  # Values with order, equal distances, and true zero, e.g. Bank balance.
}


AirQualityKeys = TypedDict('AirQualityKeys', {
    'time': str,
    'us_aqi (USAQI)': str,
    'us_aqi_pm2_5 (USAQI)': str,
    'us_aqi_pm10 (USAQI)': str,
    'us_aqi_nitrogen_dioxide (USAQI)': str,
    'us_aqi_carbon_monoxide (USAQI)': str,
    'us_aqi_ozone (USAQI)': str,
    'us_aqi_sulphur_dioxide (USAQI)': str,
    'methane (μg/m³)': str,
    'uv_index_clear_sky ()': str,
    'uv_index ()': str,
    'dust (μg/m³)': str,
    'aerosol_optical_depth ()': str,
    'ozone (μg/m³)': str,
    'sulphur_dioxide (μg/m³)': str,
    'nitrogen_dioxide (μg/m³)': str,
    'carbon_dioxide (ppm)': str,
    'pm2_5 (μg/m³)': str,
    'carbon_monoxide (μg/m³)': str,
    'pm10 (μg/m³)': str
})

aq_keys: AirQualityKeys = {
    'time': 'time',
    'us_aqi (USAQI)': 'us_aqi (USAQI)',
    'us_aqi_pm2_5 (USAQI)': 'us_aqi_pm2_5 (USAQI)',
    'us_aqi_pm10 (USAQI)': 'us_aqi_pm10 (USAQI)',
    'us_aqi_nitrogen_dioxide (USAQI)': 'us_aqi_nitrogen_dioxide (USAQI)',
    'us_aqi_carbon_monoxide (USAQI)': 'us_aqi_carbon_monoxide (USAQI)',
    'us_aqi_ozone (USAQI)': 'us_aqi_ozone (USAQI)',
    'us_aqi_sulphur_dioxide (USAQI)': 'us_aqi_sulphur_dioxide (USAQI)',
    'methane (μg/m³)': 'methane (μg/m³)',
    'uv_index_clear_sky ()': 'uv_index_clear_sky ()',
    'uv_index ()': 'uv_index ()',
    'dust (μg/m³)': 'dust (μg/m³)',
    'aerosol_optical_depth ()': 'aerosol_optical_depth ()',
    'ozone (μg/m³)': 'ozone (μg/m³)',
    'sulphur_dioxide (μg/m³)': 'sulphur_dioxide (μg/m³)',
    'nitrogen_dioxide (μg/m³)': 'nitrogen_dioxide (μg/m³)',
    'carbon_dioxide (ppm)': 'carbon_dioxide (ppm)',
    'pm2_5 (μg/m³)': 'pm2_5 (μg/m³)',
    'carbon_monoxide (μg/m³)': 'carbon_monoxide (μg/m³)',
    'pm10 (μg/m³)': 'pm10 (μg/m³)',
}

RespiratoryVirusKeys = TypedDict('RespiratoryVirusKeys', {
    'SEASON': str,
    'AGE_GRP': str,
    'RPHO_REGION': str,
    'WEEKENDING': str,
    'MMWR_WEEK': str,
    'MMWR_YEAR': str,
    'COV_POSITIVES': str,
    'COV_TOTAL_TESTS': str,
    'COV_TP': str,
    'COV_TP_LEVEL': str,
    'FLU_POSITIVES': str,
    'FLU_TOTAL_TESTS': str,
    'FLU_TP': str,
    'FLU_TP_LEVEL': str,
    'RSV_POSITIVES': str,
    'RSV_TOTAL_TESTS': str,
    'RSV_TP': str,
    'RSV_TP_LEVEL': str,
    'FLU_A_TESTS': str,
    'FLU_B_TESTS': str,
    'COV_ED_VISITS': str,
    'FLU_ED_VISITS': str,
    'RSV_ED_VISITS': str,
    'POP': str,
    'COV_ADM': str,
    'FLU_ADM': str,
    'RSV_ADM': str,
    'COV_ADM_RATE': str,
    'FLU_ADM_RATE': str,
    'RSV_ADM_RATE': str,
    'COV_ADM_LEVEL': str,
    'FLU_ADM_LEVEL': str,
    'RSV_ADM_LEVEL': str,
    'TOTAL_DEATHS': str,
    'COV_DEATHS': str,
    'FLU_DEATHS': str,
    'RSV_DEATHS': str,
    'COV_DEATHS_PER': str,
    'FLU_DEATHS_PER': str,
    'RSV_DEATHS_PER': str,
    'SEASON_COV_PED_DEATHS': str,
    'SEASON_FLU_PED_DEATHS': str,
    'SEASON_RSV_PED_DEATHS': str
})

rv_keys: RespiratoryVirusKeys = {
    'SEASON': 'SEASON',
    'AGE_GRP': 'AGE_GRP',
    'RPHO_REGION': 'RPHO_REGION',
    'WEEKENDING': 'WEEKENDING',
    'MMWR_WEEK': 'MMWR_WEEK',
    'MMWR_YEAR': 'MMWR_YEAR',
    'COV_POSITIVES': 'COV_POSITIVES',
    'COV_TOTAL_TESTS': 'COV_TOTAL_TESTS',
    'COV_TP': 'COV_TP',
    'COV_TP_LEVEL': 'COV_TP_LEVEL',
    'FLU_POSITIVES': 'FLU_POSITIVES',
    'FLU_TOTAL_TESTS': 'FLU_TOTAL_TESTS',
    'FLU_TP': 'FLU_TP',
    'FLU_TP_LEVEL': 'FLU_TP_LEVEL',
    'RSV_POSITIVES': 'RSV_POSITIVES',
    'RSV_TOTAL_TESTS': 'RSV_TOTAL_TESTS',
    'RSV_TP': 'RSV_TP',
    'RSV_TP_LEVEL': 'RSV_TP_LEVEL',
    'FLU_A_TESTS': 'FLU_A_TESTS',
    'FLU_B_TESTS': 'FLU_B_TESTS',
    'COV_ED_VISITS': 'COV_ED_VISITS',
    'FLU_ED_VISITS': 'FLU_ED_VISITS',
    'RSV_ED_VISITS': 'RSV_ED_VISITS',
    'POP': 'POP',
    'COV_ADM': 'COV_ADM',
    'FLU_ADM': 'FLU_ADM',
    'RSV_ADM': 'RSV_ADM',
    'COV_ADM_RATE': 'COV_ADM_RATE',
    'FLU_ADM_RATE': 'FLU_ADM_RATE',
    'RSV_ADM_RATE': 'RSV_ADM_RATE',
    'COV_ADM_LEVEL': 'COV_ADM_LEVEL',
    'FLU_ADM_LEVEL': 'FLU_ADM_LEVEL',
    'RSV_ADM_LEVEL': 'RSV_ADM_LEVEL',
    'TOTAL_DEATHS': 'TOTAL_DEATHS',
    'COV_DEATHS': 'COV_DEATHS',
    'FLU_DEATHS': 'FLU_DEATHS',
    'RSV_DEATHS': 'RSV_DEATHS',
    'COV_DEATHS_PER': 'COV_DEATHS_PER',
    'FLU_DEATHS_PER': 'FLU_DEATHS_PER',
    'RSV_DEATHS_PER': 'RSV_DEATHS_PER',
    'SEASON_COV_PED_DEATHS': 'SEASON_COV_PED_DEATHS',
    'SEASON_FLU_PED_DEATHS': 'SEASON_FLU_PED_DEATHS',
    'SEASON_RSV_PED_DEATHS': 'SEASON_RSV_PED_DEATHS',
}
