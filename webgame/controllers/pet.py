from extractors.lib import GameData


def getPets(request, temp, gameData: GameData):
    return []


def getPetPotions(request, temp, gameData: GameData):
    return 0


def getPetChest(request, temp, gameData: GameData):
    return {
            "starmoneySpent": 0,
            "dailyPetId": "6006"
        }
