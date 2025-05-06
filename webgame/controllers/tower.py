
def getTower(request, temp, gameData):
    response = {}
    response['userId'] = 1
    response['teamLevel'] = 65
    response['points'] = "62370"
    response['maySkipFloor'] = '26'
    response['floorNumber'] = '48'
    response['floorType'] = 'chest'

    response['states'] = {}
    response['states']['heroes'] = getTowerHeroes(temp, gameData)
    response['states']['mercenaries'] = []

    response['effects'] = getTowerEffects(temp, gameData)
    response['floor'] = getFloor(temp, gameData)
    response['reward'] = getTowerReward(temp, gameData)

    response['mayBuySkip'] = True
    response['mayFullSkip'] = False
    response['skipBought'] = False
    response['chestSkip'] = False
    response['fullSkipCost'] = {"starmoney": 1150}

    response['pointRewards'] = getTowerPointReward(temp, gameData)
    return response


def getTowerHeroes(temp, gameData):
    result = {}
    result['3'] = {
            'hp': 17000,
            'energy': '1000',
            'isDead': False,
            'maxHp': 17000,
            }
    return result


def getTowerEffects(temp, gameData):
    result = {}
    result['percentBuff_allAttacks'] = 0
    result['percentBuff_magicResist'] = 0
    result['percentBuff_armor'] = 0
    return result


def getFloor(temp, gameData):
    result = {}
    chests = []
    chests.append({'num': 0, 'opened': 0})
    chests.append({'num': 1, 'opened': 1, 'reward': {'gold': 90000}, 'critMultiplier': 1})
    chests.append({'num': 2, 'opened': 0})
    result['chests'] = chests

    chestRewards = {}
    result['chestRewards'] = chestRewards
    chestRewards['gold'] = {'gold': 90000}
    chestRewards['item'] = {'fragmentGear': {'94': '6'}}
    chestRewards['coin'] = {'coin': {'3': '250'}}
    return result


def getTowerReward(temp, gameData):
    result = {}
    result['4'] = {'gold': 45000}
    result['8'] = {'gold': 45000}
    result['10'] = {'gold': 45000}
    result['14'] = {'gold': 45000}
    result['16'] = {'gold': 45000}
    result['20'] = {'gold': 45000}
    result['22'] = {'gold': 45000}
    result['26'] = {'gold': 45000}
    result['28'] = {'gold': 45000}
    result['32'] = {'gold': 45000}
    result['35'] = {'gold': 45000}
    result['39'] = {'gold': 45000}
    result['42'] = {'gold': 45000}
    result['46'] = {'gold': 45000}
    result['50'] = {'gold': 45000}
    return result


def getTowerPointReward(temp, gameData):
    result = {}
    result['200'] = True
    result['3000'] = True
    result['10000'] = True
    result['15000'] = True
    result['20000'] = True
    result['25000'] = True
    result['35000'] = True
    result['45000'] = True
    result['60000'] = False
    return result
