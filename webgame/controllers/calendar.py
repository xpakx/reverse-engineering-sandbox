import time
from datetime import datetime
from repo.userdata import GameRepository
from repo.item import ItemDef


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
        20: ItemDef(itemType='fragmentHero', itemId=heroOfMonth, itemCount=8)
        }


def farmDaily(request, repo: GameRepository, gameData):
    print(request)
    vip = request['args']['vip'] == 1

    reward = dailyRewards[claimedDays]
    if vip:
        print("TODO: double rewards for vip accounts")
    inventory = repo.getInventoryByUserId(1)
    inventory.addItem(reward)
    return reward.toResponse()
