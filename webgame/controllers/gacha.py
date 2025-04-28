import random


def summonHero(request, temp, gameData):
    print(request)
    isFreeSummon = request['args']['free']
    isPackSummon = request['args']['pack']
    summons = 10 if isPackSummon else 1
    canSummon = checkResources(isFreeSummon, summons)
    if not canSummon:
        return []  # TODO

    response = {}
    response['onceRolled'] = []
    response["guaranteedOfferCount"] = []
    response['wishlist'] = [3, 3, 3, 3, 3]

    rareFragments = {}
    commonFragments = {}
    fragmentList = None

    for _ in range(summons):
        rarity, reward = gachaPull()
        if rarity == 'rare':
            fragmentList = rareFragments
        else:
            fragmentList = commonFragments
        id = str(reward)
        if id not in fragmentList:
            fragmentList[id] = 0
        fragmentList[id] = fragmentList[id] + 5

    response['reward'] = {}
    if len(rareFragments) > 0:
        response['reward']['rare'] = {
                'fragmentHero': rareFragments
            }
    if len(commonFragments) > 0:
        response['reward']['common'] = {
                'fragmentHero': commonFragments
            }

    return response


# TODO
def checkResources(isFreeSummon: bool, summons: int):
    return True


rare_list = [5, 7]
common_list = [1, 2, 3]


def gachaPull():
    roll = random.random()
    if roll <= 0.05:
        return 'rare', random.choice(rare_list)
    else:
        return 'common', random.choice(common_list)
