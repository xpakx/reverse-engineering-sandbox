from extractors.lib import GameData


def getTitanArena(request, temp, gameData: GameData):
    return False


def getTitanArenaChest(request, temp, gameData: GameData):
    return []


def getTitans(request, temp, gameData: GameData):
    return {}


def getTitanSpirits(request, temp, gameData: GameData):
    return {
            "water": {"id": 4001, "level": 1, "star": 0},
            "fire": {"id": 4002, "level": 18, "star": 1},
            "earth": {"id": 4003, "level": 1, "star": 0},
            "dark": {"id": 4004, "level": 1, "star": 0},
            "light": {"id": 4005, "level": 1, "star": 0}
        }
