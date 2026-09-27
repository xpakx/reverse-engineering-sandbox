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

bitfield TurnStatus {
    hidden          : 1; // Hidden
    move_finished   : 1; // Move fully finished
    dead            : 1; // Dead
    unselected_unk  : 1; // Unselected???

    rescuer         : 1; // Rescuer unit
    rescued         : 1; // Rescued unit
    move_committed  : 1; // Move committed
    flag_unk        : 1; // Unknown flag

    // [flag_unk, move_commited, rescued, rescuer] [unselected_unk, dead, move_finished, hidden]

    // MOVED
    // 0100 0010 make move fully finished
    // 0100 0000 make unit greyed out (after visual update), but
    //		it still can be moved
    //		although move cannot be cancelled out
    // 0000 0010 is still fully finished move
    
    // it seems we're still lacking flag to grey out a unit
    // although, it seems that this does update after move, so
    // probably visual refresh is only after action

    // RESCUED
    // 0010 0000 is enough to make a rescued icon in the profile
    // normally used with HIDDEN

    // RESCUER
    // 0001 0000 this seem to be fully functional
    //		i assume 'rescue' or 'unk5' has sth to do 
    //		with the actual unit
    // normally used with HIDDEN

    // HIDDEN
    // 0000 0001 this seem to make a unit hidden/out of map
    // used with RESCUED, RESCUER or DEAD

    // DEAD
    // 0000 0101
    // 0000 0100 seem to be dead in a menus/for attacking,
    //		but enemies still try to approach unit if it is 
    //		not hidden with last bit
    // normally used with HIDDEN

    // UNSELECTED
    // 0000 1000 seems to make unit non selected during pre-mission selection
};

enum HiddenStatus : u8 {
    // 0x10 and 0x20 seems to be swapped??
    NoEffect = 0x00, 			// 0000 0000
    Afa = 0x10,  			// 0001 0000 
    WillDropLastItem = 0x20, 		// 0010 0000
    AfaAndWillDropLastItem = 0x30 	// 0011 0000
    // bitmask? [unk, unk, afa?, will_drop] [in_ballista, unk, unk, unk]

    // first two makes unit unattackable by enemies
    // penultimate makes unit visually invisible if cursor is not on it
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

enum CharPortrait : u16 {
    Eliwood = 0xCE4C,
    Hector = 0xCE80,
    Lyn = 0xCEB4,
    Raven = 0xCEE8,
    Geitz = 0xCF1C,
    Guy = 0xCF50,
    Karel = 0xCF84,
    Dorcas = 0xCFB8,
    Bartre = 0xCFEC,
    Citizen = 0xD020,
    Oswin = 0xD054,
    Fargus = 0xD088,
    Wil = 0xD0BC,
    Rebecca = 0xD0F0,
    Louise = 0xD124,
    Lucius = 0xD158,
    Serra = 0xD18C,
    Renault = 0xD1C0,
    Erk = 0xD1F4,
    Nino = 0xD228,
    Pent = 0xD25C,
    Canas = 0xD290,
    Kent = 0xD2C4,
    Sain = 0xD2F8,
    Lowen = 0xD32C,
    Marcus = 0xD360,
    Priscilla = 0xD394,
    Rath = 0xD3C8,
    Florina = 0xD3FC,
    Fiora = 0xD430,
    Farina = 0xD464,
    Heath = 0xD498,
    Vaida = 0xD4CC,
    Hawkeye = 0xD500,
    Matthew = 0xD534,
    Jaffar = 0xD568,
    Ninian = 0xD59C,
    Nils = 0xD5D0,
    Athos = 0xD604,
    Merlinus = 0xD638,
    Nils2 = 0xD66C,
    Uther = 0xD6A0,
    Vaida2 = 0xD6D4,
    Wallace = 0xD708,
    Lyn2 = 0xD73C,
    Wil2 = 0xD770,
    Kent2 = 0xD7A4,
    Sain2 = 0xD7D8,
    Florina2 = 0xD80C,
    Rath2 = 0xD840,
    Dart2 = 0xD874,
    Isadora = 0xD8A8,
    Eleanora = 0xD8DC,
    Legault = 0xD910,
    Karla = 0xD944,
    Harken = 0xD978,
    Leila = 0xD9AC,
    Bramimond = 0xD9E0,
    Kishuna = 0xDA14,
    Groznyi = 0xDA48,
    Wire = 0xDA7C,
    Bandit = 0xDAB0,
    Zagan = 0xDAE4,
    Boies = 0xDB18,
    Puzon = 0xDB4C,
    Bandit2 = 0xDB80,
    Santals = 0xDBB4,
    Nergal = 0xDBE8,
    Erik = 0xDC1C,
    Sealen = 0xDC50,
    Bauker = 0xDC84,
    Bernard = 0xDCB8,
    Damian = 0xDCEC,
    Zoldam = 0xDD20,
    Uhai = 0xDD54,
    Aion = 0xDD88,
    Darin = 0xDDBC,
    Cameron = 0xDDF0,
    Oleg = 0xDE24,
    Eubans = 0xDE58,
    Ursula = 0xDE8C,
    BlackFang = 0xDEC0,
    Paul = 0xDEF4,
    Jasmine = 0xDF28,
    BlackFang2 = 0xDF5C,
    JermeMorph = 0xDF90,
    Pascal = 0xDFC4,
    Kenneth = 0xDFF8,
    Jerme = 0xE02C,
    Maxime = 0xE060,
    Sonia = 0xE094,
    Teodor = 0xE0C8,
    Georg = 0xE0FC,
    Kaim = 0xE130,
    Merc = 0xE164,
    Denning = 0xE198,
    Bern = 0xE1CC,
    Morph = 0xE200,
    Lloyd = 0xE234,
    Linus = 0xE268,
    Lloyd2 = 0xE29C,
    Linus2 = 0xE2D0,
    Bandit3 = 0xE304,
    Bandit4 = 0xE338,
    Bandit5 = 0xE36C,
    Laus = 0xE3A0,
    Laus2 = 0xE3D4,
    Pirate = 0xE408,
    BlackFang3 = 0xE43C,
    BlackFang4 = 0xE470,
    Ostia = 0xE4A4,
    BlackFang5 = 0xE4D8,
    Guardian = 0xE50C,
    Morph2 = 0xE540,
    Morph3 = 0xE574,
    Morph4 = 0xE5A8,
    Caelin = 0xE5DC,
    Caelin2 = 0xE610,
    Caelin3 = 0xE644,
    Laus3 = 0xE678,
    Laus4 = 0xE6AC,
    Zephiel = 0xE6E0,
    Elbert = 0xE714,
    BlackFang6 = 0xE748,
    BlackFang7 = 0xE77C,
    BlackFang8 = 0xE7B0,
    Morph5 = 0xE7E4,
    Morph6 = 0xE818,
    Morph7 = 0xE84C,
    Morph8 = 0xE880,
    BlackFang9 = 0xE8B4,
    Brendan = 0xE8E8,
    Limstella = 0xE91C,
    Dragon = 0xE950,
    Batta = 0xE984,
    Bandit6 = 0xE9B8,
    Zugu = 0xE9EC,
    Bandit7 = 0xEA20,
    Bandit8 = 0xEA54,
    Bandit9 = 0xEA88,
    Glass = 0xEABC,
    Migal = 0xEAF0,
    Bandit10 = 0xEB24,
    Bandit11 = 0xEB58,
    Bandit12 = 0xEB8C,
    Bandit13 = 0xEBC0,
    Bandit14 = 0xEBF4,
    Carjiga = 0xEC28,
    Bandit15 = 0xEC5C,
    Bandit16 = 0xEC90,
    Bandit17 = 0xECC4,
    Bandit18 = 0xECF8,
    Bug = 0xED2C,
    Bandit19 = 0xED60,
    Bandit20 = 0xED94,
    Bandit21 = 0xEDC8,
    Bandit22 = 0xEDFC,
    Natalie = 0xEE30,
    Bool = 0xEE64,
    Bandit23 = 0xEE98,
    Bandit24 = 0xEECC,
    Bandit25 = 0xEF00,
    Bandit26 = 0xEF34,
    Bandit27 = 0xEF68,
    Bandit28 = 0xEF9C,
    Heintz = 0xEFD0,
    BlackFang10 = 0xF004,
    BlackFang11 = 0xF038,
    BlackFang12 = 0xF06C,
    BlackFang13 = 0xF0A0,
    BlackFang14 = 0xF0D4,
    BlackFang15 = 0xF108,
    Beyard = 0xF13C,
    BlackFang16 = 0xF170,
    BlackFang17 = 0xF1A4,
    BlackFang18 = 0xF1D8,
    BlackFang19 = 0xF20C,
    BlackFang20 = 0xF240,
    BlackFang21 = 0xF274,
    BlackFang22 = 0xF2A8,
    BlackFang23 = 0xF2DC,
    Yogi = 0xF310,
    Caelin4 = 0xF344,
    Caelin5 = 0xF378,
    Caelin6 = 0xF3AC,
    Caelin7 = 0xF3E0,
    Caelin8 = 0xF414,
    Caelin9 = 0xF448,
    Caelin10 = 0xF47C,
    Eagler = 0xF4B0,
    Caelin11 = 0xF4E4,
    Caelin12 = 0xF518,
    Caelin13 = 0xF54C,
    Caelin14 = 0xF580,
    Caelin15 = 0xF5B4,
    Caelin16 = 0xF5E8,
    Lundgren = 0xF61C,
    Caelin17 = 0xF650,
    Caelin18 = 0xF684,
    Caelin19 = 0xF6B8,
    Caelin20 = 0xF6EC,
    Caelin21 = 0xF720,
    Caelin22 = 0xF754,
    Caelin23 = 0xF788,
    Tactician = 0xF7BC,
    Citizen2 = 0xF7F0,
    Citizen3 = 0xF824,
    Citizen4 = 0xF858,
    Citizen5 = 0xF88C,
    Citizen6 = 0xF8C0,
    Citizen7 = 0xF8F4,
    Citizen8 = 0xF928,
    Citizen9 = 0xF95C,
    Citizen10 = 0xF990,
    Merc2 = 0xF9C4,
    Pirate2 = 0xF9F8,
    Bandit29 = 0xFA2C,
    Citizen11 = 0xFA60,
    Citizen12 = 0xFA94,
    Citizen13 = 0xFAC8,
    BlackFang24 = 0xFAFC,
    BlackFang25 = 0xFB30,
    Bandit30 = 0xFB64,
    BlackFang26 = 0xFB98,
    Morph9 = 0xFBCC,
    BlackFang27 = 0xFC00,
    BlackFang28 = 0xFC34,
    Bandit31 = 0xFC68,
    Ostia2 = 0xFC9C,
    RathUnit = 0xFCD0,
    Bandit32 = 0xFD04,
    Bandit33 = 0xFD38,
    Bern2 = 0xFD6C,
    Guardian2 = 0xFDA0,
    Morph10 = 0xFDD4,
    Laus5 = 0xFE08,
    Bandit34 = 0xFE3C,
    Bandit35 = 0xFE70,
    Bern3 = 0xFEA4,
    Guardian3 = 0xFED8,
    Morph11 = 0xFF0C,
    Guardian4 = 0xFF40,
    BlackFang29 = 0xFF74,
    LloydMorph = 0xFFA8,
    LinusMorph = 0xFFDC,
};

struct Item {
    u8 type;
    u8 quantity;
};

struct Character {
   CharPortrait portrait;
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
   u8 supports[7];
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

