from extractors.lib import GameData


def clanDomination(request, temp, gameData: GameData):
    return None


def clanRaidRating(request, temp, gameData: GameData):
    return []


def clanRaid(request, temp, gameData: GameData):
    return None


def clanPrestige(request, temp, gameData: GameData):
    return {
            "prestigeId": 2,
            "prestigeCount": 379400,
            "userPrestigeCount": 22665,
            "farmedPrestigeLevels": [1],
            "endTime": 1746496800,
            "prestigeStartPopupViewed": True,
            "nextTime": 1746583200
            }


def clanWarInfo(request, temp, gameData: GameData):
    return {
            "tries": 0,
            "targets": 0,
            "arePointsMax": True,
            "nextWarTime": 1745571600,
            "hasActiveWar": False,
            "nearestWarEndTime": 175611200
            }


def crossClanWarInfo(request, temp, gameData: GameData):
    return {
            "status": "active",
            "hasActiveWar": True,
            "hasEnoughDefendedSlots": True,
            "seasonEndTime": 1751767200,
            "nextSeasonStartTime": 1752458400,
            "nextWarTime": 1745810100,
            "heroTries": 3,
            "titanTries": 2,
            "heroTargets": 0,
            "titanTargets": 0,
            "currentWarEndTime": 1745719200
            }


def crossClanSettings(request, temp, gameData: GameData):
    return {
            "fillDefenceByCommander": False
            }


def clanWarWarlord(request, temp, gameData: GameData):
    return None


def clanActivityRewards(request, temp, gameData: GameData):
    return {
            "12500": {
                  "activityPoints": 12500,
                  "reward": {
                      "consumable": {"4": "4"}
                      },
                  "clanGifts": 1,
                  "useClanRewardChangeDayRule": 0
                  }
            }


def clanPrevData(request, temp, gameData: GameData):
    return None


def clan(request, temp, gameData: GameData):
    return {
            "clan": {
                "id": "1",
                "ownerId": "2",
                "level": "1",
                "title": "SuperClan",
                "description": "",
                "icon": {
                    "flagColor1": 4,
                    "flagColor2": 5,
                    "flagShape": 3,
                    "iconColor": 1,
                    "iconShape": 3
                    },
                "country": "7",
                "minLevel": "30",
                "serverId": "457",
                "membersCount": "20",
                "disbanding": False,
                "topActivity": "187676",
                "topDungeon": "19052",
                "roleNames": [],
                "frameId": 2,
                "members": {},
                "news": "",
                "activityPoints": 22163,
                "dungeonPoints": 1988,
                "blackList": [],
                "warriors": [],
                "giftsCount": 0,
                "daysToKick": "14",
                "league": "2"
                },
            "membersStat": [],
            "stat": {
                "todayActivity": 2494,
                "activitySum": 22153,
                "dungeonActivitySum": 1255,
                "todayRaid": [],
                "todayItemsActivity": 0,
                "todayDungeonActivity": 75,
                "activityForRuneAvailable": False,
                "adventureStat": 2,
                "clanWarStat": 2
                },
            "serverResetTime": 1745546400,
            "clanWarEndSeasonTime": 1745670600,
            "freeClanChangeInterval": {
                "start": 1745668800,
                "end": 1745841600
                },
            "giftUids": []
            }
