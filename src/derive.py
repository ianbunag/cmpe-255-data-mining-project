from datetime import datetime

from epiweeks import Week

def derive_epi(time: str):
    epi = get_epi(time)

    return epi['SEASON'], epi['WEEKENDING'], epi['MMWR_WEEK'], epi['MMWR_YEAR']

def get_epi(time: str):
    week = Week.fromdate(datetime.strptime(time, '%Y-%m-%d %H:%M'))

    return {
        'SEASON': get_epi_season(week.week, week.year),
        'WEEKENDING': week.enddate().strftime('%m/%d/%Y'),
        'MMWR_WEEK': week.week,
        'MMWR_YEAR': week.year,
    }

def get_epi_season(week: int, year: int):
    if week >= 27:
        return f"{year}/{year + 1}"
    else:
        return f"{year - 1}/{year}"
