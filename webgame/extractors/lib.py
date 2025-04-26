import json


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


if __name__ == "__main__":
    input_file = "./indices/lib.json"

    with open(input_file, 'r') as f:
        data = json.load(f)
    # print_keys(data)

    heroes = get_enemies(data)

    # print_keys(heroes[2])
    missions = get_missions(data)
    print(missions[1])
