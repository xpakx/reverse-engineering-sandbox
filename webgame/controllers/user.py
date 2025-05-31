from repo.userdata import GameRepository

cookies = {'': '1'}


def register(request, repo: GameRepository, gameData):
    print(request)
    if 'name' not in request:
        return None
    if request['name'] != 'registration':
        print("Unknown name:", request['name'])
        return None

    cookie = request['context']['cookie']
    userId = cookies.get(cookie)

    response = {}
    response['isNewUser'] = True if userId else False
    response['userId'] = userId
    repo.tempUser = userId
    return response


def getInfo(request, repo: GameRepository, gameData):
    print(request)
    if not repo.tempUser:
        return {}
    inventory = repo.getInventoryByUserId(1)

    profile = {
            "id": "1",
            "name": "Sir Rocinante",
            "lastLoginTime": "1745545266",
            "serverId": "1",
            "level": "68",
            "clanId": "1",
            "clanRole": "2",
            "commander": False,
            "avatarId": "608",
            "isChatModerator": False,
            "frameId": 193,
            "leagueId": 2,
            "allowPm": "all",
            "accountId": "149848381",
            "timeZone": 2,
            "starMoney": inventory.emeralds,
            "vipPoints": "50000",
            "gold": inventory.gold,
            "refillable": [],
            "flags": "8",
            "tutorialStep": "9999",
            "nextDayTs": 1745550000,
            "nextServerDayTs": 1745546400,
            "experience": "253",
            "maxLevel": 130,
            "useEnergyBuyLimit": False,
            "vkPayIsActive": False,
            "registrationTime": "1743459278",
            "isCasualStart": False,
            "maxSumPower": { "heroes": 98580, "titans": 12916, "pets": 37490 }
            }

    stamina = repo.getStaminaByUserId(1)
    profile['refillable'].append(stamina.toResponse())
    for i in range(2, 61):
        profile['refillable'].append(
                {"id": i, "amount": 20, "lastRefill": 1745545328, "boughtToday": 0}
                )
    return profile
