import os
import json
import shutil


def flatten_and_prepend_paths(input_file):
    backup_file = input_file + ".backup"
    shutil.copy2(input_file, backup_file)
    print(f"Backup created: {backup_file}")

    with open(input_file, 'r') as f:
        data = json.load(f)

    modified_data = {}
    for filename, entry in data.items():
        basename = os.path.basename(entry["path"])

        modified_entry = entry.copy()
        modified_entry["path"] = f"../assets/{basename}"

        modified_data[filename] = modified_entry

    with open(input_file, 'w') as f:
        json.dump(modified_data, f, indent=2)

    print(f"Modified paths flattened and prepended with '../assets/' in {input_file}")


if __name__ == "__main__":
    input_file = "./indices/index.assets.json"
    flatten_and_prepend_paths(input_file)
