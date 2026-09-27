from extractor.extract import save_wram_to_file
from extractor.inject import inject_wram
from extractor.wram import inject_json, extract_json
import sys


def inject_full():
    inject_json("game_data.json", "game_wram.bin", "new_wram.bin")
    with open("new_wram.bin", "rb") as f:
        modified_wram = f.read()
    inject_wram("../save.ss1", modified_wram, "../new_save.ss1")


def extract_full():
    save_wram_to_file("../save.ss1", "game_wram.bin")
    extract_json("game_data.json", "game_wram.bin")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please provide command inject/extract.")
        sys.exit(1)

    user_cmd = sys.argv[1]
    if user_cmd == "inject":
        inject_full()
    elif user_cmd == "extract":
        extract_full()
    else:
        print("Error: Wrong command. Please use inject/extract.")
        sys.exit(1)
