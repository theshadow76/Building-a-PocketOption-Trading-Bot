import json
from chipa_ta import Candle, Indicator

raw_candles = [
    {"open": 1.1000, "high": 1.1050, "low": 1.0980, "close": 1.1030, "volume": 100},
    {"open": 1.1030, "high": 1.1080, "low": 1.1010, "close": 1.1060, "volume": 120},
    {"open": 1.1060, "high": 1.1090, "low": 1.1020, "close": 1.1040, "volume": 90},
]

sma = Indicator.sma(3)
ema = Indicator.ema(3)
macd = Indicator.macd(3, 6, 2)
rsi = Indicator.rsi(3)
atr = Indicator.atr(3)

print("Feeding candles...")

for raw in raw_candles:
    candle = Candle.from_json(json.dumps(raw))

    sma_val = sma.next_candle(candle)
    ema_val = ema.next_candle(candle)
    macd_val = macd.next_candle(candle)
    rsi_val = rsi.next_candle(candle)
    atr_val = atr.next_candle(candle)

    print(f"Candle close: {candle.close:.4f}")
    print(f"sma = {sma_val}")
    print(f"ema = {ema_val}")
    print(f"macd = {macd_val}")
    print(f"rsi = {rsi_val}")
    print(f"atr = {atr_val}")
    print()