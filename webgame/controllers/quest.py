from controllers.items import addMultToInventory
from extractors.lib import getStatAsInt


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


def getQuestEvents(request, temp, gameData):
    response = []
    response.append({
        "id": 68,
        "sortOrder": 1,
        "eventReward": None,
        "eventLoopData": None,
        "clientData": None,
        "icon": "event_icon_001",
        "hideCompleted": None,
        "questChains": None,
        "background": "event_background_001.jpg",
        "localeKey": "LIB_SPECIAL_QUEST_EVENT_NAME_3",
        "desc_localeKey": "LIB_SPECIAL_QUEST_EVENT_DESC_3",
        "name_localeKey": "LIB_SPECIAL_QUEST_EVENT_NAME_3",
        "notification_localeKey": "",
        "startTime": 1745104656,
        "endTime": 1745709456
        })
    return response
