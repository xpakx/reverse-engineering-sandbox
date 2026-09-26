import zlib
from construct import (
    Struct, Int32ub, Bytes, Const, GreedyRange, this
)

RawChunk = Struct(
    "size" / Int32ub,
    "type" / Bytes(4),
    "data" / Bytes(this.size),
    "crc" / Int32ub,
)

MGBASaveRaw = Struct(
    "magic" / Const(b"\x89PNG\r\n\x1a\n"),
    "chunks" / GreedyRange(RawChunk),
)


def inject_wram(original_ss_path, new_wram_bytes, output_ss_path):
    with open(original_ss_path, "rb") as f:
        parsed = MGBASaveRaw.parse_stream(f)

    new_chunks = []

    for chunk in parsed.chunks:
        if chunk.type == b"gbAs":
            decompressed = bytearray(zlib.decompress(chunk.data))

            wram_offset = 0x21000
            wram_size = 262144

            if len(new_wram_bytes) != wram_size:
                raise ValueError(f"New WRAM size must be exactly {wram_size} bytes (got {len(new_wram_bytes)})")

            decompressed[wram_offset:wram_offset + wram_size] = new_wram_bytes
            new_compressed = zlib.compress(decompressed)
            new_crc = zlib.crc32(chunk.type + new_compressed) & 0xFFFFFFFF

            new_chunks.append({
                "size": len(new_compressed),
                "type": chunk.type,
                "data": new_compressed,
                "crc": new_crc,
            })
        else:
            new_chunks.append({
                "size": chunk.size,
                "type": chunk.type,
                "data": chunk.data,
                "crc": chunk.crc,
            })

    rebuilt_file = MGBASaveRaw.build({
        "magic": b"\x89PNG\r\n\x1a\n",
        "chunks": new_chunks
    })

    with open(output_ss_path, "wb") as f:
        f.write(rebuilt_file)

    print(f"Successfully updated WRAM and saved to '{output_ss_path}'")


if __name__ == "__main__":
    with open("game_wram.bin", "rb") as f:
        modified_wram = f.read()
    inject_wram("../save.ss1", modified_wram, "../new_save.ss1")
