import time
from datetime import datetime
from controllers.items import addMultToInventory


def getTime(request, temp, gameData):
    return int(time.time())


claimed = False
claimedDays = 20
heroOfMonth = 3


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
            "heroId": heroOfMonth
        }


dailyRewards = {
        20: {
            'fragmentHero': {str(heroOfMonth): 8},
            }
        }


def farmDaily(request, temp, gameData):
    print(request)
    vip = request['args']['vip'] == 1

    rewards = dailyRewards[claimedDays]
    if vip:
        print("TODO: double rewards for vip accounts")

    addMultToInventory(temp, rewards)
    return rewards
