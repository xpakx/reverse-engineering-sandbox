import re
import json
from pathlib import Path

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


def find_script_by_hash(hash: str, name: str) -> str:
    folder = Path(f"../{hash}/akamaihd/")
    pattern = f"{name}.*.js"

    matches = list(folder.glob(pattern))
    if not matches:
        raise FileNotFoundError(f"No file matching pattern '{pattern}' found in '{hash}'.")
    return str(matches[0])


name = find_script_by_hash(hash, "heroes")
print(name)
extract_haxe_classes(
        name,
        'symbols_game.json',
        ("game.",),
        "k"
)

extract_haxe_classes(
        name,
        'symbols_engine.json',
        ("engine.",),
        "k"
)

extract_haxe_classes(
        name,
        'symbols_loader.json',
        ("loader.",),
        "k"
)


extract_haxe_classes(
        name,
        'symbols_js.json',
        ("js.",),
        "k"
)
