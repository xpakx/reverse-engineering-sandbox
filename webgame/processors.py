from controllers.user import register, getInfo
from controllers.campaign import startMission, endMission, raidMission
from controllers.heroes import getUserHeroes
from extractors.lib import GameData
from typing import NamedTuple, Any


class Processor(NamedTuple):
    process: Any = None
    ident: str = 'body'


class RequestProcessor:
    def __init__(self):
        self.processors = {}
        self.registerBodyProcessor('missionStart', startMission)
        self.registerBodyProcessor('missionEnd', endMission)
        self.registerBodyProcessor('missionRaid', raidMission)
        self.registerProcessor('registration', register)
        self.registerProcessor('userGetInfo', getInfo)
        self.registerProcessor('heroGetAll', getUserHeroes)

    def registerProcessor(self, name, processor, ident=None):
        id = ident if ident else name
        self.processors[name] = Processor(process=processor, ident=id)

    def registerBodyProcessor(self, name, processor):
        self.registerProcessor(name, processor, 'body')

    def callProcessor(self, processor, request, temp, gameData: GameData):
        response = {}
        response['ident'] = processor.ident
        if request['ident'] != 'body':
            response['ident'] = request['ident']
        response['result'] = {"response": processor.process(request, temp, gameData)}
        return response

    def process(self, request, temp, gameData: GameData):
        call = request['name']
        if call in self.processors:
            return self.callProcessor(self.processors[call], request, temp, gameData)

        if (call == 'userMergeGetStatus'):
            return register(request, temp, gameData)
        if (call == 'friendsGetInfo'):
            return friends(request)
        if (call == 'billingGetAll'):
            return billing(request)
        if (call == 'inventoryGet'):
            return inventory(request)
        if (call == 'titanGetAll'):
            return titans(request)
        if (call == 'titanSpiritGetAll'):
            return titanSpirits(request)
        if (call == 'pet_getAll'):
            return pets(request)
        if (call == 'pet_getPotionDailyBuyCount'):
            return petPotions(request)
        if (call == 'missionGetAll'):
            return missions(request)
        if (call == 'missionGetReplace'):
            return missionReplace(request)
        if (call == 'dailyBonusGetInfo'):
            return dailyBonus(request)
        if (call == 'getTime'):
            return time(request)
        if (call == 'teamGetAll'):
            return team(request)
        if (call == 'teamGetFavor'):
            return teamFavor(request)
        if (call == 'team_getBanners'):
            return teamBanners(request)
        if (call == 'clan_prestigeGetInfo'):
            return clanPrestige(request)
        if (call == 'questGetAll'):
            return quests(request)
        if (call == 'questGetEvents'):
            return questEvents(request)
        if (call == 'mailGetAll'):
            return mail(request)
        if (call == 'arenaGetAll'):
            return arena(request)
        if (call == 'socialQuestGetInfo'):
            return socialQuest(request)
        if (call == 'telegramQuestGetInfo'):
            return telegramQuest(request)
        if (call == 'userGetAvailableAvatars'):
            return avatars(request)
        if (call == 'userGetAvailableAvatarFrames'):
            return avatarFrames(request)
        if (call == 'userGetAvailableStickers'):
            return stickers(request)
        if (call == 'settingsGetAll'):
            return settings(request)
        if (call == 'subscriptionGetInfo'):
            return subscription(request)
        if (call == 'zeppelinGiftGet'):
            return zeppelinGift(request)
        if (call == 'tutorialGetInfo'):
            return tutorial(request)
        if (call == 'specialOffer_getAll'):
            return specialOffer(request)
        if (call == 'splitGetAll'):
            return splits(request)
        if (call == 'billingGetLast'):
            return billing(request)
        if (call == 'artifactGetChestLevel'):
            return artifactChest(request)
        if (call == 'titanArtifactGetChest'):
            return titanArtifactChest(request)
        if (call == 'titanGetSummoningCircle'):
            return titanSummoningCircle(request)
        if (call == 'newYearGetInfo'):
            return newYearInfo(request)
        if (call == "clanWarGetBriefInfo"):
            return clanWarInfo(request)
        if (call == "crossClanWar_getBriefInfo"):
            return crossClanWarInfo(request)
        if (call == "crossClanWar_getSettings"):
            return crossClanSettings(request)
        if (call == "clanWarGetWarlordInfo"):
            return clanWarWarlord(request)
        if (call == "campaignStoryGetList"):
            return campaignStoryList(request)
        if (call == "roleAscension_getAll"):
            return roleAscension(request)
        if (call == "chatsGetAll"):
            return chats(request)
        if (call == "chatGetTalks"):
            return chatTalks(request)
        if (call == "chatGetInfo"):
            return chatInfo(request)
        if (call == "clanGetInfo"):
            return clan(request)
        if (call == "clanGetActivityRewardTable"):
            return clanActivityRewards(request)
        if (call == "clanGetPrevData"):
            return clanPrevData(request)
        if (call == "heroesMerchantGet"):
            return heroesMerchant(request)
        if (call == "freebieHaveGroup"):
            return freebie(request)
        if (call == "pirateTreasureIsAvailable"):
            return pirateTreasure(request)
        if (call == "expeditionGet"):
            return expeditions(request)
        if (call == "hallOfFameGetTrophies"):
            return hallOfFame(request)
        if (call == "titanArenaCheckForgotten"):
            return titanArena(request)
        if (call == "titanArenaGetChestReward"):
            return titanArenaChest(request)
        if (call == "bossGetAll"):
            return bosses(request)
        if (call == "shopGetAll"):
            return shops(request)
        if (call == "adventure_getPassed"):
            return adventuresPassed(request)
        if (call == "adventure_getActiveData"):
            return adventuresActive(request)
        if (call == "adventure_find"):
            return adventuresFind(request)
        if (call == "adventureSolo_getActiveData"):
            return adventuresSolo(request)
        if (call == "pet_getChest"):
            return petChest(request)
        if (call == "playable_getAvailable"):
            return playable(request)
        if (call == "seasonAdventure_getInfo"):
            return seasonAdventure(request)
        if (call == "clanDomination_getInfo"):
            return clanDomination(request)
        if (call == "clanRaid_ratingInfo"):
            return clanRaidRating(request)
        if (call == "clanRaid_getInfo"):
            return clanRaid(request)
        if (call == "coopBundle_getInfo"):
            return coopBundle(request)
        if (call == "buffs_getInfo"):
            return buffs(request)
        if (call == "brawl_getInfo"):
            return brawl(request)
        if (call == "brawl_questGetInfo"):
            return brawlQuests(request)
        if (call == "epicBrawl_getBriefInfo"):
            return epicBrawl(request)
        if (call == "epicBrawl_getWinStreak"):
            return epicBrawlStreak(request)
        if (call == "stronghold_getInfo"):
            return stronghold(request)
        if (call == "mechanicsBan_getInfo"):
            return mechanicsBan(request)
        if (call == "gacha_getInfo"):
            return gacha(request)
        if (call == "heroRating_getInfo"):
            return heroRating(request)
        if (call == "offerwall_getActive"):
            return offerwall(request)
        if (call == "banner_getAll"):
            return banners(request)
        if (call == "idle_getAll"):
            return idle(request)
        if (call == "workshopBuff_getInfo"):
            return workshopBuff(request)
        if (call == "rewardedVideo_boxyGetInfo"):
            return videos(request)
        if (call == "newHeroNotification_get"):
            return newHeroes(request)
        if (call == "powerTournament_getState"):
            return powerTournament(request)
        if (call == "mechanicAvailability"):
            return mechanics(request)
        if (call == "towerGetInfo"):
            return tower(request)
        if (call == "battlePass_getInfo"):
            return battlePass(request)
        if (call == "battlePass_getSpecial"):
            return specialBattlePass(request)

        print("Unknown command:", call)
        return None


def friends(request):
    return {
            "ident": "friendsGetInfo",
            "result": {
                "response": {
                    "accounts": [],
                    "users": []
                    }
                }
            }


def billing(request):
    return {"ident":"billingGetAll","result":{"response":{"billings":[],"bundle":[]}}}


def inventory(request):
    return {"ident":"inventoryGet","result":{"response":{"consumable":{"14":1},"gear":{},"fragmentHero":{},"scroll":{},"coin":{},"fragmentGear":{},"fragmentScroll":{},"fragmentArtifact":{},"fragmentTitan":{},"fragmentTitanArtifact":{},"ascensionGear":{},"fragmentPet":{},"petGear":{}}}}


def titans(request):
    return {"ident":"titanGetAll","result":{"response":{}}}


def titanSpirits(request):
    return {"ident":"titanSpiritGetAll","result":{"response":{"water":{"id":4001,"level":1,"star":0},"fire":{"id":4002,"level":18,"star":1},"earth":{"id":4003,"level":1,"star":0},"dark":{"id":4004,"level":1,"star":0},"light":{"id":4005,"level":1,"star":0}}}}


def pets(request):
    return {"ident":"pet_getAll","result":{"response":[]}}


def petPotions(request):
    return {"ident":"pet_getPotionDailyBuyCount","result":{"response":0}}


def missions(request):
    result = {"ident":"missionGetAll","result":{"response":[]}}
    for i in range(1, 10):
        result['result']['response'].append(
                {"id":i,"stars":3,"triesSpent":0,"resetToday":0,"attempts":22,"wins":22}
            )
    return result


def missionReplace(request):
    return {"ident":"missionGetReplace","result":{"response":None}}


def dailyBonus(request):
    return {"ident":"dailyBonusGetInfo","result":{"response":{"year":"2025","month":4,"currentDay":"11","availableToday":False,"availableVip":True,"daysInMonth":30,"heroId":3}}}


def time(request):
    return {"ident":"getTime","result":{"response":1745545329}}


def team(request):
    return {"ident":"teamGetAll","result":{"response":{"mission":[],"arena":[],"tower":[],"boss_11":[],"boss_12":[],"boss_10":[],"dungeon_water":[],"dungeon_hero":[],"dungeon_neutral":[],"dungeon_fire":[],"brawl_titan":[],"clanDefence_heroes":[],"clanDefence_titans":[],"adventure_hero":[],"dungeon_earth":[],"clan_pvp_hero":[],"clan_pvp_titan":[],"crossClanDefence_heroes":[[],[],[]],"crossClanDefence_titans":[[],[]],"titan_arena_def":[],"titan_arena":[],"clan_global_pvp_titan":[],"clan_global_pvp":[],"clanRaid_nodes":[[],[]],"grand":[[],[],[]]}}}


def teamFavor(request):
    return {"ident":"teamGetFavor","result":{"response":{"__legacy":[],"mission":[],"arena_def":[],"arena":[],"tower":[],"boss_11":[],"boss_12":[],"boss_10":[],"dungeon_water":None,"dungeon_hero":[],"dungeon_neutral":None,"dungeon_fire":None,"brawl_titan":[],"clanDefence_heroes":[],"clanDefence_titans":[],"adventure_hero":[],"dungeon_earth":None,"clan_pvp_hero":[],"clan_pvp_titan":None,"crossClanDefence_heroes":[],"crossClanDefence_titans":[],"grand_def":[],"titan_arena_def":None,"titan_arena":None,"clan_global_pvp_titan":None,"clan_global_pvp":[],"clanRaid_nodes":[],"grand":[]}}}


def teamBanners(request):
    return {"ident":"team_getBanners","result":{"response":{"mission":None,"arena_def":None,"arena":None,"tower":None,"boss_11":None,"boss_12":None,"boss_10":None,"dungeon_water":None,"dungeon_hero":None,"dungeon_neutral":None,"dungeon_fire":None,"clanDefence_heroes":None,"clanDefence_titans":None,"adventure_hero":None,"dungeon_earth":None,"clan_pvp_hero":None,"clan_pvp_titan":None,"crossClanDefence_heroes":[None,None,None],"crossClanDefence_titans":[None,None,None],"grand_def":[None,None,None],"titan_arena":None,"clan_global_pvp_titan":None,"clan_global_pvp":None,"grand":[None,None,None]}}}


def quests(request):
    result = {"ident":"questGetAll","result":{"response":[]}}
    result['result']['response'].append({
    "id": 23151,
    "state": 2,
    "progress": 3,
    "reward": {
        "gold": 30000,
        "fragmentHero": {
            "60": 3
        }
    },
    "createTime": 1745104656
        })
    return result


def questEvents(request):
    result = {"ident":"questGetEvents","result":{"response":[]}}
    result['result']['response'].append({
        "id": 68,
        "sortOrder": 1,
        "eventReward": None,
        "eventLoopData": None,
        "clientData": None,
        "icon": "event_icon_001",
        "hideCompleted": None,
        "questChains": None,
        "background": "event_background_001.jpg",
        "localeKey": "LIB_SPECIAL_QUEST_EVENT_NAME_3",
        "desc_localeKey": "LIB_SPECIAL_QUEST_EVENT_DESC_3",
        "name_localeKey": "LIB_SPECIAL_QUEST_EVENT_NAME_3",
        "notification_localeKey": "",
        "startTime": 1745104656,
        "endTime": 1745709456
        })
    return result


def clanPrestige(request):
    return {"ident":"clan_prestigeGetInfo","result":{"response":{"prestigeId":2,"prestigeCount":379400,"userPrestigeCount":22665,"farmedPrestigeLevels":[1],"endTime":1746496800,"prestigeStartPopupViewed":True,"nextTime":1746583200}}}


def mail(request):
    return {"ident":"mailGetAll","result":{"response":{"letters":[],"users":[]}}}


def arena(request):
    return {"ident":"arenaGetAll","result":{"response":{"userId":"1","arenaPlace":"257","arenaHeroes":[],"grandPlace":"579","grandHeroes":[[],[],[]],"grandCoin":31.265900000000002,"grandCoinTime":1745545329,"arenaPower":"84873","grandPower":"122338","rewardFlag":"0","battles":45,"wins":33,"rewardTime":1745604000}}}


def socialQuest(request):
    return {"ident":"socialQuestGetInfo","result":{"response":{"farmed":True}}}


def telegramQuest(request):
    return {"ident":"telegramQuestGetInfo","result":{"response":{"twitter":"1","youtube":"1","push":True,"discord":True,"favorites":"1","emailConfirmed":True,"post":"","group":"","notifications":True}}}


def avatars(request):
    return {"ident":"userGetAvailableAvatars","result":{"response":[1325, 92, 93]}}


def avatarFrames(request):
    return {"ident":"userGetAvailableAvatarFrames","result":{"response":{"frames":[],"progress":{"41":{"frameId":41,"current":0,"max":1}}}}}


def stickers(request):
    return {"ident":"userGetAvailableStickers","result":{"response":[2]}}


def settings(request):
    return {"ident":"settingsGetAll","result":{"response":{"cookie":"nocookie","currency":"PLN","sounds":False,"music":False,"theme":True,"heroesBrowsedStatusMask":"qgNJACgAAAo","autoBattleToggle":True,"inventoryLootBoxBrowsedCount":23,"pveSpeedUpToggleIndex":1,"enableUltCinematic":False,"showHeroGachaWishlistTutorial":False,"playThemeMusicByHero":"AAA","titansBrowsedStatusMask":"AwBQwAMH","towerSpeedUpToggleIndex":0,"petsBrowsedStatusMask":"xQI","titanDungeonSpeedUpToggleIndex":1,"adventureChatBrowsingTime":1745284165,"lastBrowsedShopByGoldClanRaidStartTime":1745200800,"lastBrowsedShopByCoinsClanRaidStartTime":1745200800}}}


def subscription(request):
    return {"ident":"subscriptionGetInfo","result":{"response":{"subscription":None,"dailyReward":{"availableFarm":False,"dailyReward":{"coin":{"14":"400"}},"notFarmedDays":0,"currentReward":None}}}}


def zeppelinGift(request):
    return {"ident":"zeppelinGiftGet","result":{"response":{"available":False,"reward":{"consumable":{"45":1}}}}}


def tutorial(request):
    return {"ident":"tutorialGetInfo","result":{"response":{"chains":{"1":9999,"3":9999,"18":9999,"25":1,"2":9999,"4":9999,"5":9999,"6":9999,"7":9999,"8":9999,"9":9999,"10":0,"11":9999,"13":9999,"14":9999,"15":0,"16":0,"17":9999,"26":0,"29":0,"27":9999,"28":9999,"31":0,"33":0},"params":{"heroIcon1":"hero2","heroIcon2":"hero20","heroName1":"LIB_HERO_NAME_2","heroName2":"LIB_HERO_NAME_20","tutorialBattleEndTime":"5.46"}}}}


def specialOffer(request):
    return {"ident":"specialOffer_getAll","result":{"response":[]}}


def splits(request):
    return {"ident":"splitGetAll","result":{"response":[{"rule":{"stash":{"flushIntervalStart":1000,"flushIntervalDefault":5000}}},None]}}


def lastBilling(request):
    return {"ident":"billingGetLast","result":{"response":None}}


def artifactChest(request):
    return {"ident":"artifactGetChestLevel","result":{"response":{"level":3,"xp":60,"starmoneySpent":800}}}


def titanArtifactChest(request):
    return {"ident":"titanArtifactGetChest","result":{"response":{"starmoneySpent":4500}}}


def titanSummoningCircle(request):
    return {"ident":"titanGetSummoningCircle","result":{"response":{"starmoneySpent":700}}}


def newYearInfo(request):
    return {"ident":"newYearGetInfo","result":{"response":{"treeLevel":0,"treeExpPercent":0,"giftsToOpen":0,"eventHero":64,"dayHero":51}}}


def clanWarInfo(request):
    return {"ident":"clanWarGetBriefInfo","result":{"response":{"tries":0,"targets":0,"arePointsMax":True,"nextWarTime":1745571600,"hasActiveWar":False,"nearestWarEndTime":175611200}}}


def crossClanWarInfo(request):
    return {"ident":"crossClanWar_getBriefInfo","result":{"response":{"status":"active","hasActiveWar":True,"hasEnoughDefendedSlots":True,"seasonEndTime":1751767200,"nextSeasonStartTime":1752458400,"nextWarTime":1745810100,"heroTries":3,"titanTries":2,"heroTargets":0,"titanTargets":0,"currentWarEndTime":1745719200}}}


def crossClanSettings(request):
    return {"ident":"crossClanWar_getSettings","result":{"response":{"fillDefenceByCommander":False}}}


def clanWarWarlord(request):
    return {"ident":"clanWarGetWarlordInfo","result":{"response":None}}


def campaignStoryList(request):
    return {"ident":"campaignStoryGetList","result":{"response":[]}}


def roleAscension(request):
    return {"ident":"roleAscension_getAll","result":{"response":{"3":{"id":3,"level":14}}}}


def chats(request):
    return {"ident":"chatsGetAll","result":{"response":{"clan":{"chat":[],"users":{},"clans":[]},"xgvg":{"chat":[],"users":{},"clans":[]}}}},


def chatTalks(request):
    return {"ident":"chatGetTalks","result":{"response":{"talks":[],"users":{}}}},


def chatInfo(request):
    return {"ident":"chatGetInfo","result":{"response":{"banUntil":"0","subscribeServer":"0","lastMessageTime":"1745049961","blackList":[],"settings":{"chatSelectedTab":"CLAN_TAB","lastReadMessageId":90058375,"lastReadClanNewsHash":"f7086b389381c5b3f5d3cb07a4671ee7","lastReadTrainingMessageId":89994080,"lastReadXGVGMessageId":90050415}}}}


def clan(request):
    return {"ident":"clanGetInfo","result":{"response":{"clan":{"id":"1","ownerId":"2","level":"1","title":"SuperClan","description":"","icon":{"flagColor1":4,"flagColor2":5,"flagShape":3,"iconColor":1,"iconShape":3},"country":"7","minLevel":"30","serverId":"457","membersCount":"20","disbanding":False,"topActivity":"187676","topDungeon":"19052","roleNames":[],"frameId":2,"members":{},"news":"","activityPoints":22163,"dungeonPoints":1988,"blackList":[],"warriors":[],"giftsCount":0,"daysToKick":"14","league":"2"},"membersStat":[],"stat":{"todayActivity":2494,"activitySum":22153,"dungeonActivitySum":1255,"todayRaid":[],"todayItemsActivity":0,"todayDungeonActivity":75,"activityForRuneAvailable":False,"adventureStat":2,"clanWarStat":2},"serverResetTime":1745546400,"clanWarEndSeasonTime":1745670600,"freeClanChangeInterval":{"start":1745668800,"end":1745841600},"giftUids":[]}}}


def clanActivityRewards(request):
    return {"ident":"clanGetActivityRewardTable","result":{"response":{"12500":{"activityPoints":12500,"reward":{"consumable":{"4":"4"}},"clanGifts":1,"useClanRewardChangeDayRule":0}}}}


def clanPrevData(request):
    return {"ident":"clanGetPrevData","result":{"response":None}}


def heroesMerchant(request):
    return {"ident":"heroesMerchantGet","result":{"response":None}}


def freebie(request):
    return {"ident":"freebieHaveGroup","result":{"response":True}}


def pirateTreasure(request):
    return {"ident":"pirateTreasureIsAvailable","result":{"response":False}}


def expeditions(request):
    return {"ident":"expeditionGet","result":{"response":[{"id":0,"slotId":1,"status":3,"heroes":[],"endTime":0,"duration":900,"day":"20250424","reward":{"consumable":{"44":1,"42":3,"41":2}},"power":50200,"rarity":4,"storyId":6,"attemptsLeft":0}]}}


def hallOfFame(request):
    return {"ident":"hallOfFameGetTrophies","result":{"response":[]}}


def titanArena(request):
    return {"ident":"titanArenaCheckForgotten","result":{"response":{"result":False}}}


def titanArenaChest(request):
    return {"ident":"titanArenaGetChestReward","result":{"response":[]}}


def bosses(request):
    result = {"ident":"bossGetAll","result":{"response":[]}}
    for i in range(10, 13):
        result['result']['response'].append({
            "id": i,
            "bossLevel": 1,
            "chestNum": 1,
            "chestId": 0,
            "lastChestReward": [],
            "chests": [],
            "cost": [],
            "mayRaid": True
            })
    return result


def shops(request):
    return {"ident":"shopGetAll","result":{"response":{"1":{"id":1,"slots":{"1":{"id":1,"reward":{"consumable":{"11":"45"}},"bought":0,"cost":{"gold":450000}}},"availableUntil":0,"refreshTime":1745564400}}}}


def adventuresPassed(request):
    return {"ident":"adventure_getPassed","result":{"response":{"101":1,"1":12,"2":1,"3":5}}}


def adventuresActive(request):
    return {"ident":"adventure_getActiveData","result":{"response":{"hasActive":False,"lastChatTime":None,"hasRewards":False}}}


def adventuresFind(request):
    return {"ident":"adventure_find","result":{"response":{"lobbies":[],"users":[]}}}


def adventuresSolo(request):
    return {"ident":"adventureSolo_getActiveData","result":{"response":{"hasActive":False,"adventureId":None,"endTime":None,"turns":None,"hasRewards":None}}}


def petChest(request):
    return {"ident":"pet_getChest","result":{"response":{"starmoneySpent":2000,"dailyPetId":"6006"}}}


def playable(request):
    return {"ident":"playable_getAvailable","result":{"response":[48,49,50]}}


def seasonAdventure(request):
    return {"ident":"seasonAdventure_getInfo","result":{"response":{"id":8,"seasonAdventure":{"id":8,"startDate":1744941600,"endDate":1746064800,"closed":False}}}}


def clanDomination(request):
    return {"ident":"clanDomination_getInfo","result":{"response":None}}


def clanRaidRating(request):
    return {"ident":"clanRaid_ratingInfo","result":{"response":[]}}


def clanRaid(request):
    return {"ident":"clanRaid_getInfo","result":{"response":None}}


def coopBundle(request):
    return {"ident":"coopBundle_getInfo","result":{"response":[]}}


def buffs(request):
    return {"ident":"buffs_getInfo","result":{"response":[]}}


def brawl(request):
    return {"ident":"brawl_getInfo","result":{"response":None}}


def brawlQuests(request):
    return {"ident":"brawl_questGetInfo","result":{"response":None}}


def epicBrawl(request):
    return {"ident":"epicBrawl_getBriefInfo","result":{"response":None}}


def epicBrawlStreak(request):
    return {"ident":"epicBrawl_getWinStreak","result":{"response":None}}


def stronghold(request):
    return {"ident":"stronghold_getInfo","result":{"response":{"regions":{"1":{"status":"active","activeMission":1},"2":{"status":"locked","activeMission":-1},"3":{"status":"locked","activeMission":-1},"4":{"status":"locked","activeMission":-1},"5":{"status":"locked","activeMission":-1}}}}}


def mechanicsBan(request):
    return {"ident":"mechanicsBan_getInfo","result":{"response":[]}}


def gacha(request):
    return {"ident":"gacha_getInfo","result":{"response":{"nextRefill":1745550000,"wishlist":[40,40,40],"onceRolled":{"super":[4002,4005]},"openings":{"count":31,"last":25,"next":35,"reward":{"consumable":{"11":"30"},"gold":350000}},"guaranteedOfferCount":[]}}}


def heroRating(request):
    return {"ident":"heroRating_getInfo","result":{"response":{"userRating":[],"rating":{"1":4.827589077996817,"2":4.79506316007455,"3":4.710327455919395,"4":4.786494934782253,"5":4.480123743232792,"6":4.66074530680863,"7":4.7484863787375415,"8":4.5022778192681105,"9":4.794512471655328,"10":4.598105813193991,"11":4.472053372868792,"12":4.778655650228075,"13":4.830326821252511,"14":4.348677056904675,"15":4.593706179683679,"16":4.880622813636052,"17":4.71444645368696,"18":4.5843417611159545,"19":4.452919020715631,"20":4.553611977542109,"21":4.516604378003203,"22":4.454574049803408,"23":4.678326752747839,"24":4.719842190763519,"25":4.741841937539834,"26":4.4697183098591555,"27":4.531221198156683,"28":4.677473627987715,"29":4.720522310475319,"30":4.609442313366775,"31":4.660379450535912,"32":4.694522354901416,"33":4.678319642300094,"34":4.646717052432687,"35":4.68855811749842,"36":4.675132914451425,"37":4.776520698394819,"38":4.529679272379129,"39":4.480375782881002,"40":4.8040503956684715,"41":4.75010256773007,"42":4.791933562014804,"43":4.8218412199661875,"44":4.618315467075038,"45":4.6025180819716045,"46":4.8732917719433155,"47":4.631421754882036,"48":4.8456363459858265,"49":4.848857644991212,"50":4.771879621889267,"51":4.717578393224994,"52":4.805082628550365,"53":4.471843817787419,"54":4.508896070760334,"55":4.868098857584998,"56":4.788419432090318,"57":4.711688311688312,"58":4.708006579296439,"59":4.765730063342537,"60":4.7278191873046405,"61":4.690721649484536,"62":4.722096015618067,"63":4.661246075028921,"64":4.759112434041402,"65":4.631867076000094,"66":4.62811251152782}}}}


def offerwall(request):
    return {"ident":"offerwall_getActive","result":{"response":None}}


def banners(request):
    return {"ident":"banner_getAll","result":{"response":[]}}


def idle(request):
    return {"ident":"idle_getAll","result":{"response":[]}}


def workshopBuff(request):
	return {"ident":"workshopBuff_getInfo","result":{"response":None}}


def videos(request):
	return {"ident":"rewardedVideo_boxyGetInfo","result":{"response":None}}


def newHeroes(request):
	{"ident":"newHeroNotification_get","result":{"response":None}}


def powerTournament(request):
    return {"ident":"powerTournament_getState","result":{"response":{"id":4,"startTime":1745287200,"endTime":1745719199,"state":1,"type":"heroes","currentDayRewards":[{"id":9,"points":300,"reward":{"gold":600000},"isFarmed":1},{"id":10,"points":1000,"reward":{"consumable":{"11":50}},"isFarmed":0},{"id":11,"points":2200,"reward":{"consumable":{"339":2}},"isFarmed":1},{"id":12,"points":4000,"reward":{"consumable":{"51":40}},"isFarmed":1}],"currentDailyPoints":17196,"currentTournamentPoints":47688,"statueLevel":2,"finalRewardFarmed":0}}}


def mechanics(request):
	return {"ident":"mechanicAvailability","result":{"response":{"titan_arena":True,"titan_arena_def":True,"titan_artifact":True,"titan_artifact_chest":True,"titan_valley":True,"titan_spirits":True,"titan_artifact_merchant":True,"titan_arena_hall_of_fame":True}}}


def tower(request):
	return {"ident":"towerGetInfo","result":{"response":{"userId":"278407558","teamLevel":"65","points":"62370","maySkipFloor":"26","floorNumber":"50","floorType":"chest","states":{"heroes":{"2":{"hp":17000,"energy":"1000","isDead":False,"maxHp":17000},"20":{"hp":5340,"energy":"1000","isDead":False,"maxHp":5340},"7":{"hp":22209,"energy":845,"isDead":False,"maxHp":23352},"36":{"hp":7100,"energy":"1000","isDead":False,"maxHp":7100},"6":{"hp":5820,"energy":"1000","isDead":False,"maxHp":5820},"31":{"hp":23266,"energy":1000,"isDead":False,"maxHp":34167},"1":{"hp":18444,"energy":471,"isDead":False,"maxHp":38517},"10":{"hp":9090,"energy":"1000","isDead":False,"maxHp":9090},"3":{"hp":35805,"energy":400,"isDead":False,"maxHp":35805},"13":{"hp":23100,"energy":100,"isDead":False,"maxHp":23100},"40":{"hp":16970,"energy":848,"isDead":False,"maxHp":16970},"6006":{"hp":-1,"energy":526,"isDead":False,"maxHp":None}},"mercenaries":[]},"effects":{"percentBuff_allAttacks":11,"percentBuff_magicResist":40,"percentBuff_armor":30},"floor":{"chests":[{"num":0,"opened":0},{"num":1,"opened":1,"reward":{"gold":90000},"critMultiplier":1},{"num":2,"opened":0}],"chestRewards":{"gold":{"gold":90000},"item":{"fragmentGear":{"94":"6"}},"coin":{"coin":{"3":"250"}}}},"reward":{"4":{"gold":45000},"8":{"gold":45000},"10":{"gold":45000},"14":{"gold":45000},"16":{"coin":{"3":"75"}},"20":{"fragmentGear":{"94":"4"}},"22":{"fragmentGear":{"98":"3"}},"26":{"gold":90000},"28":{"gold":90000},"32":{"coin":{"3":"150"}},"35":{"fragmentGear":{"96":"6"}},"39":{"gold":90000},"42":{"coin":{"3":300}},"46":{"gold":90000},"50":{"gold":90000}},"mayBuySkip":True,"mayFullSkip":False,"skipBought":False,"chestSkip":False,"fullSkipCost":{"starmoney":1150},"pointRewards":{"200":True,"3000":True,"10000":True,"15000":True,"20000":True,"25000":True,"35000":True,"45000":True,"60000":True}}}}


def battlePass(request):
    return {"ident":"battlePass_getInfo","result":{"response":None}}


def specialBattlePass(request):
	{"ident":"battlePass_getSpecial","result":{"response":None}}
