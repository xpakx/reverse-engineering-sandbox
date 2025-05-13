from controllers.items import addMultToInventory
from extractors.lib import getStatAsInt, GameData
from datetime import datetime


rewards = {
        23151: {
            'fragmentHero': {'60': 3},
            'gold': 30000
            }
        }

currentEvents = [68, 581, 580]


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


def getQuests(request, temp, gameData: GameData):
    response = []
    for eventId in currentEvents:
        event = gameData.questEvents[eventId]
        for chain in event.chains:
            for quest in chain.quests:
                response.append(getQuest(quest.id))
    return response


def getQuestEvents(request, temp, gameData: GameData):
    response = []
    for id in currentEvents:
        event = gameData.questEvents[id]
        response.append(event.getForDate(datetime(2025, 4, 1), datetime(2025, 4, 30)))
    print(response)
    return response
