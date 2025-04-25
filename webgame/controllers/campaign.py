

def startMission(request, temp):
    print(request)
    print(temp)
    if 'userId' not in temp:
        temp['userId'] = 1

    missionId = request['args']['id']
    heroesIds = request['args']['heroes']

    response = {}

    response['userId'] = temp['userId']
    response['typeId'] = 1
    response['attackers'] = {7: getTestHero(3)}  # TODO
    response['defenders'] = getWavesForMission(missionId)
    response['effects'] = []

    response['reward'] = {'experience': 13, 'heroXp': {'7': 4}, 'gear': {'3': 1}, 'gold': 523}  # TODO
    response['seed'] = 301709962
    response['startTime'] = 1745606343
    response['type'] = 'mission'
    return response


def getWavesForMission(missionId):
    return [
            {1: getBaseEnemy(1000)},
            {2: getBaseEnemy(1000)},
            {3: getBaseEnemy(1000)}
        ]


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
    hero = {}
    hero['id'] = id
    hero['xp'] = 233
    hero['level'] = 5
    hero['color'] = 2
    hero['slots'] = []
    hero['skills'] = {"421": 3, "422": 3}
    hero['power'] = 535
    hero['star'] = 1
    hero['runes'] = [0, 0, 0, 0, 0]
    hero['skins'] = []
    hero['currentSkin'] = 0
    hero['titanGiftLevel'] = 0
    hero['titanCoinsSpent'] = None
    hero['artifacts'] = [
                {"level": 1, "star": 0},
                {"level": 1, "star": 0},
                {"level": 1, "star": 0}
                ]
    hero['scale'] = 1
    hero['petId'] = 0
    hero['type'] = 'hero'
    hero['perks'] = [9, 5, 1, 14]
    hero['ascensions'] = []
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
