import json

logs = False


def stash_handler(request_handler):
    return (
        200,
        {'Content-Type': 'application/json'},
        '{error: 0}'
    )


def logs_handler(request_handler):
    print('CLIENT ERROR')
    if logs:
        content_length = int(request_handler.headers.get('Content-Length', 0))
        raw_body = request_handler.rfile.read(content_length)
        print(raw_body)
    return (
        200,
        {'Content-Type': 'application/json'},
        '{error: 0}'
    )


def success_handler(request_handler):
    return (
        200,
        {'Content-Type': 'application/json'},
        '{success: true}'
    )


def currencies_handler(request_handler):
    currencies = [
            {"id": 129, "currency": "AUD"},
            {"id": 130, "currency": "BGN"},
            {"id": 131, "currency": "CAD"},
            {"id": 132, "currency": "CHF"},
            {"id": 133, "currency": "CNY"},
            {"id": 134, "currency": "CZK"},
            {"id": 135, "currency": "DKK"},
            {"id": 136, "currency": "EUR"},
            {"id": 137, "currency": "GBP"},
            {"id": 139, "currency": "HUF"},
            {"id": 140, "currency": "JPY"},
            {"id": 141, "currency": "KRW"},
            {"id": 142, "currency": "NOK"},
            {"id": 143, "currency": "NZD"},
            {"id": 144, "currency": "PHP"},
            {"id": 145, "currency": "PLN"},
            {"id": 146, "currency": "RON"},
            {"id": 147, "currency": "RUB"},
            {"id": 148, "currency": "SEK"},
            {"id": 149, "currency": "USD"}
        ]
    return (
        200,
        {'Content-Type': 'application/json'},
        json.dumps(currencies)

    )


def info_handler(request_handler):
    return (
        200,
        {'Content-Type': 'application/json'},
        "{}"
    )


def landing_handler(request_handler):
    return (
        200,
        {'Content-Type': 'application/json'},
        '{"data":{"result":true}}'
    )
