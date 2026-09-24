#pragma endian big
import type.magic;
import std.mem;
import hex.dec;

struct SaveMeta<auto size> {
    u8 data[size];
};

struct CPUState {
    u8 bytes[272];
};

struct WRAM {
    u8 bytes[262144];
};

struct UncompressedPayload {
    // TODO
    u32 version_magic; 
    u32 bios_checksum; 
    u32 rom_crc32; 
    u32 master_cycles;
    char game_title[12];
    char game_code[4];
    CPUState cpu_state;
    WRAM wram @ 0x21000;
};

struct SaveState<auto size> {
    u8 zlib_data[size];
    std::mem::Section decompressed_sec = std::mem::create_section("Decompressed gbAs");
    hex::dec::zlib_decompress(zlib_data, decompressed_sec, 15);
    UncompressedPayload payload @ 0x00 in decompressed_sec;
};

struct Chunk {
    u32 size;
    char type[4];
    if (type == "gbAx") {
        SaveMeta<size> data;
    } else if (type == "gbAs") {
        SaveState<size> data;
    } else {
        u8 data[size]; 
    }
    u32 crc;
};

struct MGBASave {
    type::Magic<"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"> magic;
    Chunk chunk[while(!std::mem::eof())];
};

MGBASave saveFile @ 0x00;


// 89 50 4E 47 0D 0A 1A 0A