"""Core conversions for gold prices.

International spot gold is quoted in USD per troy ounce.
Chinese retail/investment prices are usually quoted in CNY per gram.

1 troy ounce = 31.1034768 grams (exact definition used industry-wide).
"""
from __future__ import annotations

GRAMS_PER_TROY_OUNCE = 31.1034768


def usd_oz_to_cny_g(price_usd_per_oz: float, usd_cny_rate: float) -> float:
    """Convert a USD/troy-ounce gold price to CNY/gram.

    Args:
        price_usd_per_oz: Spot price, e.g. 2650.30
        usd_cny_rate: USD/CNY exchange rate, e.g. 7.25

    Returns:
        Price in CNY per gram, rounded to 2 decimals.
    """
    if price_usd_per_oz <= 0:
        raise ValueError("price_usd_per_oz must be positive")
    if usd_cny_rate <= 0:
        raise ValueError("usd_cny_rate must be positive")
    return round(price_usd_per_oz * usd_cny_rate / GRAMS_PER_TROY_OUNCE, 2)


def format_briefing(date_str: str, spot_usd_oz: float, usd_cny_rate: float,
                    sge_au9999: float | None = None, note: str = "") -> str:
    """Format a short, shareable daily briefing (no calculation steps)."""
    cny_g = usd_oz_to_cny_g(spot_usd_oz, usd_cny_rate)
    lines = [f"Gold Daily Brief - {date_str}", "",
             f"International spot: ${spot_usd_oz:,.2f} /oz",
             f"Converted: {cny_g:,.2f} CNY/g"]
    if sge_au9999 is not None:
        lines.append(f"SGE Au99.99: {sge_au9999:,.2f} CNY/g")
    if note:
        lines += ["", note]
    return "\n".join(lines)
