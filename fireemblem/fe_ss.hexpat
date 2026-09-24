#pragma endian big
import type.magic;
import std.mem;

struct Chunk {
    u32 size;
    char type[4];
    u8 data[size]; 
    u32 crc;
};

struct MGBASave {
    type::Magic<"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"> magic;
    Chunk chunk[while(!std::mem::eof())];
};

MGBASave saveFile @ 0x00;


// 89 50 4E 47 0D 0A 1A 0A

