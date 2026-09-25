from construct import (
        Struct, Pointer, PaddedString, Int32ul, Int16ul,
        Int8ul, Enum, Array
)

PhaseEnum = Enum(
        Int8ul,
        Player=0x00,
        Neutral=0x40,
        Enemy=0x80,
)

Item = Struct(
        "id" / Int8ul,
        "quantity" / Int8ul,
)

Character = Struct(
        "portrait" / Int16ul,
        "unk1" / Int16ul,
        "char_class" / Int8ul,
        "unk2" / Int16ul,
        "level" / Int8ul,
        "exp" / Int8ul,
        "unk3" / Int16ul,
        "turn_status" / Int32ul,
        "hidden_status" / Int32ul,
        "unk4" / Int16ul,
        "horiz_pos" / Int8ul,
        "vert_pos" / Int8ul,
        "max_hp" / Int8ul,
        "curr_hp" / Int8ul,
        "strength" / Int8ul,
        "skill" / Int8ul,
        "speed" / Int8ul,
        "defense" / Int8ul,
        "resistance" / Int8ul,
        "luck" / Int8ul,
        "constitution_bonus" / Int8ul,
        "rescue" / Int8ul,
        "unk5" / Int8ul,
        "move_bonus" / Int8ul,
        "items" / Array(5, Item),
        "sword_skill" / Int8ul,
        "lance_skill" / Int8ul,
        "axe_skill" / Int8ul,
        "bow_skill" / Int8ul,
        "staff_skill" / Int8ul,
        "anima_skill" / Int8ul,
        "light_skill" / Int8ul,
        "dark_skill" / Int8ul,
        "status_effect" / Int8ul,
        "unk6" / Int8ul,
        "supports" / Array(7, Int8ul),
        "unk7" / Array(15, Int8ul),
)

WRAMStructure = Struct(
        "player_name" / Pointer(0x2BC18, PaddedString(7, "ascii")),
        "money" / Pointer(0x2BC00, Int32ul),
        "turn_num" / Pointer(0x2BC08, Int16ul),
        "phase" / Pointer(0x2BC07, PhaseEnum),
        "chars" / Pointer(0x2BD50, Array(16, Character)),
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

    print("--- Characters ---")
    for i, char in enumerate(parsed.chars):
        print(f"Slot {i:2d} | Lvl {char.level:2d} | {char.portrait} | {char.char_class}")
    return parsed


parse_wram_file("game_wram.bin")
