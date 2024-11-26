#!python3
# https://dragonlancenexus.com/moon-tracking-chart/

"""
Created for DragonLance 5e

If you are playing a wizard, the phases of the three moons has impact 
on a spell casting bonus.
"""

DAYS_PER_MONTH = 28

CYCLES = {
    "Solinari": 36,
    "Lunitari": 28,
    "Nuitari": 8,
}

MONTHS = [
    "Winter Night",  # Jan
    "Winter Deep",  # Feb
    "Spring Dawning",  # Mar
    "Spring Rain",  # Apr
    "Spring Blossom",  # May
    "Summer Home",  # Jun
    "Summer Run",  # Jul
    "Summer End",  # Aug
    "Autumn Harvest",  # Sep
    "Autumn Twilight",  # Oct
    "Autumn Dark",  # Nov
    "Winter Come",  # Dec
]

# Campaign start date and months
# in index format.  0 -> Winter Night, 0 -> 1st of the month
START_MONTH = 8
START_DAY = 0

# What are the initial indexes for the moons
# Start in the 'New Moon' quadrant.
# This corresponds to 1 for Nuitari, 4 for Lunitari and 2 slots left of 1 for Solinari
START_CYCLE = {
    "Solinari": 0,
    "Lunitari": 0,
    "Nuitari": 0,
}


def cal_date(offset: int) -> str:
    total_num = START_MONTH * DAYS_PER_MONTH + START_DAY + offset
    month = (total_num // DAYS_PER_MONTH) % len(MONTHS)
    day = total_num % DAYS_PER_MONTH
    return MONTHS[month] + " " + str(day + 1)


def nuitari_phase(n: int) -> str:
    n = n % CYCLES["Nuitari"]
    if n == 0 or n == 1:
        return "New Moon"
    if n == 2 or n == 3:
        return "First Quarter"
    if n == 4 or n == 5:
        return "Full Moon"
    if n == 6 or n == 7:
        return "Last Quarter"
    return "ERROR"


def lunitari_phase(n: int) -> str:
    n = n % CYCLES["Lunitari"]
    if n >= 0 and n < 7:
        return "New Moon"
    if n > 6 and n < 14:
        return "First Quarter"
    if n > 13 and n < 21:
        return "Full Moon"
    if n > 20 and n < 28:
        return "Last Quarter"
    return "ERROR"


def solinari_phase(n: int) -> str:
    n = n % CYCLES["Solinari"]
    if n >= 0 and n < 9:
        return "New Moon"
    if n > 8 and n < 18:
        return "First Quarter"
    if n > 17 and n < 27:
        return "Full Moon"
    if n > 26 and n < 36:
        return "Last Quarter"
    return "ERROR"


def mod_calc(sol: str, lun: str, nui: str) -> int:
    return 0


def main():
    for i in range(DAYS_PER_MONTH * len(MONTHS)):
        date_str = cal_date(i)
        sol_phase = solinari_phase(i + START_CYCLE["Solinari"])
        lun_phase = lunitari_phase(i + START_CYCLE["Lunitari"])
        nui_phase = nuitari_phase(i + START_CYCLE["Nuitari"])
        modifier = mod_calc(sol_phase, lun_phase, nui_phase)
        print(
            "{},{},{},{},{}".format(date_str, sol_phase, lun_phase, nui_phase, modifier)
        )


if __name__ == "__main__":
    main()
