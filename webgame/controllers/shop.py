
def getShops(request, temp, gameData):
    response = {}
    response['1'] = getTownShop(1)
    response['2'] = getTownShop(2)
    response['3'] = getTownShop(3)
    return response


def getTownShop(id):
    shop = {}
    shop['id'] = id
    shop['availableUntil'] = 0
    shop['refreshTime'] = 1745564400
    shop['slots'] = {}
    shop['slots'][1] = {
            'id': 1,
            "reward": {"consumable": {"11": "45"}},
            "bought": 0,
            "cost": {"gold": 450000}
            }
    return shop
