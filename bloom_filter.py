import json
from collections.abc import Sequence
from pathlib import Path
from typing import Any


class BloomFilter:
    def __init__(self, size: int, num_hashes: int, bit_array: Sequence[int]):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = bytearray(bit_array)

    @staticmethod
    def fnv1a(string: str, seed: int = 0) -> int:
        hash_value = 2166136261 ^ seed
        for char in string:
            hash_value ^= ord(char)
            hash_value += (
                (hash_value << 1)
                + (hash_value << 4)
                + (hash_value << 7)
                + (hash_value << 8)
                + (hash_value << 24)
            )
        return hash_value & 0xFFFFFFFF

    def get_hash_values(self, string: str) -> list[int]:
        return [self.fnv1a(string, i) % self.size for i in range(self.num_hashes)]

    def might_contain(self, string: str) -> bool:
        hashes = self.get_hash_values(string)
        return all(self.bit_array[h] != 0 for h in hashes)

    def to_json(self) -> dict[str, Any]:
        return {
            "size": self.size,
            "num_hashes": self.num_hashes,
            "bit_array": list(self.bit_array),
        }

    @staticmethod
    def from_json(json_data: dict[str, Any]) -> "BloomFilter":
        return BloomFilter(
            json_data["size"], json_data["numHashes"], json_data["bitArray"]
        )

    @staticmethod
    def from_file(file_path: str | Path) -> "BloomFilter":
        with open(file_path, "r") as f:
            return BloomFilter.from_json(json.load(f))
