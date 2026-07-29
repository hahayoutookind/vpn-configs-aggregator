#!/usr/bin/env python3
import base64
import urllib.request
from pathlib import Path

URLS = [
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-SNI-RU-all.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/BLACK_SS%2BAll_RUS.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/BLACK_VLESS_RUS.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/BLACK_VLESS_RUS_mobile.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/Vless-Reality-White-Lists-Rus-Mobile.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-all.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-SNI-RU-all.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/refs/heads/main/V2RAY_RAW.txt",
    "https://raw.githubusercontenct.com/Epodonios/v2ray-configs/refs/heads/main/All_Configs_Sub.txt",
    "https://raw.githubusercontent.com/FNET00bot/FNET00/Config/Main",
    "https://raw.githubusercontent.com/nikita29a/FreeProxyList/refs/heads/main/mirror/1.txt"
]

def to_raw(url: str) -> str:
    if "github.com/" in url and "/blob/" in url:
        owner_repo, path = url.split("github.com/", 1)[1].split("/blob/", 1)
        return f"https://raw.githubusercontent.com/{owner_repo}/{path}"
    return url

def fetch_text(url: str) -> str:
    req = urllib.request.Request(
        to_raw(url),
        headers={"User-Agent": "Mozilla/5.0", "Accept": "text/plain,*/*"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", errors="replace")

def main():
    combined = "\n".join(fetch_text(url) for url in URLS)

    Path("all-vpn.txt").write_text(combined, encoding="utf-8")
    Path("all-vpn-base64.txt").write_text(
        base64.b64encode(combined.encode("utf-8")).decode("utf-8"),
        encoding="utf-8",
    )

if __name__ == "__main__":
    main()
