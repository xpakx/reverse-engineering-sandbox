from extractors.lib import GameData
from datetime import datetime

activeSeason = 8


def getSeason(request, temp, gameData: GameData):
    today = datetime.now()
    startDate = datetime(today.year, today.month, 1)
    startDate = int(startDate.timestamp())
    endDate = datetime(today.year, today.month, 28)
    endDate = int(endDate.timestamp())
    today = int(today.timestamp())
    result = {}
    result['id'] = activeSeason
    result['seasonAdventure'] = {
            'id': activeSeason,
            'startDate': startDate,
            'endDate': endDate,
            'closed': endDate < today,
            }
    return result
