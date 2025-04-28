from extractors.lib import getStatAsInt


def buyStamina(request, temp, gameData):
    print(request)
    return {'stamina': 120}


def useStaminaItem(request, temp, gameData):
    print(request)
    itemId = getStatAsInt(request['args'], 'libId')
    amount = getStatAsInt(request['args'], 'amount')
    return []


def inventory(request, temp, gameData):
    return temp['inventory']


it = {
        'bottledEnergy': '17',
        'bigExp': '11',
    }


def getTestInventory():
    return {
            "consumable": {
                it['bigExp']: 20,
                it['bottledEnergy']: 30
            },
            "gear": {},
            "fragmentHero": {},
            "scroll": {},
            "coin": {},
            "fragmentGear": {},
            "fragmentScroll": {},
            "fragmentArtifact": {},
            "fragmentTitan": {},
            "fragmentTitanArtifact": {},
            "ascensionGear": {},
            "fragmentPet": {},
            "petGear": {}
        }


def addToInventory(temp, category: str, id: int, amount: int):
    inventory = temp['inventory']
    if category not in inventory:
        inventory[category] = {}

    cat = inventory[category]
    strId = str(id)
    if strId not in cat:
        cat[strId] = 0

    cat[strId] = cat[strId] + amount


def addMultToInventory(temp, reward):
    for category in reward:
        items = reward[category]
        if isinstance(items, dict):
            for item in items:
                id = int(item)
                addToInventory(temp, category, id, items[item])
