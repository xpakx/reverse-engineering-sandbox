from extractors.lib import getStatAsInt


def buyStamina(request, temp, gameData):
    print(request)
    return {'stamina': 120}


def useStaminaItem(request, temp, gameData):
    print(request)
    itemId = getStatAsInt(request['args'], 'libId')
    amount = getStatAsInt(request['args'], 'amount')
    return []
