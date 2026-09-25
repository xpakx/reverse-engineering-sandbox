from construct import (
        Struct, Pointer, PaddedString, Int32ul, Int16ul,
        Int8ul
)

WRAMStructure = Struct(
    "player_name" / Pointer(0x2BC18, PaddedString(7, "ascii")),
    "money" / Pointer(0x2BC00, Int32ul),
    "turn_num" / Pointer(0x2BC08, Int16ul),
    "phase" / Pointer(0x2BC07, Int8ul),
)


def parse_wram_file(wram_path="wram.bin"):
    with open(wram_path, "rb") as f:
        wram_data = f.read()

    parsed = WRAMStructure.parse(wram_data)

    print("--- Extracted WRAM Data ---")
    print(f"Player Name:     {parsed.player_name}")
    print(f"Money:           {parsed.money}")
    print(f"Turn:            {parsed.turn_num}")
    print(f"Phase:           {parsed.phase}")

    return parsed


parse_wram_file("game_wram.bin")
