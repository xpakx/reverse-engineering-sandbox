import os
import json
import time
import hashlib
import requests
from urllib.parse import urljoin
from pathlib import Path


"""
WARNING: Downloading all assets may consume approximately ~4GB of disk space.
Run with caution if you have limited storage or bandwidth.
"""


def download_file(url, entry, assets_dir):
    file_url = urljoin(url, entry['path'])
    local_path = os.path.join(assets_dir, os.path.basename(entry['path']))

    print(f"Downloading {file_url}...")

    try:
        response = requests.get(file_url, stream=True)
        response.raise_for_status()

        temp_path = local_path + '.tmp'
        with open(temp_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        file_size = os.path.getsize(temp_path)
        if file_size != entry['size']:
            os.remove(temp_path)
            raise ValueError(f"Size mismatch: expected {entry['size']}, got {file_size}")

        md5 = hashlib.md5()
        with open(temp_path, 'rb') as f:
            while chunk := f.read(8192):
                md5.update(chunk)
        file_md5 = md5.hexdigest()

        if file_md5 != entry['md5']:
            os.remove(temp_path)
            raise ValueError(f"MD5 mismatch: expected {entry['md5']}, got {file_md5}")

        os.rename(temp_path, local_path)

        print(f"Successfully downloaded and verified {entry['path']}")
        return True

    except Exception as e:
        print(f"Failed to download {entry['path']}: {str(e)}")
        return False


def process_entries(json_file, url, assets_dir):
    os.makedirs(assets_dir, exist_ok=True)
    with open(json_file, 'r') as f:
        data = json.load(f)

    for entry_key, entry_data in data.items():
        success = download_file(url, entry_data, assets_dir)
        if not success:
            continue

        time.sleep(1)


def process_entries_select(json_file, url, assets_dir, keys):
    os.makedirs(assets_dir, exist_ok=True)
    with open(json_file, 'r') as f:
        data = json.load(f)

    for entry_key in keys:
        entry_data = data[entry_key]
        success = download_file(url, entry_data, assets_dir)
        if not success:
            continue

        time.sleep(1)


def process_entries_js(json_file, url, assets_dir):
    os.makedirs(assets_dir, exist_ok=True)
    with open(json_file, 'r') as f:
        data = json.load(f)

    for entry_key, entry_data in data.items():
        if not entry_key.endswith('.js'):
            continue
        success = download_file(url, entry_data, assets_dir)
        if not success:
            continue

        time.sleep(1)


def process_entries_ver(json_file, url, assets_dir, parent_assets_dir):
    os.makedirs(assets_dir, exist_ok=True)
    with open(json_file, 'r') as f:
        data = json.load(f)

    for entry_key, entry_data in data.items():
        filename = os.path.basename(entry_data['path'])
        parent_file = Path(f"{parent_assets_dir}/{filename}")
        if parent_file.exists():
            print("File already exists. Skipping download.")
            continue
        current_file = Path(f"{assets_dir}/{filename}")
        if current_file.exists():
            print("File already exists. Skipping download.")
            continue
        success = download_file(url, entry_data, assets_dir)
        if not success:
            continue

        time.sleep(1)


if __name__ == "__main__":
    print("Warning: This will download ~4GB of assets. Ctrl+C to abort in 5s…")
    time.sleep(5)
    base_url = "https://heroesweb-a.akamaihd.net/wb/assets/"
    hash = "f867035b"
    json_file = f"./{hash}/indices/index.assets.json.backup"
    assets_dir = f"./{hash}/assets"
    parent_dir = "./assets"
    process_entries_ver(json_file, base_url, assets_dir, parent_dir)
