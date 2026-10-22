"""CLI: python -m gold_daily_brief.cli [--push]"""
from __future__ import annotations
import argparse, datetime as dt, os, sys
from .core import format_briefing
from .fetch import fetch_spot_usd_oz, fetch_usd_cny

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Daily gold price briefing")
    ap.add_argument("--spot", type=float, help="Override spot USD/oz (skip fetch)")
    ap.add_argument("--rate", type=float, help="Override USD/CNY rate (skip fetch)")
    ap.add_argument("--sge", type=float, help="Optional SGE Au99.99 CNY/g")
    args = ap.parse_args(argv)
    spot = args.spot if args.spot is not None else fetch_spot_usd_oz()
    rate = args.rate if args.rate is not None else fetch_usd_cny()
    today = dt.date.today().isoformat()
    print(format_briefing(today, spot, rate, sge_au9999=args.sge))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
