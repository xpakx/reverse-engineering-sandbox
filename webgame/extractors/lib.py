from typing import NamedTuple, Dict, List, Any, Tuple, Optional, Union
import json
from datetime import time, datetime
from repo.item import ItemDef

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


class SkinData(NamedTuple):
    id: int = 0
    heroId: int = 0
    isDefault: bool = False
    stats: Dict[int, StatData] = {}
    costs: Dict[int, ItemDef] = {}
    enabled: bool = True
    notObtainable: bool = False
    default: bool = False


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
    skins: Dict[int, SkinData] = {}
    minStar: int = 1

    def getDefaultSkin(self) -> Optional[SkinData]:
        for skinKey in self.skins:
            skin = self.skins[skinKey]
            if skin.default:
                return skin
        return None


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
        self.experience = 0
        self.skills = []
        self.skinLevels = {}
        defaultSkin = self.data.getDefaultSkin()
        if defaultSkin:
            self.activeSkin = defaultSkin.id
            self.skinLevels[defaultSkin.id] = 1
        else:
            self.activeSkin = data.id
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

    def revert(self, stat: StatData, times: int = 1):
        for attr in attrs:
            if not hasattr(self, attr) or not hasattr(stat, attr):
                continue
            new_value = getattr(self, attr) - getattr(stat, attr) * times
            setattr(self, attr, new_value)

    def applyStarsAndLevel(self, stars: int, level: int):
        starsData = self.data.stars[stars]
        self.level = level
        self.stars = stars
        self.update(starsData, level)

    def revertStarsAndLevel(self, stars: int, level: int):
        starsData = self.data.stars[stars]
        self.revert(starsData, level)

    def applyColor(self, color: int):
        colorData = self.data.color[color]
        stats = colorData[0]
        self.color = color
        if stats:
            self.update(stats)

    def revertColor(self):
        colorData = self.data.color[self.color]
        stats = colorData[0]
        self.color = 1
        if stats:
            self.revert(stats)

    def applyGear(self, gear: List[bool]):
        currColor = self.data.color[self.color]
        items = currColor[1]
        print(items)
        length = min(len(gear), len(items))
        self.gear = gear
        for i in range(0, length):
            if gear[i]:
                self.update(items[i].battleStats)

    def removeGear(self):
        currColor = self.data.color[self.color]
        items = currColor[1]
        length = min(len(self.gear), len(items))
        for i in range(0, length):
            if self.gear[i]:
                self.revert(items[i].battleStats)

    def addExperience(self, experience: int, levelToExp: Dict[int, int]):
        self.experience += experience
        if (self.level + 1) not in levelToExp:
            return
        oldLevel = self.level

        levelExperience = levelToExp[self.level+1]
        while self.experience >= levelExperience:
            self.level += 1
            if self.level+1 not in levelToExp:
                break
            levelExperience = levelToExp[self.level+1]

        if self.level > oldLevel:
            self.revertStarsAndLevel(self.stars, oldLevel)
            self.applyStarsAndLevel(self.stars, self.level)

    def getBattleData(self):
        return {
                "id": self.data.id,
                "xp": self.experience,
                "level": self.level,
                "color": self.color,
                "slots": [0, 0, 0],
                "skills": {"432": 1},
                "power": 19156,
                "star": self.stars,
                "runes": [0, 0, 0, 0, 0],
                "skins": [],
                "currentSkin": self.activeSkin,
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

    def getGearData(self):
        print(self.data.id, self.gear)
        if all(self.gear):
            return [0]*len(self.gear)
        return {i: 0 for i, equipped in enumerate(self.gear) if equipped}

    def getProfileData(self):
        skills = {}
        skillIndex = 0
        for skill in self.data.heroSkills:
            skills[str(skill)] = self.skills[skillIndex]
            skillIndex += 1
        skins = self.skinLevels if len(self.skinLevels) > 0 else []
        return {
            "id": self.data.id,
            "xp": self.experience,
            "level": self.level,
            "color": self.color,
            "slots": self.getGearData(),
            "skills": skills,
            "power": 19156,
            "star": self.stars,
            "runes": [0, 0, 0, 0, 0],
            "skins": skins,
            "currentSkin": self.activeSkin,
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
    reward: List[ItemDef]


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
    minStar = 100
    for i in data['stars']:
        entry = data['stars'][i]
        stats = getStats(entry['battleStatData'])
        key = int(i)
        if key < minStar:
            minStar = key
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
            skins={},
            minStar=minStar,
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
    if not val:
        return default
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
            for category in drop:
                drops.append(category)
    if len(drops) == 0:
        return []

    result = []
    for drop in drops:
        if 'reward' not in drop:
            continue
        chance = getStatAsInt(drop, 'chance')

        items = []
        for category in drop['reward']:
            if category == 'gold':
                count = getStatAsInt(drop['reward'], 'gold')
                itemDef = ItemDef(itemType='gold', itemCount=count)
                items.append(itemDef)
            else:
                for key in drop['reward'][category]:
                    value = drop['reward'][category][key]
                    itemDef = ItemDef(
                            itemType=category,
                            itemCount=int(value),
                            itemId=int(key))
                    items.append(itemDef)
        dropData = DropData(chance=chance, reward=items)

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


class SpecialQuestData(NamedTuple):
    id: int = 0
    chainId: int = 0
    sortOrder: int = 0
    farmCondition: Any = None
    rewardSorting: Optional[int] = None
    disabled: bool = False
    daily: bool = False
    autoFarm: bool = False


class QuestChainData(NamedTuple):
    id: int = 0
    startCondition: Optional[Any] = None
    disabled: bool = False


class SpecialQuestChainData(NamedTuple):
    id: int = 0
    sortOrder: int = 0
    isInfinite: bool = False
    quests: List[QuestChainData] = []


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
    chains: List[Union[SpecialQuestChainData, QuestChainData]] = []

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
    skins: Dict[int, SkinData] = {}
    missions: Dict[int, MissionData] = {}
    questEvents: Dict[int, QuestEventData] = {}
    quests: Dict[int, SpecialQuestData] = {}
    levelToExp: Dict[int, int] = {}


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
                notifLocale=getOrDefault(eventEntry, 'notification_localeKey', ''),
                chains=[],
                )
        result[id] = event
    return result


def parseQuestChains(data) -> Dict[int, QuestChainData]:
    result = {}
    for key in data:
        eventEntry = data[key]
        id = getStatAsInt(eventEntry, 'id')
        disabled = getStatAsInt(eventEntry, 'disabled') != 0
        event = QuestChainData(
                id=id,
                disabled=disabled,
                startCondition=eventEntry['startCondition'],
                )
        result[id] = event
    return result


def parseSpecialQuestChains(data, questEvents: Dict[int, QuestEventData]) -> Dict[int, SpecialQuestChainData]:
    result = {}
    for key in data:
        chainEntry = data[key]
        id = getStatAsInt(chainEntry, 'id')
        sortOrder = getStatAsInt(chainEntry, 'sortOrder')
        isInfinite = getStatAsInt(chainEntry, 'isInfinite') != 0
        chain = SpecialQuestChainData(
                id=id,
                isInfinite=isInfinite,
                sortOrder=sortOrder,
                quests=[],
                )
        result[id] = chain

        if 'eventId' not in chainEntry:
            continue
        eventId = getStatAsInt(chainEntry, 'eventId')
        if eventId not in questEvents:
            continue
        event = questEvents[eventId]
        event.chains.append(chain)
    return result


def parseQuests(data, questChains: Dict[int, SpecialQuestChainData]) -> Dict[int, SpecialQuestData]:
    result = {}
    for key in data:
        questEntry = data[key]
        id = getStatAsInt(questEntry, 'id')
        sortOrder = getStatAsInt(questEntry, 'chainOrder')
        farmCondition = questEntry['farmCondition']
        disabled = getStatAsInt(questEntry, 'disabled') != 0
        daily = getStatAsInt(questEntry, 'daily') != 0
        autoFarm = getStatAsInt(questEntry, 'autoFarm') != 0

        quest = SpecialQuestData(
                id=id,
                farmCondition=farmCondition,
                sortOrder=sortOrder,
                disabled=disabled,
                daily=daily,
                autoFarm=autoFarm,
                )
        result[id] = quest

        if 'eventChainId' not in questEntry:
            continue
        chainId = getStatAsInt(questEntry, 'eventChainId')
        if chainId not in questChains:
            continue
        event = questChains[chainId]
        event.quests.append(quest)
    return result


def prepareData(hash) -> GameData:
    input_file = f"./{hash}/indices/lib.json"

    with open(input_file, 'r') as f:
        data = json.load(f)
    gear = parseItems(data['inventoryItem']['gear'])
    heroes = parseHeroes(data['hero'], gear)
    missions = parseMissions(data['mission'], heroes, gear)
    skins = parseSkins(data['skin'], heroes)

    questEvents = parseQuestEvents(data['specialQuestEvent']['type'])
    questChains = parseSpecialQuestChains(data['specialQuestEvent']['chain'], questEvents)
    updateChains(questEvents, questChains)
    quests = parseQuests(data['quest']['special'], questChains)
    levelToExp = parseLevels(data['level']['hero'])

    return GameData(
            heroes=heroes,
            items=gear,
            missions=missions,
            questEvents=questEvents,
            quests=quests,
            levelToExp=levelToExp,
            skins=skins,
            )


def updateChains(events, chains):
    for eventKey in events:
        event = events[eventKey]
        if not event.questChains:
            continue
        for id in event.questChains:
            if id in chains:
                event.chains.append(chains[id])


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


def compareEvents(hashOld, hashNew):
    file = f"./{hashNew}/indices/lib.json"
    with open(file, 'r') as f:
        data = json.load(f)
    oldFile = f"./{hashOld}/indices/lib.json"
    with open(oldFile, 'r') as f:
        dataOld = json.load(f)

    quests = parseQuestEvents(data['specialQuestEvent']['type'])
    questsOld = parseQuestEvents(dataOld['specialQuestEvent']['type'])
    newKeys = []
    for key in quests:
        if key not in questsOld:
            newKeys.append(int(key))

    print(newKeys)


def compareSpecialQuests(hashOld, hashNew, questType):
    file = f"./{hashNew}/indices/lib.json"
    with open(file, 'r') as f:
        data = json.load(f)
    oldFile = f"./{hashOld}/indices/lib.json"
    with open(oldFile, 'r') as f:
        dataOld = json.load(f)

    quests = parseQuests(data['quest'][questType], {})
    questsOld = parseQuests(dataOld['quest'][questType], {})
    newKeys = []
    for key in quests:
        if key not in questsOld:
            newKeys.append(int(key))

    print(newKeys)


def parseLevels(data):
    result = {}
    for key in data:
        exp = data[key]['exp']
        result[int(key)] = exp
    return result


def parseSkins(data, heroes: Dict[int, HeroData]) -> List[SkinData]:
    result = {}
    for key in data:
        skin = data[key]
        id = getStatAsInt(skin, 'id')
        heroId = getStatAsInt(skin, 'heroId')
        default = getStatAsInt(skin, 'isDefault') == 1
        stats = {}
        costs = {}
        for levelKey in skin['statData']['levels']:
            level = skin['statData']['levels'][levelKey]
            lvl = getStatAsInt(level, 'level')
            statsData = getStats(level['statBonus'])
            costDict = level['cost']
            if costDict:
                costType = next(iter(costDict), 'coin')
                costValue = costDict[costType]
                costId = next(iter(costValue), 0)
                costAmount = costValue[costId]
                cost = ItemDef(
                        itemType=costType,
                        itemId=int(costId),
                        itemCount=costAmount,
                        )
                costs[lvl] = cost
            stats[lvl] = statsData

        skinData = SkinData(
                id=id,
                heroId=heroId,
                stats=stats,
                costs=costs,
                default=default,
                )
        result[id] = skinData

        hero = heroes[heroId]
        if not hero:
            continue
        hero.skins[id] = skinData
    return result


if __name__ == "__main__":
    # compareSpecialQuests('91c10ca0', 'f867035b', 'special')
    # compareEvents('91c10ca0', 'f867035b')
    input_file = "./82048d36/indices/lib.json"

    with open(input_file, 'r') as f:
        data = json.load(f)

    print_keys(data['skin']['1'])
    print(data['skin']['3'])
    gear = parseItems(data['inventoryItem']['gear'])
    heroes = parseHeroes(data['hero'], gear)
    skins = parseSkins(data['skin'], heroes)
    # print(skins[3])

    # print_keys(data['quest'])
