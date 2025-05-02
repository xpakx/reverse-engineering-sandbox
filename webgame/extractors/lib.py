from typing import NamedTuple, Dict, List, Any, Tuple, Optional
import json
from datetime import time, datetime

attrs = ["strength", "agility", "intelligence", "hp",
         "physicalCritChance", "physicalAttack",
         "magicResist", "magicPower", "magicPenetration",
         "lifesteal", "dodge", "armorPenetration", "armor"]

colors = ['white', 'green', 'green+1', 'blue', 'blue+1', 'blue+2',
          'violet', 'violet+1', 'violet+2', 'violet+3', 'orange',
          'orange+1', 'orange+2', 'orange+3', 'orange+4', 'red',
          'red+1', 'red+2']


class StatData(NamedTuple):
    strength: int = 0
    agility: int = 0
    intelligence: int = 0
    hp: int = 0
    physicalCritChance: int = 0
    physicalAttack: int = 0
    magicResist: int = 0
    magicPower: int = 0
    magicPenetration: int = 0
    lifesteal: int = 0
    dodge: int = 0
    armorPenetration: int = 0
    armor: int = 0

    def print(self):
        for attr in attrs:
            if not hasattr(self, attr):
                continue
            if getattr(self, attr) == 0:
                continue
            print("   ", f'{attr}:', getattr(self, attr))


class GearData(NamedTuple):
    id: int = 0
    battleStats: StatData = StatData()
    teamLevel: int = 0
    heroLevel: int = 0
    sellCost: Dict[str, int] = 0
    buyCost: Dict[str, int] = 0
    color: int = 1


class HeroData(NamedTuple):
    id: int = 0
    baseStats: StatData = StatData()
    mainStat: str = 'strength'
    scale: int = 1
    stars: Dict[int, StatData] = {}
    color: Dict[int, Tuple[StatData, List[GearData]]] = {}
    perk: List[int] = []
    skills: List[int] = []
    heroSkills: List[int] = []
    artifacts: Any = None
    runes: Any = None


class Hero:
    def __init__(self, data: HeroData):
        self.data = data
        base = data.baseStats
        self.strength = base.strength
        self.physicalCritChance = base.physicalCritChance
        self.physicalAttack = base.physicalAttack
        self.magicResist = base.magicResist
        self.magicPower = base.magicPower
        self.magicPenetration = base.magicPenetration
        self.lifesteal = base.lifesteal
        self.intelligence = base.intelligence
        self.hp = base.hp
        self.dodge = base.dodge
        self.armorPenetration = base.armorPenetration
        self.armor = base.armor
        self.agility = base.agility
        self.color = 1
        self.level = 0
        self.stars = 0
        self.gear = []
        self.skills = []
        for skill in data.heroSkills:
            self.skills.append(0)

    def processBaseStats(self):
        self.physicalAttack = self.physicalAttack + 2 * self.agility + self.getMainAttr()
        self.hp = self.hp + 40 * self.strength
        self.armor = self.armor + self.agility
        self.magicPower = self.magicPower + 3 * self.intelligence
        self.magicResist = self.magicResist + self.intelligence

    def getMainAttr(self):
        if not hasattr(self, self.data.mainStat):
            return 0
        return getattr(self, self.data.mainStat)

    def update(self, stat: StatData, times: int = 1):
        for attr in attrs:
            if not hasattr(self, attr) or not hasattr(stat, attr):
                continue
            new_value = getattr(self, attr) + getattr(stat, attr) * times
            setattr(self, attr, new_value)

    def applyStarsAndLevel(self, stars: int, level: int):
        starsData = self.data.stars[stars]
        self.level = level
        self.stars = stars
        self.update(starsData, level)

    def applyColor(self, color: int):
        colorData = self.data.color[color]
        stats = colorData[0]
        self.color = color
        if stats:
            self.update(stats)

    def applyGear(self, gear: List[bool]):
        currColor = self.data.color[self.color]
        items = currColor[1]
        length = min(len(gear), len(items))
        self.gear = gear
        for i in range(0, length):
            if gear[i]:
                self.update(items[i].battleStats)

    def getBattleData(self):
        return {
                "id": self.data.id,
                "xp": 0,
                "level": self.level,
                "color": self.color,
                "slots": [0, 0, 0],
                "skills": {"432": 1},
                "power": 19156,
                "star": self.stars,
                "runes": [0, 0, 0, 0, 0],
                "skins": [],
                "currentSkin": 3,
                "titanGiftLevel": 0,
                "titanCoinsSpent": None,
                "artifacts": [
                    {"level": 1, "star": 0},
                    {"level": 1, "star": 0},
                    {"level": 1, "star": 0}
                ],
                "scale": 1,
                "petId": 0,
                "type": "hero",
                "perks": self.data.perk,
                "ascensions": [],
                "strength": self.strength,
                "agility": self.agility,
                "intelligence": self.intelligence,
            }

    def getProfileData(self):
        skills = {}
        skillIndex = 0
        for skill in self.data.heroSkills:
            skills[str(skill)] = self.skills[skillIndex]
            skillIndex += 1
        return {
            "id": self.data.id,
            "xp": 0,
            "level": self.level,
            "color": self.color,
            "slots": [0, 0, 0],
            "skills": skills,
            "power": 19156,
            "star": self.stars,
            "runes": [0, 0, 0, 0, 0],
            "skins": {str(self.data.id): 40},
            "currentSkin": self.data.id,
            "titanGiftLevel": 0,
            "titanCoinsSpent": {
                "consumable": {"24": 0}
                },
            "artifacts": [
                {"level": 1, "star": 0},
                {"level": 1, "star": 0},
                {"level": 1, "star": 0}
                ],
            "scale": 1,
            "petId": 0,
            "type": "hero",
            "perks": self.data.perk,
            "ascensions": []
        }


class WaveData(NamedTuple):
    enemies: List[Hero] = []


class DropData(NamedTuple):
    chance: int
    reward: Any


class MissionData(NamedTuple):
    cost: Dict[str, int] = {}
    tryCost: Dict[str, int] = {}
    heroExp: int = 0,
    teamExp: int = 0,
    waves: List[WaveData] = []
    drops: List[DropData] = []


def print_keys(data):
    for key in data:
        print(key)


def print_hero_types(data):
    heroTypes = set()
    if 'hero' not in data:
        return []
    for key in data['hero']:
        var = data['hero'][key]
        if 'type' not in var:
            continue
        heroTypes.add(var['type'])
    print(heroTypes)


def get_hero_type(data, heroType):
    if 'hero' not in data:
        return []
    heroes = []
    for key in data['hero']:
        var = data['hero'][key]
        if 'type' not in var:
            continue
        if var['type'] == heroType:
            heroes.append(var)
    return heroes


def get_heroes(data):
    return get_hero_type(data, 'hero')


def get_enemies(data):
    return get_hero_type(data, 'creep')


def get_missions(data):
    if 'mission' not in data:
        return []
    missions = []
    for key in data['mission']:
        var = data['mission'][key]
        missions.append(var)
    return missions


def getStat(data, attr) -> int:
    if attr not in data:
        return 0
    return data[attr]


def getStats(data) -> StatData:
    return StatData(
            strength=getStat(data, 'strength'),
            physicalCritChance=getStat(data, 'physicalCritChance'),
            physicalAttack=getStat(data, 'physicalAttack'),
            magicResist=getStat(data, 'magicResist'),
            magicPower=getStat(data, 'magicPower'),
            magicPenetration=getStat(data, 'magicPenetration'),
            lifesteal=getStat(data, 'lifesteal'),
            intelligence=getStat(data, 'intelligence'),
            hp=getStat(data, 'hp'),
            dodge=getStat(data, 'dodge'),
            armorPenetration=getStat(data, 'armorPenetration'),
            armor=getStat(data, 'armor'),
            agility=getStat(data, 'agility')
            )


def print_hero(data):
    print("Id:", data['id'])
    print(f'main stat: {data['mainStat']}')
    print("BASE STATS")
    baseStats = getStats(data['baseStats'])
    baseStats.print()

    print("STARS")
    stars = data['stars']
    for i in range(1, 7):
        if i in stars:
            print(i*'*')
            starStats = getStats(stars[i]['battleStatData'])
            starStats.print()
        if str(i) in stars:
            print(i*'*')
            starStats = getStats(stars[str(i)]['battleStatData'])
            starStats.print()

    print("ITEMS FOR COLOR")
    heroColors = data['color']
    for i in range(1, 19):
        if i in heroColors:
            print(colors[i-1])
            colorStats = getStats(heroColors[i]['battleStatData'])
            colorStats.print()
            print(heroColors[i]['items'])
        if str(i) in heroColors:
            print(colors[i-1])
            if 'battleStatData' in heroColors[str(i)]:
                # sum of all bonuses from earlier colors
                colorStats = getStats(heroColors[str(i)]['battleStatData'])
                colorStats.print()
            print(heroColors[str(i)]['items'])

    print("RUNES")
    print(data['runes'])

    print("ARTIFACTS")
    print(data['artifacts'])

    print(data['battleOrder'])
    print(data['scale'])
    print(data['type'])
    print(data['role'])
    print(data['obtainType'])
    print(data['characterType'])
    print(data['roleExtended'])
    print(data['perk'])
    print(data['fragmentBuyCost'])
    print(data['fragmentSellCost'])
    print(data['fragmentSpecialCost'])
    print(data['lockedUntil'])
    print(data['skill'])


def parseItems(data) -> Dict[int, GearData]:
    result = {}
    for item in data:
        gearEntry = data[item]
        stats = getStats(gearEntry['battleStatData'])
        id = int(gearEntry['id'])
        gear = GearData(
                id=id,
                battleStats=stats,
                teamLevel=gearEntry['teamLevel'],
                heroLevel=gearEntry['heroLevel'],
                sellCost=gearEntry['sellCost'],
                buyCost=gearEntry['buyCost'],
                color=gearEntry['color'],
                )
        result[id] = gear
    return result


def parseHero(data, gear, heroId) -> HeroData:
    baseStats = getStats(data['baseStats'])
    skills = []
    heroSkills = []
    if isinstance(data['skill'], list):
        skills = data['skill']
        if data['type'] == 'hero':
            heroSkills = skills[1:5]
    else:
        for i in data['skill']:
            key = int(i)
            skill = data['skill'][i]
            skills.append(skill)
            if data['type'] == 'hero' and key > 0 and key <= 4:
                heroSkills.append(skill)

    stars = {}
    for i in data['stars']:
        entry = data['stars'][i]
        stats = getStats(entry['battleStatData'])
        key = int(i)
        stars[key] = stats

    colors = {}
    for i in data['color']:
        entry = data['color'][i]
        stats = None
        if 'battleStatData' in entry:
            stats = getStats(entry['battleStatData'])
        items = []
        itemsIds = entry['items']
        for id in itemsIds:
            if id == 0:
                continue
            item = gear[id]
            items.append(item)
        key = int(i)
        colors[key] = (stats, items)

    return HeroData(
            id=heroId,
            baseStats=baseStats,
            mainStat=data['mainStat'],
            scale=data['scale'],
            perk=data['perk'],
            skills=skills,
            heroSkills=heroSkills,
            stars=stars,
            color=colors,
            )


def parseHeroes(data, gear) -> Dict[int, HeroData]:
    result = {}
    for item in data:
        heroEntry = data[item]
        id = int(heroEntry['id'])
        hero = parseHero(heroEntry, gear, id)
        result[id] = hero
    return result


def createHero(data: List[HeroData]):
    hero = Hero(data[3])
    hero.applyStarsAndLevel(2, 5)
    hero.applyColor(2)
    hero.applyGear([True, True, True])
    hero.processBaseStats()
    resp = {}
    for attr in attrs:
        value = getattr(hero, attr)
        resp[attr] = value
    response = json.dumps(resp)
    return response


def createEnemy(data: List[HeroData]):
    hero = Hero(data[1001])
    hero.applyStarsAndLevel(1, 1)
    hero.applyColor(1)
    hero.processBaseStats()
    resp = {}
    for attr in attrs:
        value = getattr(hero, attr)
        resp[attr] = value
    response = json.dumps(resp)
    return response


def getStatAsInt(data, stat: str, default: int = 0) -> int:
    if stat not in data:
        return default
    val = data[stat]
    if not isinstance(val, int):
        return int(val)
    return val


def parseWave(data, heroes, gear) -> WaveData:
    enemies = []
    for enemy in data['enemies']:
        # gid = enemy['gid']
        id = getStatAsInt(enemy, 'id')
        color = getStatAsInt(enemy, 'color', 1)
        level = getStatAsInt(enemy, 'lvl')
        stars = getStatAsInt(enemy, 'star')
        hero = Hero(heroes[id])
        if stars in hero.data.stars:
            hero.applyStarsAndLevel(stars, level)
        hero.applyColor(color)
        enemies.append(hero)
    return WaveData(enemies=enemies)


def parseWaveDrops(wave) -> List[DropData]:
    drops = []
    for enemy in wave['enemies']:
        if 'drop' not in enemy:
            continue
        drop = enemy['drop']
        if len(drop) > 0:
            for item in drop:
                drops.append(item)
    if len(drops) == 0:
        return []

    result = []
    for drop in drops:
        if 'reward' not in drop:
            continue
        chance = getStatAsInt(drop, 'chance')
        dropData = DropData(chance=chance, reward=drop['reward'])
        result.append(dropData)
    return result


def parseMissions(data, heroes, gear) -> Dict[int, MissionData]:
    result = {}
    for key in data:
        item = data[key]['normalMode']
        cost = item['cost']
        heroExp = item['heroExp']
        teamExp = item['teamExp']
        tryCost = item['tryCost']
        waves = []
        drops = []
        for wave in item['waves']:
            waveData = parseWave(wave, heroes, gear)
            waves.append(waveData)
            waveDrops = parseWaveDrops(wave)
            if len(waveDrops) > 0:
                drops.extend(waveDrops)
        missionsEntry = MissionData(
                cost=cost,
                heroExp=heroExp,
                teamExp=teamExp,
                tryCost=tryCost,
                waves=waves,
                drops=drops,
                )
        result[int(key)] = missionsEntry
    return result


class QuestEventData(NamedTuple):
    id: int = 0
    sortOrder: int = 1
    eventReward: Optional[Any] = None
    eventLoopData: Optional[Any] = None
    clientData: Optional[Any] = None
    icon: str = "event_icon_001"
    hideCompleted: Optional[bool] = None
    questChains: Optional[Any] = None
    background: str = ""
    localeKey: str = ""
    descLocale: str = ""
    nameLocale: str = ""
    notifLocale: str = ""

    def getForDate(self, startDate, endDate):
        result = {}
        result['id'] = self.id
        result["sortOrder"] = self.sortOrder
        result["eventReward"] = self.eventReward
        result["eventLoopData"] = self.eventLoopData
        result["clientData"] = self.clientData
        result["icon"] = self.icon
        result["hideCompleted"] = self.hideCompleted
        result["questChains"] = self.questChains
        result["background"] = self.background
        result["localeKey"] = self.localeKey
        result["desc_localeKey"] = self.descLocale
        result["name_localeKey"] = self.nameLocale
        result["notification_localeKey"] = self.notifLocale
        startTime = datetime.combine(startDate, time.min)
        endTime = datetime.combine(endDate, time.min)
        result["startTime"] = int(startTime.timestamp())
        result["endTime"] = int(endTime.timestamp())
        return result


class GameData(NamedTuple):
    heroes: Dict[int, HeroData] = {}
    items: Dict[int, GearData] = {}
    missions: Dict[int, MissionData] = {}
    questEvents: Dict[int, QuestEventData] = {}


def getOrDefault(data, stat: str, default: Any = None) -> Any:
    if stat not in data:
        return default
    val = data[stat]
    return val


def parseQuestEvents(data) -> Dict[int, QuestEventData]:
    result = {}
    for item in data:
        eventEntry = data[item]
        id = getStatAsInt(eventEntry, 'id')
        event = QuestEventData(
                id=id,
                sortOrder=getOrDefault(eventEntry, 'sortOrder', 1),
                eventReward=getOrDefault(eventEntry, 'eventReward'),
                eventLoopData=getOrDefault(eventEntry, 'eventLoopData'),
                clientData=getOrDefault(eventEntry, 'clientData'),
                icon=getOrDefault(eventEntry, 'icon', ''),
                hideCompleted=getOrDefault(eventEntry, 'hideCompleted'),
                questChains=getOrDefault(eventEntry, 'questChains'),
                background=getOrDefault(eventEntry, 'background', ''),
                localeKey=getOrDefault(eventEntry, 'localeKey', ''),
                descLocale=getOrDefault(eventEntry, 'desc_localeKey', ''),
                nameLocale=getOrDefault(eventEntry, 'name_localeKey', ''),
                notifLocale=getOrDefault(eventEntry, 'notification_localeKey', '')
                )
        result[id] = event
    return result


def prepareData(hash) -> GameData:
    input_file = f"./{hash}/indices/lib.json"

    with open(input_file, 'r') as f:
        data = json.load(f)
    gear = parseItems(data['inventoryItem']['gear'])
    heroes = parseHeroes(data['hero'], gear)
    missions = parseMissions(data['mission'], heroes, gear)
    questEvents = parseQuestEvents(data['specialQuestEvent']['type'])
    return GameData(
            heroes=heroes,
            items=gear,
            missions=missions,
            questEvents=questEvents
            )


def detectNewHeroes(data) -> bool:
    heroes = data['hero']
    for heroKey in heroes:
        hero = heroes[heroKey]
        if hero['type'] != 'hero':
            continue
        if hero['id'] > 66 and hero['id'] < 7002:
            return True
    return False


def unlockHero(data, id):
    id = str(id)
    hero = data['hero'][id]
    hero['lockedUntil'] = None
    with open(f"{input_file}.test", 'w') as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    input_file = "./a58c9976/indices/lib.json"

    with open(input_file, 'r') as f:
        data = json.load(f)

    if detectNewHeroes(data):
        print("New heroes in data")
    else:
        print("No new heroes in data")

    unlockHero(data, 67)


    # quests = data['quest']
    # print_keys(data)
    # print_keys(quests)
    # print()
    # print_keys(data['specialQuestEvent'])
    # print()
    # print(quests['special']['23149'])  # chain: 338
    # print(data['specialQuestEvent']['chain']['338'])
    # print(data['specialQuestEvent']['type']['68'])

    # quests = parseQuestEvents(data['specialQuestEvent']['type'])
    # print(quests[68])
    # 23149/68

    # missions = data['mission']
    # mission = missions['1']
    # normalMode = mission['normalMode']
    # print_keys(normalMode)
    # for wave in normalMode['waves']:
        # for enemy in wave['enemies']:
            # if 'drop' not in enemy:
                # continue
            # drop = enemy['drop']
            # if len(drop) > 0:
                # print(drop)
