from controllers.heroes import getHeroById
from extractors.lib import GameData, MissionData, getStatAsInt


def startMission(request, temp, gameData: GameData):
    print(request)
    print(temp)
    if 'userId' not in temp:
        temp['userId'] = 1

    missionId = getStatAsInt(request['args'], 'id', 1)
    heroesIds = request['args']['heroes']

    response = {}

    response['userId'] = temp['userId']
    response['typeId'] = 1
    response['attackers'] = {}
    for heroId in heroesIds:
        response['attackers'][heroId] = getTestHero(heroId)

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


def getBaseEnemy(id):
    enemy = {}
    enemy['id'] = id
    enemy['xp'] = 0
    enemy['level'] = '1'
    enemy['color'] = 1
    enemy['slots'] = []
    enemy['skills'] = []
    enemy['power'] = 33
    enemy['star'] = '1'
    enemy['runes'] = [0, 0, 0, 0, 0]
    enemy['skins'] = []
    enemy['currentSkin'] = 0
    enemy['titanGiftLevel'] = 0
    enemy['titanCoinsSpent'] = None
    enemy['artifacts'] = None
    enemy['scale'] = 1
    enemy['petId'] = 0
    enemy['type'] = 'hero'
    enemy['perks'] = None
    enemy['ascensions'] = []
    enemy['agility'] = 2
    enemy['intelligence'] = 2
    enemy['hp'] = 50
    enemy['physicalAttack'] = 15
    enemy['strength'] = 2
    enemy['skin'] = 0
    enemy['favorPetId'] = 0
    enemy['favorPower'] = 0
    return enemy


def getTestHero(id):
    hero = getHeroById(id)
    hero['agility'] = 27
    hero['intelligence'] = 52
    hero['hp'] = 700
    hero['physicalAttack'] = 50
    hero['strength'] = 32
    hero['armor'] = 25
    hero['magicPower'] = 25
    hero['magicResist'] = 25
    hero['skin'] = 0
    hero['favorPetId'] = 0
    hero['favorPower'] = 0
    return hero


def endMission(request, temp):
    reward = {}
    reward['experience'] = 13
    reward['heroXp'] = {'3': 4}
    reward['gear'] = {'3': 1}
    reward['gold'] = 523
    response = {}
    response['reward'] = reward
    return response


def raidMission(request, temp):
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
