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
