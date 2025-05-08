from extractors.lib import GameData


def adventuresPassed(request, temp, gameData: GameData):
    return {"101": 1, "1": 12, "2": 1, "3": 5}


def adventuresActive(request, temp, gameData: GameData):
    return {"hasActive": False, "lastChatTime": None, "hasRewards": False}


def adventuresFind(request, temp, gameData: GameData):
    return {"lobbies": [], "users": []}


def adventuresSolo(request, temp, gameData: GameData):
    return {
            "hasActive": False,
            "adventureId": None,
            "endTime": None,
            "turns": None,
            "hasRewards": None
        }
