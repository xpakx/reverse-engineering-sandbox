from datetime import time, datetime

tournamentOpen = False


def isTournamentActive():
    return tournamentOpen


def powerTournament(request, temp, gameData):
    if not isTournamentActive():
        return {}

    response = {}
    response['id'] = 4

    startDate = datetime(2025, 4, 1)
    startTime = datetime.combine(startDate, time.min)
    response['startTime'] = int(startTime.timestamp())
    endDate = datetime(2025, 5, 30)
    endTime = datetime.combine(endDate, time.min)
    response['endTime'] = int(endTime.timestamp())

    response['state'] = 1
    response['type'] = 'heroes'

    response['currentDailyPoints'] = 0
    response['currentTournamentPoints'] = 0
    response['statueLevel'] = 1,
    response['finalRewardFarmed'] = 0

    return response


def getRewards():
    response = []

    response.append({
      "id": 5,
      "points": 300,
      "reward": {
        "gold": 600000
      },
      "isFarmed": 0
    })

    response.append({
      "id": 6,
      "points": 1000,
      "reward": {
        "consumable": {
          "11": 50
        }
      },
      "isFarmed": 0
    })

    response.append({
      "id": 7,
      "points": 2200,
      "reward": {
        "consumable": {
          "339": 2
        }
      },
      "isFarmed": 1
    })
    response.append({
      "id": 8,
      "points": 4000,
      "reward": {
        "consumable": {
          "51": 40
        }
      },
      "isFarmed": 1
    })
    return response


def getTournamentOffer():
    if not isTournamentActive():
        return None

    response = {}
    response['id'] = 1679
    response['localeIdent'] = None
    response['type'] = "powerTournament"
    response['offerType'] = "powerTournament"
    response['clientType'] = None
    response['offerData'] = []

    endDate = datetime(2025, 5, 30)
    endTime = datetime.combine(endDate, time.min)
    response['endTime'] = int(endTime.timestamp())

    response['clientData'] = getTournamentClientData()

    return response


def getTournamentClientData():
    response = {}
    response['entryButtonData'] = {
            "buttonAsset": "power_tournament_entrance_2",
            "buttonClipName": "power_tournament_entrance_class",
            "buttonPivotX": 30,
            "buttonPivotY": 0,
            "spineAnimationAsset": "Mainscreen_TournamentOfPower_VFX",
            "spineAnimationInversion": True
            }

    response['popupActive'] = getPopup('dialog_main_active')
    response['popupFinished'] = getPopup('dialog_main_finished')
    response['popupRating'] = getPopup('dialog_main_rating')
    response['popupHub'] = getPopup('dialog_hub')
    response['popupTutorial'] = getTutorial()

    response['backgroundStatueAsset'] = "power_tournament_background"
    response['specialQuestEventId'] = 576
    response['hubOffers'] = []

    response['locale'] = getLocale()
    return response


def getPopup(name):
    return {
            "asset": "power_tournament_dialogs",
            "clip": name
            }


def getTutorial():
    return {
            "asset": "power_tournament_tutorial",
            "clip": "power_tournament_tutorial"
            }


def getLocale():
    return {
      "title_active": "TOURNAMENT_NAME_HEROES",
      "title_finished": "TOURNAMENT_FINISH_DESCRIPTION",
      "title_rating": "TOURNAMENT_BUTTON_LEADERBOARD",
      "timeToNextDay": "TOURNAMENT_MAIN_SCREEN_TIMER_DESCRIPTION",
      "timeToEnd": "TOURNAMENT_LEADERBOARD_TIMER_DESCRIPTION",
      "ratingDescFooter": "TOURNAMENT_LEADERBOARD_TOOLTIP_DESCRIPTION",
      "ratingDescFinished": "TOURNAMENT_FINISH_DESCRIPTION",
      "currentPlace": "TOURNAMENT_MAIN_SCREEN_PLACE",
      "currentPoints": "TOURNAMENT_MAIN_SCREEN_SCORE_TODAY",
      "finalPlace": "TOURNAMENT_FINAL_SCREEN_PLAYER_PLACE",
      "finalReward": "TOURNAMENT_FINAL_SCREEN_PLAYER_REWARD",
      "buttonRating": "TOURNAMENT_BUTTON_LEADERBOARD",
      "buttonGo": "TOURNAMENT_BUTTON_UPGRADE_POWER",
      "buttonEvent": "TOURNAMENT_LEADERBOARD_BUTTON_TO_EVENT",
      "buttonHub": "UI_MAINMENU_OFFERS_BUTTON",
      "buttonFarmFinal": "UI_DIALOG_QUEST_FARM",
      "buttonRatingOk": "UI_COMMON_OK",
      "hubTitles": [
        "TOURNAMENT_OFFERS_HUB_ENERGY_OFFER",
        "TOURNAMENT_OFFERS_HUB_SKIN_OFFER",
        "TOURNAMENT_OFFERS_HUB_CORES_OFFER",
        "TOURNAMENT_OFFERS_HUB_RELICS_OFFER"
      ],
      "hubDescriptions": [
        "TOURNAMENT_OFFERS_HUB_ENERGY_OFFER_DESC",
        "TOURNAMENT_OFFERS_HUB_SKIN_OFFER_DESC",
        "TOURNAMENT_OFFERS_HUB_CORES_OFFER_DESC",
        "TOURNAMENT_OFFERS_HUB_RELICS_OFFER_DESC"
      ],
      "hubOfferUnavailable": "UI_UNAVAILABLE",
      "interactiveTutorial": [
        "TOURNAMENT_TUTORIAL_STEP1",
        "TOURNAMENT_TUTORIAL_STEP2",
        "TOURNAMENT_TUTORIAL_STEP3",
        "TOURNAMENT_TUTORIAL_STEP4",
        "TOURNAMENT_TUTORIAL_STEP5"
      ],
      "tutorialTitle": "TOURNAMENT_TUTORIAL_TITLE",
      "tutorialTopText": "TOURNAMENT_TUTORIAL_TOP_TEXT",
      "tutorialHints": [
        "TOURNAMENT_TUTORIAL_HINT_1",
        "TOURNAMENT_TUTORIAL_HINT_2",
        "TOURNAMENT_TUTORIAL_HINT_3"
      ],
      "tutorialBottomText": "TOURNAMENT_TUTORIAL_BOTTOM_TEXT",
      "tutorialSuper": "TOURNAMENT_TUTORIAL_SUPER"
    }
