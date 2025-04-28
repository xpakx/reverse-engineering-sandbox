from controllers.items import addMultToInventory
from extractors.lib import getStatAsInt, GameData
from datetime import datetime


rewards = {
        23151: {
            'fragmentHero': {'60': 3},
            'gold': 30000
            }
        }


def farmQuest(request, temp, gameData):
    print(request)
    questId = getStatAsInt(request['args'], 'questId')
    if questId not in rewards:
        return []
    print(rewards[questId])
    addMultToInventory(temp, rewards[questId])
    return rewards[questId]


def getQuest(id):
    return {
        "id": id,
        "state": 2,
        "progress": 3,
        "reward": {
            "gold": 30000,
            "fragmentHero": {
                "60": 3
                }
            },
        "createTime": 1745104656
        }


def getQuests(request, temp, gameData):
    response = []
    for i in range(23149, 23155):
        response.append(getQuest(i))
    return response


def getQuestEvents(request, temp, gameData: GameData):
    response = []
    event = gameData.questEvents[68]
    response.append(event.getForDate(datetime(2025, 4, 1), datetime(2025, 4, 30)))
    print(response)
    return response
