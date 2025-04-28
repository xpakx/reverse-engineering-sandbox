import time
from datetime import datetime


def getTime(request, temp, gameData):
    return int(time.time())


claimed = False
claimedDays = 20


def getDailyBonus(request, temp, gameData):
    now = datetime.now()
    year = str(now.year)
    month = now.month
    day = str(claimedDays)
    return {
            "year": year,
            "month": month,
            "currentDay": day,
            "availableToday": not claimed,
            "availableVip": True,
            "daysInMonth": 30,
            "heroId": 3
        }
