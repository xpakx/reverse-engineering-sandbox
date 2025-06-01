from extractors.lib import GameData, Hero, getStatAsInt
from typing import Optional
from repo.userdata import GameRepository
from repo.item import ItemDef


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


def craftHero(request, repo: GameRepository, gameData: GameData):
    heroId = getStatAsInt(request['args'], 'heroId')
    inventory = repo.getInventoryByUserId(1)

    heroData = gameData.heroes[heroId]
    soulStones = starsToCost(heroData.minStar)

    cost = ItemDef(
            itemType='fragmentHero',
            itemId=heroId,
            itemCount=soulStones)
    hasFragments = inventory.removeItem(cost)
    if not hasFragments:
        print("Not enough soul stones")
        return []
    userHeroes = repo.getHeroesByUserId(1)

    hero = Hero(heroData)
    hero.applyStarsAndLevel(heroData.minStar, 1)
    hero.applyColor(1)
    hero.skills[0] = 1
    userHeroes.append(hero)
    return []


def starsToCost(minStar: int) -> int:
    if minStar == 1:
        return 10
    if minStar == 2:
        return 30
    if minStar == 3:
        return 80
    if minStar == 4:
        return 180
    if minStar == 5:
        return 330
    return 630
