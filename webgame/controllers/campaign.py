from extractors.lib import GameData, MissionData, getStatAsInt, Hero
from typing import List
import random
from repo.userdata import GameRepository


def startMission(request, repo: GameRepository, gameData: GameData):
    print(request)
    if not repo.tempUser:
        repo.tempUser = 1

    missionId = getStatAsInt(request['args'], 'id', 1)
    heroesIds = request['args']['heroes']

    response = {}

    response['userId'] = repo.tempUser
    response['typeId'] = 1
    response['attackers'] = {}

    for heroId in heroesIds:
        response['attackers'][heroId] = getTestHero(gameData, repo, heroId)

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


def getTestHero(data: GameData, repo: GameRepository, heroId: int) -> Hero:
    heroes: List[Hero] = repo.getHeroesByUserId(1)

    hero = None
    for h in heroes:
        if h.data.id == heroId:
            hero = h
            break
    if not hero:
        return

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


def endMission(request, repo: GameRepository, gameData):
    print(request)
    missionId = getStatAsInt(request['args'], 'id', 1)
    mission = gameData.missions[missionId]
    reward = getRewardsForMission(gameData, missionId)
    reward['heroXp'] = {'3': mission.heroExp}
    response = {}
    response['reward'] = reward
    return response


def getRewardsForMission(gameData: GameData, missionId: int):
    mission = gameData.missions[missionId]
    reward = {}
    for dropData in mission.drops:
        if dropData.chance == 0:
            continue
        if dropData.chance != 100:
            roll = random.random()*100
            if roll > dropData.chance:
                continue

        for drop in dropData.rewardNew:
            if drop.itemType == 'gold':
                reward['gold'] = dropData.reward['gold']
            if drop.itemType in ['gear', 'fragmentHero', 'consumable']:
                if drop.itemType not in reward:
                    reward[drop.itemType] = {}
                key = str(drop.itemId)
                value = drop.itemCount
                if key not in reward[drop.itemType]:
                    reward[drop.itemType][key] = 0
                reward[drop.itemType][key] = reward[drop.itemType][key] + value
    reward['experience'] = mission.teamExp
    return reward


def raidMission(request, repo: GameRepository, gameData):
    print(request)
    missionId = getStatAsInt(request['args'], 'id', 1)
    attempts = getStatAsInt(request['args'], 'times', 1)
    response = {}
    for i in range(attempts):
        reward = getRewardsForMission(gameData, missionId)
        id = str(i)
        response[id] = reward

    raidReward = {}
    raidReward['consumable'] = {'9': 2*attempts}
    response['raid'] = raidReward
    return response


def getMissions(request, temp, gameData):
    response = []
    for i in range(1, 2):
        response.append(
                {
                    "id": i,
                    "stars": 3,
                    "triesSpent": 0,
                    "resetToday": 0,
                    "attempts": 22,
                    "wins": 22
                }
            )
    return response


def getMissionReplace(request, temp, gameData):
    return None
