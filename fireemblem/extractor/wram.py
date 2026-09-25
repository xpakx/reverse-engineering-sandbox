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

CharClass = Enum(
        Int16ul,
        Eliwood=0x01B0,
        Lyn=0x0204,
        Hector=0x0258,
        KnightLord=0x03A8,
        BladeLord=0x03FC,
        GreatLord=0x0450,
        Mercenary=0x04A4,
        Mercenary2=0x04F8,
        MaleHero=0x054C,
        FemaleHero=0x05A0,
        MaleMyrmidon=0x05F4,
        FemaleMyrmidon=0x0648,
        MaleSwordmaster=0x069C,
        FemaleSwordmaster=0x06F0,
        Fighter=0x0744,
        Warrior=0x0798,
        MaleKnight=0x07EC,
        FemaleKnight=0x0840,
        MaleGeneral=0x0894,
        FemaleGeneral=0x08E8,
        MaleArcher=0x093C,
        FemaleArcher=0x0990,
        MaleSniper=0x09E4,
        FemaleSniper=0x0A38,
        Monk=0x0A8C,
        Cleric=0x0AE0,
        MaleBishop=0x0B34,
        FemaleBishop=0x0B88,
        MaleMage=0x0BDC,
        FemaleMage=0x0C30,
        MaleSage=0x0C84,
        FemaleSage=0x0CD8,
        MaleShaman=0x0D2C,
        FemaleShaman=0x0D80,
        MaleDruid=0x0DD4,
        FemaleDruid=0x0E28,
        MaleCavalier=0x0E7C,
        FemaleCavalier=0x0ED0,
        MalePaladin=0x0F24,
        FemalePaladin=0x0F78,
        Troubadour=0x0FCC,
        Valkyrie=0x1020,
        MaleNomad=0x1074,
        FemaleNomad=0x10C8,
        MaleTrooper=0x111C,
        FemaleTrooper=0x1170,
        PegasusKnight=0x11C4,
        Falcoknight=0x1218,
        MaleWyvernRider=0x126C,
        FemaleWyvernRider=0x12C0,
        MaleWyvernLord=0x1314,
        FemaleWyvernLord=0x1368,
        Soldier=0x13BC,
        Brigand=0x1410,
        Pirate=0x1464,
        Berserker=0x14B8,
        MaleThief=0x150C,
        FemaleThief=0x1560,
        Assassin=0x15B4,
        DeadCivilian=0x1608,
        Dancer=0x165C,
        Bard=0x16B0,
        Archsage=0x1704,
        MagicSeal=0x1758,
        Tent=0x17AC,
        DarkDruid=0x1800,
        FireDragon=0x1854,
        MaleCivilian=0x18A8,
        FemaleCivilian=0x18FC,
        NilsVar=0x1950,
        Bramimond=0x19A4,
        MalePeer=0x19F8,
        FemalePeer=0x1A4C,
        Prince4=0x1AA0,
        Queen=0x1AF4,
        Civilian=0x1B48,
        Corsair=0x1B9C,
        Prince=0x1BF0,
        Prince2=0x1C44,
        Prince3=0x1C98,
        Child=0x1CEC,
        FireDragon2=0x1D40,
        DeadWarrior=0x1D94,
        MaleChild=0x1DE8,
        FemaleChild=0x1E3C,
        TransporterCart=0x1E90,
        FemaleSage2=0x1EE4,
        ArcherBallista=0x1F38,
        ArcherIronBallista=0x1F8C,
        ArcherKillerBallista=0x1FE0,
        EmptyBallista=0x2034,
        EmptyIronBallista=0x2088,
        EmptyKillerBallista=0x20DC,
)

Item = Struct(
        "id" / Int8ul,
        "quantity" / Int8ul,
)

Character = Struct(
        "portrait" / Int16ul,
        "unk1" / Int16ul,
        "char_class" / CharClass,
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
