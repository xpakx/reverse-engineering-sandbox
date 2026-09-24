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

struct ExternalWRAM {
    u8 bytes[262144];
    char tactician_name[7] @ addressof(bytes) + ewram_off(0x202BC18);
    u32 money @ addressof(bytes) + ewram_off(0x202BC00);
    u16 turn_num @ addressof(bytes) + ewram_off(0x202BC08);
    Phase phase @ addressof(bytes) + ewram_off(0x202BC07);
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
