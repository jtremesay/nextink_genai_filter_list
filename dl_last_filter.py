from datetime import datetime, timezone

import httpx

UPDATE_URL = "https://next.ink/wp-content/uploads/2025/08/bloom-genai.json"


def main():
    today = datetime.now(timezone.utc).strftime(r"%Y%m%d")

    r = httpx.get(UPDATE_URL, timeout=60.0)
    with open(f"bloom_filter_{today}.json", "wb") as f:
        f.write(r.content)


if __name__ == "__main__":
    main()
