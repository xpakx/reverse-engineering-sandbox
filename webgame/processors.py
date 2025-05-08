from controllers.user import register, getInfo
from controllers.campaign import startMission, endMission, raidMission
from controllers.heroes import getUserHeroes, upgradeSkill, evolveHero
from controllers.heroes import addExpToHero, getHeroRatings
from controllers.items import buyStamina, useStaminaItem, inventory
from controllers.gacha import summonHero
from extractors.lib import GameData
from typing import NamedTuple, Any
from controllers.calendar import getTime, getDailyBonus, farmDaily
from controllers.quest import farmQuest, getQuests, getQuestEvents
from controllers.season import getSeason
from controllers.shop import getShops
from controllers.tower import getTower
from controllers.tournament import powerTournament
from controllers.offer import getOffers
from controllers.adventure import adventuresFind, adventuresSolo
from controllers.adventure import adventuresPassed, adventuresActive


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
        self.registerProcessor('inventoryGet', inventory)
        self.registerProcessor('getTime', getTime)
        self.registerProcessor('dailyBonusGetInfo', getDailyBonus)
        self.registerBodyProcessor('refillableBuyStamina', buyStamina)
        self.registerBodyProcessor('consumableUseStamina', useStaminaItem)
        self.registerBodyProcessor('gacha_open', summonHero)
        self.registerBodyProcessor('questFarm', farmQuest)
        self.registerBodyProcessor('dailyBonusFarm', farmDaily)
        self.registerProcessor('questGetAll', getQuests)
        self.registerProcessor('questGetEvents', getQuestEvents)
        self.registerBodyProcessor('heroUpgradeSkill', upgradeSkill)
        self.registerProcessor('seasonAdventure_getInfo', getSeason)
        self.registerProcessor('shopGetAll', getShops)
        self.registerProcessor('towerGetInfo', getTower)
        self.registerBodyProcessor('heroEvolve', evolveHero)
        self.registerBodyProcessor('consumableUseHeroXp', addExpToHero)
        self.registerProcessor('powerTournament_getState', powerTournament)
        self.registerProcessor('specialOffer_getAll', getOffers)
        self.registerProcessor('heroRating_getInfo', getHeroRatings)
        self.registerProcessor('adventure_getPassed', adventuresPassed)
        self.registerProcessor('adventure_getActiveData', adventuresActive)
        self.registerProcessor('adventure_find', adventuresFind)
        self.registerProcessor('adventureSolo_getActiveData', adventuresSolo)

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
        if (call == 'teamGetAll'):
            return team(request)
        if (call == 'teamGetFavor'):
            return teamFavor(request)
        if (call == 'team_getBanners'):
            return teamBanners(request)
        if (call == 'clan_prestigeGetInfo'):
            return clanPrestige(request)
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
        if (call == "pet_getChest"):
            return petChest(request)
        if (call == "playable_getAvailable"):
            return playable(request)
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
        if (call == "mechanicAvailability"):
            return mechanics(request)
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
    for i in range(1, 2):
        result['result']['response'].append(
                {"id":i,"stars":3,"triesSpent":0,"resetToday":0,"attempts":22,"wins":22}
            )
    return result


def missionReplace(request):
    return {"ident":"missionGetReplace","result":{"response":None}}


def team(request):
    return {"ident":"teamGetAll","result":{"response":{"mission":[],"arena":[],"tower":[],"boss_11":[],"boss_12":[],"boss_10":[],"dungeon_water":[],"dungeon_hero":[],"dungeon_neutral":[],"dungeon_fire":[],"brawl_titan":[],"clanDefence_heroes":[],"clanDefence_titans":[],"adventure_hero":[],"dungeon_earth":[],"clan_pvp_hero":[],"clan_pvp_titan":[],"crossClanDefence_heroes":[[],[],[]],"crossClanDefence_titans":[[],[]],"titan_arena_def":[],"titan_arena":[],"clan_global_pvp_titan":[],"clan_global_pvp":[],"clanRaid_nodes":[[],[]],"grand":[[],[],[]]}}}


def teamFavor(request):
    return {"ident":"teamGetFavor","result":{"response":{"__legacy":[],"mission":[],"arena_def":[],"arena":[],"tower":[],"boss_11":[],"boss_12":[],"boss_10":[],"dungeon_water":None,"dungeon_hero":[],"dungeon_neutral":None,"dungeon_fire":None,"brawl_titan":[],"clanDefence_heroes":[],"clanDefence_titans":[],"adventure_hero":[],"dungeon_earth":None,"clan_pvp_hero":[],"clan_pvp_titan":None,"crossClanDefence_heroes":[],"crossClanDefence_titans":[],"grand_def":[],"titan_arena_def":None,"titan_arena":None,"clan_global_pvp_titan":None,"clan_global_pvp":[],"clanRaid_nodes":[],"grand":[]}}}


def teamBanners(request):
    return {"ident":"team_getBanners","result":{"response":{"mission":None,"arena_def":None,"arena":None,"tower":None,"boss_11":None,"boss_12":None,"boss_10":None,"dungeon_water":None,"dungeon_hero":None,"dungeon_neutral":None,"dungeon_fire":None,"clanDefence_heroes":None,"clanDefence_titans":None,"adventure_hero":None,"dungeon_earth":None,"clan_pvp_hero":None,"clan_pvp_titan":None,"crossClanDefence_heroes":[None,None,None],"crossClanDefence_titans":[None,None,None],"grand_def":[None,None,None],"titan_arena":None,"clan_global_pvp_titan":None,"clan_global_pvp":None,"grand":[None,None,None]}}}


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


def petChest(request):
    return {"ident":"pet_getChest","result":{"response":{"starmoneySpent":2000,"dailyPetId":"6006"}}}


def playable(request):
    return {"ident":"playable_getAvailable","result":{"response":[25,48,49,50]}}


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


def mechanics(request):
	return {"ident":"mechanicAvailability","result":{"response":{"titan_arena":True,"titan_arena_def":True,"titan_artifact":True,"titan_artifact_chest":True,"titan_valley":True,"titan_spirits":True,"titan_artifact_merchant":True,"titan_arena_hall_of_fame":True}}}


def battlePass(request):
    return {"ident":"battlePass_getInfo","result":{"response":None}}


def specialBattlePass(request):
	{"ident":"battlePass_getSpecial","result":{"response":None}}
