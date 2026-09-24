#pragma endian little
import type.magic;
import std.mem;


struct CPUState {
    u8 bytes[272];
};

u32 EWRAM_BASE = 0x02000000;
u32 IWRAM_BASE = 0x03000000;

fn ewram_off(u32 gba_addr) { return gba_addr - EWRAM_BASE; };
fn iwram_off(u32 gba_addr) { return gba_addr - IWRAM_BASE; };

enum Phase : u8 {
    Player = 0x00,
    Neutral = 0x40,
    Enemy = 0x80
};

enum TurnStatus : u8 {
    NotMoved = 0x00,
    Rescuer = 0x10,
    Moved = 0x42,
    MovedRescuer = 0x52,
    Rescued = 0x63
};

enum HiddenStatus : u8 {
    NoEffect = 0x00,
    Afa = 0x10,
    WillDropLastItem = 0x20,
    AfaAndWillDropLastItem = 0x30
};

enum CharClass : u16 {
    Eliwood = 0x01B0,
    Lyn = 0x0204,
    Hector = 0x0258,
    KnightLord = 0x03A8,
    BladeLord = 0x03FC,
    GreatLord = 0x0450,
    Mercenary = 0x04A4,
    Mercenary2 = 0x04F8,
    MaleHero = 0x054C,
    FemaleHero = 0x05A0,
    MaleMyrmidon = 0x05F4,
    FemaleMyrmidon = 0x0648,
    MaleSwordmaster = 0x069C,
    FemaleSwordmaster = 0x06F0,
    Fighter = 0x0744,
    Warrior = 0x0798,
    MaleKnight = 0x07EC,
    FemaleKnight = 0x0840,
    MaleGeneral = 0x0894,
    FemaleGeneral = 0x08E8,
    MaleArcher = 0x093C,
    FemaleArcher = 0x0990,
    MaleSniper = 0x09E4,
    FemaleSniper = 0x0A38,
    Monk = 0x0A8C,
    Cleric = 0x0AE0,
    MaleBishop = 0x0B34,
    FemaleBishop = 0x0B88,
    MaleMage = 0x0BDC,
    FemaleMage = 0x0C30,
    MaleSage = 0x0C84,
    FemaleSage = 0x0CD8,
    MaleShaman = 0x0D2C,
    FemaleShaman = 0x0D80,
    MaleDruid = 0x0DD4,
    FemaleDruid = 0x0E28,
    MaleCavalier = 0x0E7C,
    FemaleCavalier = 0x0ED0,
    MalePaladin = 0x0F24,
    FemalePaladin = 0x0F78,
    Troubadour = 0x0FCC,
    Valkyrie = 0x1020,
    MaleNomad = 0x1074,
    FemaleNomad = 0x10C8,
    MaleTrooper = 0x111C,
    FemaleTrooper = 0x1170,
    PegasusKnight = 0x11C4,
    Falcoknight = 0x1218,
    MaleWyvernRider = 0x126C,
    FemaleWyvernRider = 0x12C0,
    MaleWyvernLord = 0x1314,
    FemaleWyvernLord = 0x1368,
    Soldier = 0x13BC,
    Brigand = 0x1410,
    Pirate = 0x1464,
    Berserker = 0x14B8,
    MaleThief = 0x150C,
    FemaleThief = 0x1560,
    Assassin = 0x15B4,
    DeadCivilian = 0x1608,
    Dancer = 0x165C,
    Bard = 0x16B0,
    Archsage = 0x1704,
    MagicSeal = 0x1758,
    Tent = 0x17AC,
    DarkDruid = 0x1800,
    FireDragon = 0x1854,
    MaleCivilian = 0x18A8,
    FemaleCivilian = 0x18FC,
    NilsVar = 0x1950,
    Bramimond = 0x19A4,
    MalePeer = 0x19F8,
    FemalePeer = 0x1A4C,
    Prince = 0x1AA0,
    Queen = 0x1AF4,
    Civilian = 0x1B48,
    Corsair = 0x1B9C,
    Prince = 0x1BF0,
    Prince2 = 0x1C44,
    Prince3 = 0x1C98,
    Child = 0x1CEC,
    FireDragon = 0x1D40,
    DeadWarrior = 0x1D94,
    MaleChild = 0x1DE8,
    FemaleChild = 0x1E3C,
    TransporterCart = 0x1E90,
    FemaleSage = 0x1EE4,
    ArcherBallista = 0x1F38,
    ArcherIronBallista = 0x1F8C,
    ArcherKillerBallista = 0x1FE0,
    EmptyBallista = 0x2034,
    EmptyIronBallista = 0x2088,
    EmptyKillerBallista = 0x20DC,
};

struct Item {
    u8 type;
    u8 quantity;
};

struct Character {
   u16 portrait;
   u16 unk1;
   CharClass class;
   u16 unk2;
   u8 level;
   u8 exp;
   u16 unk3;
   TurnStatus turn_status;
   HiddenStatus hidden_status;
   u16 unk4;
   u8 horiz_pos;  // (0,0) is in top left
   u8 vert_pos;
   u8 max_hp;
   u8 curr_hp;
   u8 strength;
   u8 skill;
   u8 speed;
   u8 defense;
   u8 resistance;
   u8 luck;
   u8 constitution_bonus;
   u8 rescue;
   u8 unk5;
   u8 move_bonus;
   Item items[5];
   u8 sword_skill;
   u8 lance_skill;
   u8 axe_skill;
   u8 bow_skill;
   u8 staff_skill;
   u8 anima_skill;
   u8 light_skill;
   u8 dark_skill;
   u8 status_effect; //enum
   u8 unk6;
   u8 support[7];
   u8 unk7[15];
};


struct ExternalWRAM {
    u8 bytes[262144];
    char tactician_name[7] @ addressof(bytes) + ewram_off(0x202BC18);
    u32 money @ addressof(bytes) + ewram_off(0x202BC00);
    u16 turn_num @ addressof(bytes) + ewram_off(0x202BC08);
    Phase phase @ addressof(bytes) + ewram_off(0x202BC07);
    Character chars[16] @ addressof(bytes) + ewram_off(0x202BD50);
    Item merlinus[100] @ addressof(bytes) + ewram_off(0x203A720);
};

struct InternalWRAM {
    u8 bytes[262144];
    //u8 test @ addressof(bytes) + iwram_off(0x202BC18);

   
    
};

struct Save {
    u32 version_magic; 
    u32 bios_checksum; 
    u32 rom_crc32; 
    u32 master_cycles;
    char game_title[12];
    char game_code[4];
    CPUState cpu_state;
    InternalWRAM iwram @ 0x19000;
    ExternalWRAM wram @ 0x21000;
};


Save saveFile @ 0x00;

