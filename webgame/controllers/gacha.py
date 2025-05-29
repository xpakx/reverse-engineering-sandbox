import random
from repo.userdata import GameRepository
from repo.item import ItemDef, Inventory


def summonHero(request, repo: GameRepository, gameData):
    print(request)
    isFreeSummon = request['args']['free']
    isPackSummon = request['args']['pack']
    summons = 10 if isPackSummon else 1
    inventory = repo.getInventoryByUserId(1)
    canSummon = checkResources(inventory, isFreeSummon, summons)
    if not canSummon:
        return []  # TODO

    response = {}
    response['onceRolled'] = []
    response["guaranteedOfferCount"] = []
    response['wishlist'] = [3, 3, 3, 3, 3]

    rareFragments = []
    commonFragments = []
    fragmentList = None

    for _ in range(summons):
        rarity, reward = gachaPull()
        if rarity == 'rare':
            fragmentList = rareFragments
        else:
            fragmentList = commonFragments
        rew = {}
        rew[str(reward)] = 5
        fragmentList.append(rew)
        inventory.addItem(
                ItemDef(
                    itemType='fragmentHero',
                    itemId=reward,
                    itemCount=5))

    rare = []
    common = []
    response['rewards'] = {}
    response['rewards']['rare'] = rare
    response['rewards']['common'] = common
    for frag in rareFragments:
        rare.append({
                'fragmentHero': frag
            })
    for frag in commonFragments:
        common.append({
                'fragmentHero': frag
            })

    return response


def checkResources(inventory: Inventory, isFreeSummon: bool, summons: int):
    itemType = "coin" if isFreeSummon else "starmoney"
    cost = summons if isFreeSummon else (
            summons*200 if summons < 10 else summons*150)
    cost = ItemDef(
            itemId=38,
            itemCount=cost,
            itemType=itemType
        )
    enoughResources = inventory.checkItem(cost)
    if not enoughResources:
        return False
    inventory.removeItem(cost)
    return True


rare_list = [5, 7]
common_list = [1, 2, 3]


def gachaPull():
    roll = random.random()
    if roll <= 0.05:
        return 'rare', random.choice(rare_list)
    else:
        return 'common', random.choice(common_list)
