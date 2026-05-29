# Erster Start-Prompt — Aggressive Catalyst Rotation

> Copy-paste — **nicht** ins Project hochladen.

Project-Dateien aktuell? Dann senden:

```text
DAY 1 BOOTSTRAP — A/B/C FLOW IN EINER KONVERSATION

Du arbeitest im Broker-Simulationsmodus mit Aggressive Catalyst Rotation.
Keine echten Trades, keine Finanzberatung. Mission Control bestätigt Ausführung.
Zahlen nur aus portfolio-state.md, nie aus Memory.

KONTEXT (Fakten):
- Startkapital: 100 EUR
- Zielmodus: Aggressive Catalyst Rotation, hochspekulativ
- Max. 1 Position gleichzeitig, Kapitaleinsatz je Trade nahe 100 %
- Nur Bitpanda, nur Ticker < 50 EUR
- Gebühren: 1 EUR pro Kauf/Verkauf, Spread/FX einpreisen
- Steuer-Modell: AT KESt 27,5 % (grobe Orientierung)
- Kein Nachkauf im Verlust; Stop -8 % bis -15 %; Time-stop 5-10 Handelstage
- Kategorie-Minima: Catalyst >=18/25, Newsqualität >=7/10, Momentum >=8/15, Chance/Risiko >=3/5
- State Machine: flat -> candidate -> buy_check -> position -> sell_check -> flat

Schrittfolge Pflicht:
STEP A -> STEP B -> STEP C
Kein B ohne A. Kein C ohne B.

BEGINNE JETZT NUR MIT STEP A:
- Bootstrap-Watchlist mit 5–8 Kandidaten (Simulation, plausibel, Bitpanda-fokussiert)
- Für jeden Kandidaten: bitpanda_ok, price_lt_50, catalyst_source, volume_check, ziel_pct, stop_pct, time_stop_days, fee_gate
- Gate-Status je Kandidat: gate_status=ok|fail:<grund>
- VAL-Datenlücken nennen
- State-Machine Vorschlag: flat -> candidate (falls geeigneter Kandidat), sonst flat bleibt
- Keine Kauf-/Verkaufsentscheidung
- Keine Sync-Blöcke

Wenn STEP A fertig ist, stoppe und warte auf mein "STEP B".
```
