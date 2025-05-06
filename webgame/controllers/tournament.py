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
