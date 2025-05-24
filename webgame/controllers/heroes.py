from extractors.lib import GameData, Hero, getStatAsInt
from typing import Optional
from repo.userdata import GameRepository


def getHeroById(id: int, data: GameData):
    heroData = data.heroes[id]
    hero = Hero(heroData)
    hero.applyStarsAndLevel(3, 68)
    hero.applyColor(9)
    return hero.getProfileData()


def getUserHeroes(request, repo: GameRepository, gameData: GameData):
    result = {}
    userHeroes = repo.getHeroesByUserId(1)
    for hero in userHeroes:
        result[str(hero.data.id)] = hero.getProfileData()
    return result


def upgradeSkill(request, repo: GameRepository, gameData: GameData):
    heroId = getStatAsInt(request['args'], 'heroId')
    skillNum = getStatAsInt(request['args'], 'skill') - 1
    hero: Optional[Hero] = None
    heroes = repo.getHeroesByUserId(1)
    for h in heroes:
        if h.data.id == heroId:
            hero = h
            break
    if not hero:
        return None
    hero.skills[skillNum] += 1
    return None


def evolveHero(request, repo: GameRepository, gameData: GameData):
    heroId = getStatAsInt(request['args'], 'heroId')
    # TODO: errors, verify and deduct gold

    userHeroes = repo.getHeroesByUserId(1)
    for hero in userHeroes:
        if hero.data.id == heroId:
            hero.revertStarsAndLevel(hero.stars, hero.level)
            hero.stars += 1
            hero.applyStarsAndLevel(hero.stars, hero.level)
    return []


def addExpToHero(request, repo: GameRepository, gameData: GameData):
    heroId = getStatAsInt(request['args'], 'heroId')
    # consumableId = getStatAsInt(request['args'], 'libId')
    consumableAmount = getStatAsInt(request['args'], 'amount')
    exp = 1500 * consumableAmount
    userHeroes = repo.getHeroesByUserId(1)
    for hero in userHeroes:
        if hero.data.id == heroId:
            hero.addExperience(exp, gameData.levelToExp)
    return []


def getHeroRatings(request, repo: GameRepository, gameData: GameData):
    response = {}
    response['userRating'] = []
    response['rating'] = {}
    for i in range(1, 67):
        response['rating'][str(i)] = 4.00
    return response
