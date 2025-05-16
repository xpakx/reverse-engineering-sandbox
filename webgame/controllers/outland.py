from extractors.lib import GameData


def getBosses(request, temp, gameData: GameData):
    response = {}
    for i in range(10, 13):
        response.append({
            "id": i,
            "bossLevel": 1,
            "chestNum": 1,
            "chestId": 0,
            "lastChestReward": [],
            "chests": [],
            "cost": [],
            "mayRaid": True
            })
    return response
