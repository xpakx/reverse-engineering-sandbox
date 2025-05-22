from controllers.user import register, getInfo
from controllers.campaign import startMission, endMission, raidMission
from controllers.campaign import getMissions, getMissionReplace
from controllers.heroes import getUserHeroes, upgradeSkill, evolveHero
from controllers.heroes import addExpToHero, getHeroRatings
from controllers.items import buyStamina, useStaminaItem, inventory
from controllers.gacha import summonHero
from extractors.lib import GameData
from typing import NamedTuple, Any
from controllers.calendar import getTime, getDailyBonus, farmDaily
from controllers.quest import farmQuest, getQuests, getQuestEvents
from controllers.season import getSeason
from controllers.shop import getShops, buy
from controllers.tower import getTower
from controllers.tournament import powerTournament
from controllers.offer import getOffers
from controllers.adventure import adventuresFind, adventuresSolo
from controllers.adventure import adventuresPassed, adventuresActive
from controllers.clan import clanDomination, clanRaidRating, clanRaid
from controllers.clan import clanPrestige, clanWarInfo, clanWarWarlord
from controllers.clan import crossClanWarInfo, crossClanSettings
from controllers.clan import clanActivityRewards, clanPrevData, clan
from controllers.battlepass import getBattlePass, getSpecialBattlePass
from controllers.titan import getTitans, getTitanSpirits, getTitanArena
from controllers.titan import getTitanArenaChest, getTitanSummoningCircle
from controllers.titan import getTitanArtifactChest
from controllers.pet import getPets, getPetChest, getPetPotions
from controllers.outland import getBosses
from repo.userdata import GameRepository


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
        self.registerBodyProcessor('shopBuy', buy)
        self.registerProcessor('clanDomination_getInfo', clanDomination)
        self.registerProcessor('clanRaid_ratingInfo', clanRaidRating)
        self.registerProcessor('clanRaid_getInfo', clanRaid)
        self.registerProcessor('clan_prestigeGetInfo', clanPrestige)

        self.registerProcessor('clanWarGetBriefInfo', clanWarInfo)
        self.registerProcessor('crossClanWar_getBriefInfo', crossClanWarInfo)
        self.registerProcessor('crossClanWar_getSettings', crossClanSettings)
        self.registerProcessor('clanWarGetWarlordInfo', clanWarWarlord)
        self.registerProcessor('clanGetInfo', clan)
        self.registerProcessor(
                'clanGetActivityRewardTable', clanActivityRewards
                )
        self.registerProcessor('clanGetPrevData', clanPrevData)
        self.registerProcessor('battlePass_getInfo', getBattlePass)
        self.registerProcessor('battlePass_getSpecial', getSpecialBattlePass)

        self.registerProcessor('titanGetAll', getTitans)
        self.registerProcessor('titanSpiritGetAll', getTitanSpirits)
        self.registerProcessor('titanArenaCheckForgotten', getTitanArena)
        self.registerProcessor('titanArenaGetChestReward', getTitanArenaChest)
        self.registerProcessor('titanArtifactGetChest', getTitanArtifactChest)
        self.registerProcessor(
                'titanGetSummoningCircle', getTitanSummoningCircle
                )

        self.registerProcessor('pet_getAll', getPets)
        self.registerProcessor('pet_getPotionDailyBuyCount', getPetPotions)
        self.registerProcessor('pet_getChest', getPetChest)
        self.registerProcessor('bossGetAll', getBosses)

        self.registerProcessor('missionGetAll', getMissions)
        self.registerProcessor('missionGetReplace', getMissionReplace)

        # TODO: extract

        self.registerProcessor('userMergeGetStatus', register)
        self.registerProcessor('friendsGetInfo', friends)
        self.registerProcessor('billingGetAll', billing)
        self.registerProcessor('subscriptionGetInfo', subscription)

        self.registerProcessor('userGetAvailableAvatars', avatars)
        self.registerProcessor('userGetAvailableAvatarFrames', avatarFrames)
        self.registerProcessor('userGetAvailableStickers', stickers)

        self.registerProcessor('teamGetAll', team)
        self.registerProcessor('teamGetFavor', teamFavor)
        self.registerProcessor('team_getBanners', teamBanners)

        self.registerProcessor('chatsGetAll', chats)
        self.registerProcessor('chatGetTalks', chatTalks)
        self.registerProcessor('chatGetInfo', chatInfo)

        self.registerProcessor('mailGetAll', mail)

        self.registerProcessor('arenaGetAll', arena)
        self.registerProcessor('socialQuestGetInfo', socialQuest)
        self.registerProcessor('telegramQuestGetInfo', telegramQuest)
        self.registerProcessor('settingsGetAll', settings)
        self.registerProcessor('zeppelinGiftGet', zeppelinGift)
        self.registerProcessor('tutorialGetInfo', tutorial)
        self.registerProcessor('splitGetAll', splits)
        self.registerProcessor('billingGetLast', billing)
        self.registerProcessor('artifactGetChestLevel', artifactChest)
        self.registerProcessor('newYearGetInfo', newYearInfo)
        self.registerProcessor('campaignStoryGetList', campaignStoryList)
        self.registerProcessor('roleAscension_getAll', roleAscension)
        self.registerProcessor('heroesMerchantGet', heroesMerchant)
        self.registerProcessor('freebieHaveGroup', freebie)
        self.registerProcessor('pirateTreasureIsAvailable', pirateTreasure)
        self.registerProcessor('expeditionGet', expeditions)
        self.registerProcessor('hallOfFameGetTrophies', hallOfFame)
        self.registerProcessor('playable_getAvailable', playable)
        self.registerProcessor('coopBundle_getInfo', coopBundle)
        self.registerProcessor('buffs_getInfo', buffs)
        self.registerProcessor('brawl_getInfo', brawl)
        self.registerProcessor('brawl_questGetInfo', brawlQuests)
        self.registerProcessor('epicBrawl_getBriefInfo', epicBrawl)
        self.registerProcessor('epicBrawl_getWinStreak', epicBrawlStreak)
        self.registerProcessor('stronghold_getInfo', stronghold)
        self.registerProcessor('mechanicsBan_getInfo', mechanicsBan)
        self.registerProcessor('gacha_getInfo', gacha)
        self.registerProcessor('offerwall_getActive', offerwall)
        self.registerProcessor('banner_getAll', banners)
        self.registerProcessor('idle_getAll', idle)
        self.registerProcessor('workshopBuff_getInfo', workshopBuff)
        self.registerProcessor('rewardedVideo_boxyGetInfo', videos)
        self.registerProcessor('newHeroNotification_get', newHeroes)
        self.registerProcessor('mechanicAvailability', mechanics)

    def registerProcessor(self, name, processor, ident=None):
        id = ident if ident else name
        self.processors[name] = Processor(process=processor, ident=id)

    def registerBodyProcessor(self, name, processor):
        self.registerProcessor(name, processor, 'body')

    def callProcessor(self, processor, request, repo: GameRepository, gameData: GameData):
        response = {}
        response['ident'] = processor.ident
        if request['ident'] != 'body':
            response['ident'] = request['ident']
        response['result'] = {
                "response": processor.process(request, repo, gameData)
                }
        return response

    def process(self, request, repo: GameRepository, gameData: GameData):
        call = request['name']
        print(f'Call: {call}')
        if call in self.processors:
            return self.callProcessor(
                    self.processors[call],
                    request,
                    repo,
                    gameData
                )

        print(f'WARNING: Unknown command {call}')
        return None


def friends(request, temp, gameData: GameData):
    return {
                "accounts": [],
                "users": []
            }


def billing(request, temp, gameData: GameData):
    return {"billings": [], "bundle": []}


def team(request, temp, gameData: GameData):
    return {
            "mission": [],
            "arena": [],
            "tower": [],
            "boss_11": [],
            "boss_12": [],
            "boss_10": [],
            "dungeon_water": [],
            "dungeon_hero": [],
            "dungeon_neutral": [],
            "dungeon_fire": [],
            "brawl_titan": [],
            "clanDefence_heroes": [],
            "clanDefence_titans": [],
            "adventure_hero": [],
            "dungeon_earth": [],
            "clan_pvp_hero": [],
            "clan_pvp_titan": [],
            "crossClanDefence_heroes": [[], [], []],
            "crossClanDefence_titans": [[], []],
            "titan_arena_def": [],
            "titan_arena": [],
            "clan_global_pvp_titan": [],
            "clan_global_pvp": [],
            "clanRaid_nodes": [[], []],
            "grand": [[], [], []]
        }


def teamFavor(request, temp, gameData: GameData):
    return {
            "__legacy": [],
            "mission": [],
            "arena_def": [],
            "arena": [],
            "tower": [],
            "boss_11": [],
            "boss_12": [],
            "boss_10": [],
            "dungeon_water": None,
            "dungeon_hero": [],
            "dungeon_neutral": None,
            "dungeon_fire": None,
            "brawl_titan": [],
            "clanDefence_heroes": [],
            "clanDefence_titans": [],
            "adventure_hero": [],
            "dungeon_earth": None,
            "clan_pvp_hero": [],
            "clan_pvp_titan": None,
            "crossClanDefence_heroes": [],
            "crossClanDefence_titans": [],
            "grand_def": [],
            "titan_arena_def": None,
            "titan_arena": None,
            "clan_global_pvp_titan": None,
            "clan_global_pvp": [],
            "clanRaid_nodes": [],
            "grand": []
        }


def teamBanners(request, temp, gameData: GameData):
    return {
            "mission": None,
            "arena_def": None,
            "arena": None,
            "tower": None,
            "boss_11": None,
            "boss_12": None,
            "boss_10": None,
            "dungeon_water": None,
            "dungeon_hero": None,
            "dungeon_neutral": None,
            "dungeon_fire": None,
            "clanDefence_heroes": None,
            "clanDefence_titans": None,
            "adventure_hero": None,
            "dungeon_earth": None,
            "clan_pvp_hero": None,
            "clan_pvp_titan": None,
            "crossClanDefence_heroes": [None, None, None],
            "crossClanDefence_titans": [None, None, None],
            "grand_def": [None, None, None],
            "titan_arena": None,
            "clan_global_pvp_titan": None,
            "clan_global_pvp": None,
            "grand": [None, None, None]
        }


def mail(request, temp, gameData: GameData):
    return {
            "letters": [],
            "users": []
        }


def arena(request, temp, gameData: GameData):
    return {
            "userId": "1",
            "arenaPlace": "257",
            "arenaHeroes": [],
            "grandPlace": "579",
            "grandHeroes": [[], [], []],
            "grandCoin": 31.265900000000002,
            "grandCoinTime": 1745545329,
            "arenaPower": "84873",
            "grandPower": "122338",
            "rewardFlag": "0",
            "battles": 45,
            "wins": 33,
            "rewardTime": 1745604000
        }


def socialQuest(request, temp, gameData: GameData):
    return {"farmed": True}


def telegramQuest(request, temp, gameData: GameData):
    return {
            "twitter": "1",
            "youtube": "1",
            "push": True,
            "discord": True,
            "favorites": "1",
            "emailConfirmed": True,
            "post": "",
            "group": "",
            "notifications": True
        }


def avatars(request, temp, gameData: GameData):
    return [1325, 92, 93]


def avatarFrames(request, temp, gameData: GameData):
    return {
            "frames": [],
            "progress": {
                "41": {
                    "frameId": 41,
                    "current": 0,
                    "max": 1
                }
            }
        }


def stickers(request, temp, gameData: GameData):
    return [2]


def settings(request, temp, gameData: GameData):
    return {
            "cookie": "nocookie",
            "currency": "PLN",
            "sounds": False,
            "music": False,
            "theme": True,
            "heroesBrowsedStatusMask": "qgNJACgAAAo",
            "autoBattleToggle": True,
            "inventoryLootBoxBrowsedCount": 23,
            "pveSpeedUpToggleIndex": 1,
            "enableUltCinematic": False,
            "showHeroGachaWishlistTutorial": False,
            "playThemeMusicByHero": "AAA",
            "titansBrowsedStatusMask": "AwBQwAMH",
            "towerSpeedUpToggleIndex": 0,
            "petsBrowsedStatusMask": "xQI",
            "titanDungeonSpeedUpToggleIndex": 1,
            "adventureChatBrowsingTime": 1745284165,
            "lastBrowsedShopByGoldClanRaidStartTime": 1745200800,
            "lastBrowsedShopByCoinsClanRaidStartTime": 1745200800
        }


def subscription(request, temp, gameData: GameData):
    return {
            "subscription": None,
            "dailyReward": {
                "availableFarm": False,
                "dailyReward": {"coin": {"14": "400"}},
                "notFarmedDays": 0,
                "currentReward": None
                }
        }


def zeppelinGift(request, temp, gameData: GameData):
    return {
            "available": False,
            "reward": {"consumable": {"45": 1}}
        }


def tutorial(request, temp, gameData: GameData):
    return {
            "chains": {
                "1": 9999,
                "3": 9999,
                "18": 9999,
                "25": 1,
                "2": 9999,
                "4": 9999,
                "5": 9999,
                "6": 9999,
                "7": 9999,
                "8": 9999,
                "9": 9999,
                "10": 0,
                "11": 9999,
                "13": 9999,
                "14": 9999,
                "15": 0,
                "16": 0,
                "17": 9999,
                "26": 0,
                "29": 0,
                "27": 9999,
                "28": 9999,
                "31": 0,
                "33": 0
            },
            "params": {
                "heroIcon1": "hero2",
                "heroIcon2": "hero20",
                "heroName1": "LIB_HERO_NAME_2",
                "heroName2": "LIB_HERO_NAME_20",
                "tutorialBattleEndTime": "5.46"
            }
        }


def splits(request, temp, gameData: GameData):
    return [
            {
                "rule": {
                    "stash": {
                        "flushIntervalStart": 1000,
                        "flushIntervalDefault": 5000
                    }
                }
            },
            None
        ]


def lastBilling(request, temp, gameData: GameData):
    return None


def artifactChest(request, temp, gameData: GameData):
    return {
            "level": 3,
            "xp": 60,
            "starmoneySpent": 800
        }


def newYearInfo(request, temp, gameData: GameData):
    return {
            "treeLevel": 0,
            "treeExpPercent": 0,
            "giftsToOpen": 0,
            "eventHero": 64,
            "dayHero": 51
        }


def campaignStoryList(request, temp, gameData: GameData):
    return []


def roleAscension(request, temp, gameData: GameData):
    return {
            "3": {"id": 3, "level": 14}
        }


def chats(request, temp, gameData: GameData):
    return {
        "clan": {
            "chat": [],
            "users": {},
            "clans": []
        },
        "xgvg": {
            "chat": [],
            "users": {},
            "clans": []
        }
    }


def chatTalks(request, temp, gameData: GameData):
    return {
            "talks": [],
            "users": {}
        }


def chatInfo(request, temp, gameData: GameData):
    return {
            "banUntil": "0",
            "subscribeServer": "0",
            "lastMessageTime": "1745049961",
            "blackList": [],
            "settings": {
                "chatSelectedTab": "CLAN_TAB",
                "lastReadMessageId": 90058375,
                "lastReadClanNewsHash": "f7086b389381c5b3f5d3cb07a4671ee7",
                "lastReadTrainingMessageId": 89994080,
                "lastReadXGVGMessageId": 90050415
                }
            }


def heroesMerchant(request, temp, gameData: GameData):
    return None


def freebie(request, temp, gameData: GameData):
    return True


def pirateTreasure(request, temp, gameData: GameData):
    return False


def expeditions(request, temp, gameData: GameData):
    return [
            {
                "id": 0,
                "slotId": 1,
                "status": 3,
                "heroes": [],
                "endTime": 0,
                "duration": 900,
                "day": "20250424",
                "reward": {
                    "consumable": {
                        "44": 1,
                        "42": 3,
                        "41": 2
                    }
                },
                "power": 50200,
                "rarity": 4,
                "storyId": 6,
                "attemptsLeft": 0
            }
        ]


def hallOfFame(request, temp, gameData: GameData):
    return []


def playable(request, temp, gameData: GameData):
    return [25, 48, 49, 50]


def coopBundle(request, temp, gameData: GameData):
    return []


def buffs(request, temp, gameData: GameData):
    return []


def brawl(request, temp, gameData: GameData):
    return None


def brawlQuests(request, temp, gameData: GameData):
    return None


def epicBrawl(request, temp, gameData: GameData):
    return None


def epicBrawlStreak(request, temp, gameData: GameData):
    return None


def stronghold(request, temp, gameData: GameData):
    return {"regions":
            {
                "1": {
                    "status": "active",
                    "activeMission": 1
                    },
                "2": {
                    "status": "locked",
                    "activeMission": -1
                    },
                "3": {
                    "status": "locked",
                    "activeMission": -1
                    },
                "4": {
                    "status": "locked",
                    "activeMission": -1
                    },
                "5": {
                    "status": "locked",
                    "activeMission": -1
                    }
                }
            }


def mechanicsBan(request, temp, gameData: GameData):
    return []


def gacha(request, temp, gameData: GameData):
    return {
            "nextRefill": 1745550000,
            "wishlist": [40, 40, 40],
            "onceRolled": {
                "super": [4002, 4005]
            },
            "openings": {
                "count": 31,
                "last": 25,
                "next": 35,
                "reward": {
                    "consumable": {"11": "30"},
                    "gold": 350000
                }
            },
            "guaranteedOfferCount": []
        }


def offerwall(request, temp, gameData: GameData):
    return None


def banners(request, temp, gameData: GameData):
    return []


def idle(request, temp, gameData: GameData):
    return []


def workshopBuff(request, temp, gameData: GameData):
    return None


def videos(request, temp, gameData: GameData):
    return None


def newHeroes(request, temp, gameData: GameData):
    return None


def mechanics(request, temp, gameData: GameData):
    return {
            "titan_arena": True,
            "titan_arena_def": True,
            "titan_artifact": True,
            "titan_artifact_chest": True,
            "titan_valley": True,
            "titan_spirits": True,
            "titan_artifact_merchant": True,
            "titan_arena_hall_of_fame": True
        }
