from extractors.lib import GameData, MissionData, getStatAsInt, Hero


def startMission(request, temp, gameData: GameData):
    print(request)
    if 'userId' not in temp:
        temp['userId'] = 1

    missionId = getStatAsInt(request['args'], 'id', 1)
    heroesIds = request['args']['heroes']

    response = {}

    response['userId'] = temp['userId']
    response['typeId'] = 1
    response['attackers'] = {}
    for heroId in heroesIds:
        response['attackers'][heroId] = getTestHero(gameData, heroId)

    mission = gameData.missions[missionId]
    response['defenders'] = getWavesForMission(mission)
    response['effects'] = []

    response['reward'] = {'experience': 13, 'heroXp': {'3': 4}, 'gear': {'3': 1}, 'gold': 523}  # TODO
    response['seed'] = 301709962
    response['startTime'] = 1745606343
    response['type'] = 'mission'
    return response


def getWavesForMission(mission: MissionData):
    enemies = []
    index = 1
    for wave in mission.waves:
        waveEnemies = {}
        for enemy in wave.enemies:
            waveEnemies[index] = enemy.getBattleData()
            index += 1
        enemies.append(waveEnemies)
    return enemies


def getTestHero(data: GameData, id: int, lvl: int = 1, stars: int = 1, color: int = 1) -> Hero:
    heroData = data.heroes[id]
    hero = Hero(heroData)
    hero.applyStarsAndLevel(stars, lvl)
    hero.applyColor(color)
    # hero.applyGear([True, True, True])
    battleData = hero.getBattleData()

    battleData["skills"] = {"432": 1}
    battleData["power"] = 241
    battleData["runes"] = [0, 0, 0, 0, 0]
    battleData["skins"] = {"3": 1}
    battleData["currentSkin"] = 3
    battleData["titanGiftLevel"] = 0
    battleData["titanCoinsSpent"] = None
    battleData["artifacts"] = [
        {"level": 1, "star": 0},
        {"level": 1, "star": 0},
        {"level": 1, "star": 0}
        ]
    battleData["perks"] = [6, 1]
    battleData["ascensions"] = None
    battleData['physicalAttack'] = hero.physicalAttack
    battleData['armor'] = hero.armor
    battleData['magicPower'] = hero.magicPower
    battleData['magicResist'] = hero.magicResist
    battleData['skin'] = 0
    battleData['favorPetId'] = 0
    battleData['favorPower'] = 0
    return battleData


def endMission(request, temp, gameData):
    print(request)
    reward = {}
    reward['experience'] = 13
    reward['heroXp'] = {'3': 4}
    reward['gear'] = {'3': 1}
    reward['gold'] = 523
    response = {}
    response['reward'] = reward
    return response


def raidMission(request, temp, gameData):
    print(request)
    # missionId = getStatAsInt(request['args'], 'id', 1)
    attempts = getStatAsInt(request['args'], 'times', 1)
    reward = {}
    reward['experience'] = 13 * attempts
    reward['gear'] = {'37': 666 * attempts}
    reward['gold'] = 523 * attempts
    response = {}
    response['reward'] = reward
    return response
