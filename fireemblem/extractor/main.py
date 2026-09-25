from construct import (
    Struct, Int32ub, Bytes, Const, Switch,
    GreedyRange, FixedSized, Compressed,
    PaddedString, Pointer, this
)

UncompressedPayload = Struct(
    "version_magic" / Int32ub,
    "bios_checksum" / Int32ub,
    "rom_crc32" / Int32ub,
    "master_cycles" / Int32ub,
    "game_title" / PaddedString(12, "ascii"),
    "game_code" / PaddedString(4, "ascii"),
    "cpu_state" / Bytes(272),
    "wram" / Pointer(0x21000, Bytes(262144)),
)

Chunk = Struct(
    "size" / Int32ub,
    "type" / Bytes(4),
    "data" / Switch(
        this.type,
        {
            b"gbAs": FixedSized(this.size, Compressed(UncompressedPayload, "zlib")),
        },
        default=Bytes(this.size)
    ),
    "crc" / Int32ub,
)

MGBASave = Struct(
    "magic" / Const(b"\x89PNG\r\n\x1a\n"),
    "chunks" / GreedyRange(Chunk),
)


def parse_and_decompress(file_path):
    with open(file_path, "rb") as f:
        parsed = MGBASave.parse_stream(f)

    for chunk in parsed.chunks:
        if chunk.type == b"gbAs":
            save_state = chunk.data
            print(f"Game Title: {save_state.game_title}")
            print(f"Game Code:  {save_state.game_code}")
            print(f"WRAM size:  {len(save_state.wram)} bytes")
            return save_state

    print("No gbAs save state chunk found.")
    return None


def save_wram_to_file(mgba_save_path, output_wram_path="wram.bin"):
    save_state = parse_and_decompress(mgba_save_path)

    if save_state:
        with open(output_wram_path, "wb") as f:
            f.write(save_state.wram)

        print(f"Successfully exported {len(save_state.wram)} bytes to '{output_wram_path}'")


save_wram_to_file("../save.ss1", "game_wram.bin")
