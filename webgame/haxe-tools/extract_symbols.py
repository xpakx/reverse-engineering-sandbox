import re
import json

hash = "d24aef06"


def extract_haxe_classes(
        js_file_path: str, output_json_path: str, prefixes: tuple[str],
        class_registry_name: str
):
    pattern = re.compile(
            fr'{class_registry_name}\["([^"]+)"\]=([a-zA-Z0-9_$]+)'
    )
    class_map = {}

    with open(js_file_path, 'r', encoding='utf-8') as file:
        js_content = file.read()

    for match in pattern.finditer(js_content):
        class_name = match.group(1)
        minified_var = match.group(2)

        if class_name.startswith((prefixes)):
            class_map[class_name] = minified_var

    with open(output_json_path, 'w', encoding='utf-8') as out_file:
        json.dump(class_map, out_file, indent=4)

    print("Successfully extracted")


# TODO: extract from indices
name = "heroes.d24aef0654d76f8bbeefb95953b00cf8.js"
extract_haxe_classes(
        f'../{hash}/akamaihd/{name}',
        'symbols.json',
        ("game.",),
        "k"
)
