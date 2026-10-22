# gold-daily-brief

A small, dependency-free Python tool that fetches the daily international
spot gold price, converts it from **USD / troy ounce** to **CNY / gram**,
and formats a short, shareable daily briefing.

Built and maintained by a single maintainer for a daily gold-price briefing
workflow, and released as open source so anyone tracking gold in CNY can
reuse the conversion and formatting logic instead of re-implementing it.

## Why this exists

- International spot gold is quoted in USD/oz, but Chinese investors and
  jewellers think in CNY/g. Converting by hand every day is error-prone.
- Most price sites are heavy dashboards. This tool prints one short briefing:
  the original price and the converted price, nothing else.

## Install

```bash
pip install -e .
```

## Usage

```bash
# Fetch live price + USD/CNY rate and print today's briefing
gold-daily-brief

# Offline / reproducible run with your own numbers
gold-daily-brief --spot 2650.30 --rate 7.25 --sge 618.50
```

Example output:

```
Gold Daily Brief - 2026-10-22

International spot: $2,650.30 /oz
Converted: 617.77 CNY/g
SGE Au99.99: 618.50 CNY/g
```

## How it works

- `core.py` — pure conversion (1 troy ounce = 31.1034768 g) and formatting, fully tested.
- `fetch.py` — fetches spot XAU and USD/CNY from free public endpoints, no API key, stdlib only.
- `cli.py` — command-line entry point; values can be overridden for testing/offline use.

## Development

```bash
pip install -e . pytest
pytest -q
```

## Roadmap

- Optional PushPlus / webhook delivery of the daily briefing
- Historical CSV log and day-over-day change
- SGE Au99.99 auto-fetch

## License

MIT — see [LICENSE](LICENSE).
