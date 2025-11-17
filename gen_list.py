from pathlib import Path

import zstd
from tqdm import tqdm

from bloom_filter import BloomFilter

FILTER_VERSION = "20251117"
FILTER_FILE = Path(f"bloom_filter_{FILTER_VERSION}.json")


def main():
    domains_to_check = set()
    for domains_file in Path("domains").glob("*.txt.zst"):
        print("Loading domains from", domains_file)
        domains_to_check.update(
            l.strip()
            for l in zstd.decompress(domains_file.read_bytes()).decode().splitlines()
        )
    print("Total domains loaded:", len(domains_to_check))

    filter = BloomFilter.from_file(FILTER_FILE)
    print("Filter loaded from", FILTER_FILE)

    with open(f"domains_in_filter_{FILTER_VERSION}.txt", "w") as out_file:
        for domain in tqdm(sorted(domains_to_check)):
            if filter.might_contain(domain):
                tqdm.write(f"Found {domain}")
                out_file.write(f"{domain}\n")


if __name__ == "__main__":
    main()
