from extractors.lib import GameData, Hero, getStatAsInt
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
    hero = repo.getHeroByUserIdAndId(1, heroId)
    if not hero:
        return None
    hero.skills[skillNum] += 1
    return None


def evolveHero(request, repo: GameRepository, gameData: GameData):
    heroId = getStatAsInt(request['args'], 'heroId')
    # TODO: errors, verify and deduct gold

    hero = repo.getHeroByUserIdAndId(1, heroId)
    if not hero:
        # TODO: error
        return None

    hero.revertStarsAndLevel(hero.stars, hero.level)
    hero.stars += 1
    hero.applyStarsAndLevel(hero.stars, hero.level)
    return []


def addExpToHero(request, repo: GameRepository, gameData: GameData):
    heroId = getStatAsInt(request['args'], 'heroId')
    # consumableId = getStatAsInt(request['args'], 'libId')
    consumableAmount = getStatAsInt(request['args'], 'amount')
    exp = 1500 * consumableAmount
    hero = repo.getHeroByUserIdAndId(1, heroId)
    if not hero:
        return None
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


def heroEquip(request, repo: GameRepository, gameData: GameData):
    heroId = getStatAsInt(request['args'], 'heroId')
    slot = getStatAsInt(request['args'], 'slot')

    hero = repo.getHeroByUserIdAndId(1, heroId)
    if not hero:
        return None

    item = hero.data.color[hero.color][1][slot].id
    cost = ItemDef(
            itemType='gear',
            itemId=item,
            itemCount=1)
    inventory = repo.getInventoryByUserId(1)
    hasGear = inventory.removeItem(cost)
    if not hasGear:
        print("No gear in inventory")
        return []

    gearCount = len(hero.gear)
    if slot >= gearCount:
        gearCount = slot + 1
    newGear = []
    for i in range(gearCount):
        if i < len(hero.gear) and hero.gear[i]:
            newGear.append(True)
            continue
        if i == slot:
            newGear.append(True)
            continue
        newGear.append(False)
    hero.removeGear()
    hero.applyGear(newGear)
    return []


def heroPromote(request, repo: GameRepository, gameData: GameData):
    heroId = getStatAsInt(request['args'], 'heroId')
    hero = repo.getHeroByUserIdAndId(1, heroId)
    if not hero:
        return None
    if len(hero.gear) < 6:
        return None
    if not all(hero.gear):
        return None
    color = hero.color
    hero.removeGear()
    hero.gear = []
    hero.revertColor()
    hero.applyColor(color + 1)
    return []


def heroSkinUpgrade(request, repo: GameRepository, gameData: GameData):
    heroId = getStatAsInt(request['args'], 'heroId')
    skinId = getStatAsInt(request['args'], 'skinId')
    hero = repo.getHeroByUserIdAndId(1, heroId)
    inventory = repo.getInventoryByUserId(1)
    if not hero:
        return None
    if skinId not in hero.data.skins:
        return None
    skin = hero.data.skins[skinId]
    level = hero.skinLevels[skinId] if skinId in hero.skinLevels else 0
    newLevel = level + 1
    cost = skin.costs[newLevel]
    hasSkinStones = inventory.removeItem(cost)
    if not hasSkinStones:
        print("Not enough skin stones")
        return None
    if level > 0:
        hero.revert(skin.stats[level])
    hero.skinLevels[skinId] = newLevel
    hero.update(skin.stats[newLevel])
    return None
