# Daily Prompt

Nutze pro Tag **eine** Project-Konversation und fahre die Schritte strikt in Reihenfolge:

1. STEP A senden und Ergebnis abwarten
2. STEP B senden und Ergebnis abwarten
3. STEP C senden und Sync-Blöcke übernehmen

## STEP A — Data & Gate Check

```text
STEP A — Data & Gate Check.

Lies zuerst OPERATOR_VIEW in portfolio-state.md (inkl. modus, positionen_detail), dann §4/§5/§6.
Zahlen nur aus portfolio-state.md, nie aus Memory.

Erstelle für jeden relevanten Kandidaten:
- bitpanda_ok=yes/no
- price_lt_50=yes/no
- catalyst_source=<Quelle oder FEHLT>
- volume_check=pass/fail
- ziel_pct, stop_pct, time_stop_days
- fee_gate=pass/fail

Nenne VAL-Datenlücken und markiere je Kandidat gate_status=ok|fail:<grund>.
Erlaube in STEP A keine Kauf-/Verkaufsentscheidung und keine Sync-Blöcke.
Wenn STEP A abgeschlossen ist, stoppe und warte auf "STEP B".
```

## STEP B — Score & Decision

```text
STEP B — Score & Decision.

Nutze nur STEP-A-Ergebnisse + File-Daten.
Regeln:
- Score >= 80 Pflicht
- Kategorie-Minima: Catalyst >=18/25, Newsqualität >=7/10, Momentum >=8/15, Chance/Risiko >=3/5
- Kein kauf_pruefen bei Gate-Fail oder Minima-Fail
- State Machine strikt: flat -> candidate -> buy_check -> position -> sell_check -> flat

Liefere:
- Scoring je Top-Kandidat
- Entscheidung: kauf_pruefen | verkauf_pruefen | halten
- no_trade_grund falls kein Trade
- vorgeschlagener nächster state_machine-Übergang

Keine Sync-Blöcke in STEP B. Stoppe und warte auf "STEP C".
```

## STEP C — Emit & Sync

```text
STEP C — Emit & Sync.

Erzeuge jetzt ausschließlich:
1) ### Briefing — YYYY-MM-DD (max. 12 Zeilen; ACT mit modus= und trigger=)
2) # UPDATED_PORTFOLIO_STATE (vollständig)
3) # UPDATED_WATCHLIST (nur bei Status-/Positions-/Verwerfen-Änderung)
4) # NEW_LOG_ENTRY (max. 15 Zeilen, inkl. Ausführung: keine|Kauf bestätigt|Verkauf bestätigt + QA: zielpfad_status|drawdown_stufe|regelkonflikt|verlustserie|strategie_status|no_trade_grund)
5) # REJECTED_IDEA (nur bei Verwerfen)

Keine Einleitung, keine Links im Briefing, keine Regelwiederholung, kein „ich habe gekauft/verkauft“.
```
