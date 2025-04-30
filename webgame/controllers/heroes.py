from extractors.lib import GameData, Hero

userHeroes = [3]


def getHeroById(id: int, data: GameData):
    heroData = data.heroes[id]
    hero = Hero(heroData)
    hero.applyStarsAndLevel(3, 68)
    hero.applyColor(9)
    return hero.getProfileData()


def getUserHeroes(request, temp, gameData: GameData):
    result = {}
    for id in userHeroes:
        result[str(id)] = getHeroById(id, gameData)
    return result
