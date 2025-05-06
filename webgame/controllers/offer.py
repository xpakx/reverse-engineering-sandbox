from controllers.tournament import getTournamentOffer


def getOffers(request, temp, gameData):
    response = []
    tournament = getTournamentOffer()
    if tournament:
        response.append(tournament)
    return response
