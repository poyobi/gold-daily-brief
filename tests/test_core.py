import pytest
from gold_daily_brief.core import usd_oz_to_cny_g, format_briefing, GRAMS_PER_TROY_OUNCE

def test_conversion_known_value():
    # 31.1034768 USD/oz at rate 1.0 == exactly 1.00 CNY/g
    assert usd_oz_to_cny_g(GRAMS_PER_TROY_OUNCE, 1.0) == 1.00

def test_conversion_rejects_nonpositive():
    with pytest.raises(ValueError):
        usd_oz_to_cny_g(0, 7.2)
    with pytest.raises(ValueError):
        usd_oz_to_cny_g(2600, 0)

def test_format_contains_both_prices():
    out = format_briefing("2026-10-22", 2650.0, 7.25, sge_au9999=618.5)
    assert "2,650.00" in out and "618.50" in out
