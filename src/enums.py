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


class AirQualityKeys(TypedDict):
    time: str
    us_aqi: str
    us_aqi_pm2_5: str
    us_aqi_pm10: str
    us_aqi_nitrogen_dioxide: str
    us_aqi_carbon_monoxide: str
    us_aqi_ozone: str
    us_aqi_sulphur_dioxide: str
    methane: str
    uv_index_clear_sky: str
    uv_index: str
    dust: str
    aerosol_optical_depth: str
    ozone: str
    sulphur_dioxide: str
    nitrogen_dioxide: str
    carbon_dioxide: str
    pm2_5: str
    carbon_monoxide: str
    pm10: str


air_quality_keys: AirQualityKeys = {
    'time': 'time',
    'us_aqi': 'us_aqi (USAQI)',
    'us_aqi_pm2_5': 'us_aqi_pm2_5 (USAQI)',
    'us_aqi_pm10': 'us_aqi_pm10 (USAQI)',
    'us_aqi_nitrogen_dioxide': 'us_aqi_nitrogen_dioxide (USAQI)',
    'us_aqi_carbon_monoxide': 'us_aqi_carbon_monoxide (USAQI)',
    'us_aqi_ozone': 'us_aqi_ozone (USAQI)',
    'us_aqi_sulphur_dioxide': 'us_aqi_sulphur_dioxide (USAQI)',
    'methane': 'methane (μg/m³)',
    'uv_index_clear_sky': 'uv_index_clear_sky ()',
    'uv_index': 'uv_index ()',
    'dust': 'dust (μg/m³)',
    'aerosol_optical_depth': 'aerosol_optical_depth',
    'ozone': 'ozone (μg/m³)',
    'sulphur_dioxide': 'sulphur_dioxide (μg/m³)',
    'nitrogen_dioxide': 'nitrogen_dioxide (μg/m³)',
    'carbon_dioxide': 'carbon_dioxide (ppm)',
    'pm2_5': 'pm2_5 (μg/m³)',
    'carbon_monoxide': 'carbon_monoxide (μg/m³)',
    'pm10': 'pm10 (μg/m³)',
}


class RespiratoryVirusKeys(TypedDict):
    season: str
    age_group: str
    rpho_region: str
    weekending: str
    mmwr_week: str
    mmwr_year: str
    cov_positives: str
    cov_total_tests: str
    cov_tp: str
    cov_tp_level: str
    flu_positives: str
    flu_total_tests: str
    flu_tp: str
    flu_tp_level: str
    rsv_positives: str
    rsv_total_tests: str
    rsv_tp: str
    rsv_tp_level: str
    flu_a_tests: str
    flu_b_tests: str
    cov_ed_visits: str
    flu_ed_visits: str
    rsv_ed_visits: str
    pop: str
    cov_adm: str
    flu_adm: str
    rsv_adm: str
    cov_adm_rate: str
    flu_adm_rate: str
    rsv_adm_rate: str
    cov_adm_level: str
    flu_adm_level: str
    rsv_adm_level: str
    total_deaths: str
    cov_deaths: str
    flu_deaths: str
    rsv_deaths: str
    cov_deaths_per: str
    flu_deaths_per: str
    rsv_deaths_per: str
    season_cov_ped_deaths: str
    season_flu_ped_deaths: str
    season_rsv_ped_deaths: str


respiratory_virus_keys: RespiratoryVirusKeys = {
    'season': 'SEASON',
    'age_group': 'AGE_GRP',
    'rpho_region': 'RPHO_REGION',
    'weekending': 'WEEKENDING',
    'mmwr_week': 'MMWR_WEEK',
    'mmwr_year': 'MMWR_YEAR',
    'cov_positives': 'COV_POSITIVES',
    'cov_total_tests': 'COV_TOTAL_TESTS',
    'cov_tp': 'COV_TP',
    'cov_tp_level': 'COV_TP_LEVEL',
    'flu_positives': 'FLU_POSITIVES',
    'flu_total_tests': 'FLU_TOTAL_TESTS',
    'flu_tp': 'FLU_TP',
    'flu_tp_level': 'FLU_TP_LEVEL',
    'rsv_positives': 'RSV_POSITIVES',
    'rsv_total_tests': 'RSV_TOTAL_TESTS',
    'rsv_tp': 'RSV_TP',
    'rsv_tp_level': 'RSV_TP_LEVEL',
    'flu_a_tests': 'FLU_A_TESTS',
    'flu_b_tests': 'FLU_B_TESTS',
    'cov_ed_visits': 'COV_ED_VISITS',
    'flu_ed_visits': 'FLU_ED_VISITS',
    'rsv_ed_visits': 'RSV_ED_VISITS',
    'pop': 'POP',
    'cov_adm': 'COV_ADM',
    'flu_adm': 'FLU_ADM',
    'rsv_adm': 'RSV_ADM',
    'cov_adm_rate': 'COV_ADM_RATE',
    'flu_adm_rate': 'FLU_ADM_RATE',
    'rsv_adm_rate': 'RSV_ADM_RATE',
    'cov_adm_level': 'COV_ADM_LEVEL',
    'flu_adm_level': 'FLU_ADM_LEVEL',
    'rsv_adm_level': 'RSV_ADM_LEVEL',
    'total_deaths': 'TOTAL_DEATHS',
    'cov_deaths': 'COV_DEATHS',
    'flu_deaths': 'FLU_DEATHS',
    'rsv_deaths': 'RSV_DEATHS',
    'cov_deaths_per': 'COV_DEATHS_PER',
    'flu_deaths_per': 'FLU_DEATHS_PER',
    'rsv_deaths_per': 'RSV_DEATHS_PER',
    'season_cov_ped_deaths': 'SEASON_COV_PED_DEATHS',
    'season_flu_ped_deaths': 'SEASON_FLU_PED_DEATHS',
    'season_rsv_ped_deaths': 'SEASON_RSV_PED_DEATHS',
}
