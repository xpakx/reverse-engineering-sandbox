userHeroes = [3]


def getHeroById(id):
    return {
            "id": id,
            "xp": 300105,
            "level": 68,
            "color": 9,
            "slots": [0, 0, 0],
            "skills": {
                "432": 67,
                "433": 67,
                "434": 67,
                "435": 67
                },
            "power": 19156,
            "star": 3,
            "runes": [3230, 0, 100, 2790, 0],
            "skins": {"3": 48},
            "currentSkin": 3,
            "titanGiftLevel": 14,
            "titanCoinsSpent": {
                "consumable": {"24": 12110}
                },
            "artifacts": [
                {"level": 6, "star": 2},
                {"level": 23, "star": 4},
                {"level": 19, "star": 1}
                ],
            "scale": 1,
            "petId": 0,
            "type": "hero",
            "perks": [6, 1],
            "ascensions": {"1": [0, 1, 2, 3]}
        }


def getUserHeroes(request, temp):
    result = {}
    for id in userHeroes:
        result[str(id)] = getHeroById(id)
    return result
