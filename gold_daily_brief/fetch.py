"""Fetch spot gold and USD/CNY from free public endpoints (no API key).

Sources (verify availability in your region before relying on them):
- Gold: https://api.gold-api.com/price/XAU
- FX:   https://open.er-api.com/v6/latest/USD
"""
from __future__ import annotations
import json, urllib.request

def _get_json(url: str, timeout: int = 20) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "gold-daily-brief/0.1"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))

def fetch_spot_usd_oz() -> float:
    data = _get_json("https://api.gold-api.com/price/XAU")
    return float(data["price"])

def fetch_usd_cny() -> float:
    data = _get_json("https://open.er-api.com/v6/latest/USD")
    return float(data["rates"]["CNY"])
