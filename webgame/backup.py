import re
import requests
from pathlib import Path
from asset_downloader import process_entries, process_entries_select
from asset_downloader import process_entries_js
from asset_renamer import flatten_and_prepend_paths
import gzip
from typing import List, Set


def extractIndexHashes(data):
    pattern = re.compile(
        r'https?:\\/\\/[^"]+?\\/index\.(client|assets|lib)\.[a-f0-9]{32}\.json\.gz',
        re.IGNORECASE
    )

    hashes = {}
    for url in pattern.finditer(data):
        parts = url.group().split('/')[-1].split('.')
        if len(parts) >= 4:
            hash_type = parts[1]
            hash_value = parts[2]
            hashes[hash_type] = hash_value
    return hashes


def extractHeroHash(data):
    pattern = re.compile(
        r'https?:\\/\\/[^"]+?\\/heroes\.[a-f0-9]{32}\.js',
        re.IGNORECASE
    )

    url = pattern.search(data)
    parts = url.group().split('/')[-1].split('.')
    if len(parts) >= 3:
        return parts[1]
    return ""


def createVerDir(hash):
    shortHash = hash[:8]
    versionDir = Path(shortHash)
    versionDir.mkdir(exist_ok=True)

    indices = versionDir / "indices"
    indices.mkdir(exist_ok=True)
    return shortHash


def downloadFile(name, filename, filepath, url):
    print(f"Downloading {name}...")
    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()

        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Saved {filename} to {dir}")
    except Exception as e:
        print(f"Failed to download {filename}: {str(e)}")


def downloadIndex(index, hash, dir):
    baseUrl = "https://heroesweb-a.akamaihd.net/wb"
    url = f"{baseUrl}/{index}/index.{index}.{hash}.json.gz"
    filename = f"index.{index}.json.gz"
    filepath = Path(dir) / "indices" / filename
    downloadFile(index, filename, filepath, url)


def extractIndex(index, hash):
    index_gz = f'{hash}/indices/index.{index}.json.gz'
    index_json = f'{hash}/indices/index.{index}.json'

    with gzip.open(index_gz, 'rb') as gz_file:
        with open(index_json, 'wb') as out_file:
            out_file.write(gz_file.read())


def downloadFromIndex(index, hash):
    js = f'{hash}/akamaihd'
    js = Path(js)
    js.mkdir(exist_ok=True)

    extractIndex(index, hash)

    process_entries(
            f'{hash}/indices/index.{index}.json',
            f'https://heroesweb-a.akamaihd.net/wb/{index}/',
            f'./{hash}/akamaihd'
            )


def downloadLibFromIndex(index, hash):
    extractIndex(index, hash)

    process_entries_select(
            f'{hash}/indices/index.{index}.json',
            f'https://heroesweb-a.akamaihd.net/wb/{index}/',
            f'./{hash}/indices',
            ['en.json.gz', 'lib.json.gz']
            )


def downloadExternalLibsFromIndex(index, hash):
    extractIndex(index, hash)

    process_entries_js(
            f'{hash}/indices/index.{index}.json',
            f'https://heroesweb-a.akamaihd.net/wb/{index}/',
            f'./{hash}/akamaihd'
            )


def extractGameUrl(data):
    pattern = re.compile(
        r'https?://[^"]+?/game\.js',
        re.IGNORECASE
    )

    url = pattern.search(data)
    return url.group()


def downloadGameJs(url, hash):
    name = 'game'
    filename = "game.js"
    filepath = Path(hash) / filename
    downloadFile(name, filename, filepath, url)


def findJsImports(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    pattern = r'[\'"]([^\'"]+\.js)[\'"]'
    matches = re.findall(pattern, content)
    return matches


def getJsUrl(imports: List[str]):
    for imp in imports:
        if imp.endswith('apps.js'):
            return imp.rsplit('/', 1)[0]


def downloadAppAndTranslate(imports: List[str], hash: str, jsUrl: str) -> Set:
    nums = set()
    for imp in imports:
        if imp.endswith('apps.js'):
            name = 'apps'
            filename = "apps.js"
            dir = Path(f'{hash}/akamaihd')
            filepath = dir / filename
            url = f'{jsUrl}/{filename}'
            downloadFile(name, filename, filepath, url)
        elif imp.endswith('autoGenerateTranslate.js'):
            name = 'autoGenerateTranslate'
            filename = "autoGenerateTranslate.js"
            dir = Path(f'{hash}/js/locale/en')
            dir.mkdir(exist_ok=True, parents=True)
            filepath = dir / filename
            url = f'{jsUrl}/locale/en/{filename}'
            downloadFile(name, filename, filepath, url)
        else:
            if '/' in imp:
                nums.add(imp.rsplit('/', 1)[1])
            else:
                nums.add(imp)
    return nums


def addToNums(nums: Set[str], imports: List[str]):
    for imp in imports:
        if '/' in imp:
            nums.add(imp.rsplit('/', 1)[1])
        else:
            nums.add(imp)


def downloadNums(nums: Set[str], hash: str, jsUrl: str):
    for num in nums:
        name = num
        filename = num
        filepath = Path(f'{hash}/js') / filename
        url = f'{jsUrl}/{filename}'
        downloadFile(name, filename, filepath, url)


def readData(filename) -> str:
    with open(filename, 'r') as f:
        data = f.read()
        heroHash = extractHeroHash(data)
        hashToDir = createVerDir(heroHash)
        addDataJs(hashToDir, heroHash)

        hashes = extractIndexHashes(data)
        print(hashes)
        for hash in hashes:
            downloadIndex(hash, hashes[hash], hashToDir)
        downloadFromIndex('client', hashToDir)
        downloadLibFromIndex('lib', hashToDir)
        downloadExternalLibsFromIndex('assets', hashToDir)
        gameJs = extractGameUrl(data)
        print(gameJs)
        downloadGameJs(gameJs, hashToDir)
        imports = findJsImports(f'{hashToDir}/game.js')
        print(imports)
        jsUrl = getJsUrl(imports)
        print(jsUrl)
        nums = downloadAppAndTranslate(imports, hashToDir, jsUrl)
        print(nums)
        imports = findJsImports(f'{hashToDir}/akamaihd/apps.js')
        addToNums(nums, imports)
        print(nums)
        downloadNums(nums, hashToDir, jsUrl)
        return hashToDir


def replaceAppsJsUrl(data) -> str:
    return re.sub(
        r'https?://[^"]+?/js/apps\.js',
        "./akamaihd/apps.js",
        data
    )


def replaceBaseJsUrl(data) -> str:
    return re.sub(
        r'https?://[^"]+?/hw-web/v2/[0-9]{7}',
        "http://localhost:8081",
        data
    )


def patchGameJs(hash):
    filename = f'{hash}/game.js'
    path = Path(filename)
    data = path.read_text()
    data = replaceAppsJsUrl(data)
    data = replaceBaseJsUrl(data)
    path.write_text(data)


def replaceDataJsHash(data, fullHash) -> str:
    return data.replace(
        '{HEROES_HASH}',
        fullHash,
        1
    )


def addDataJs(hash, fullHash):
    orig = './data.template.js'
    filename = f'{hash}/data.js'
    path = Path(orig)
    data = path.read_text()
    data = replaceDataJsHash(data, fullHash)
    filename = f'{hash}/data.js'
    path = Path(filename)
    path.write_text(data)


def patchFiles(hash):
    patchGameJs(hash)
    flatten_and_prepend_paths(f"{hash}/indices/index.client.json", "../akamaihd")
    flatten_and_prepend_paths(f"{hash}/indices/index.assets.json", '../assets')


hash = readData('hero.html')
patchFiles(hash)
