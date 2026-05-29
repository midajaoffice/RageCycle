# Daily Prompt

Nutze pro Tag **eine** Project-Konversation und fahre die Schritte strikt in Reihenfolge:

1. STEP A senden und Ergebnis abwarten
2. STEP B senden und Ergebnis abwarten
3. STEP C senden und Sync-Blöcke übernehmen

## STEP A — Data & Gate Check (Web-augmented)

```text
STEP A — Data & Gate Check (web-augmented).

Lies zuerst OPERATOR_VIEW in portfolio-state.md (inkl. modus, positionen_detail), dann §4/§5/§6.

Datenhierarchie (strikt):
- Aus portfolio-state.md NUR: Cash, PV, investiert, Positionen, state_machine, Scores/Status aus §5, offene Prüfpunkte.
- Nie aus Memory für Bestand/Kapital.
- Web Search in STEP A ist PFLICHT (auch bei modus=maintenance): aktuelle Kurse, Newsquellen, Volumen vs Referenz.

Für jeden Kandidaten in §5 recherchieren und ausgeben:
- price_eur=<Wert oder FEHLT> (USD nur mit FX-Hinweis)
- price_lt_50=yes/no (aus recherchiertem Kurs)
- catalyst_source=<Quellenname + Kurzbeleg; Link in STEP A erlaubt>
- volume_check=pass/fail (aktuell vs Referenz-Durchschnitt; bei Widerspruch: fail)
- ziel_pct, stop_pct, time_stop_days (FEHLT ok in STEP A; STEP B setzt Strategie-Defaults)
- fee_gate=pass/fail (nur wenn Ziel/Stop gesetzt, sonst fail:parameter_fehlt)
- gate_status=ok|fail:<grund>
- Markiere Web-Fakten mit Tag external: wo nicht aus File.

Kein bitpanda_ok — Bitpanda-Verfügbarkeit ist kein Gate mehr.
Keine Kauf-/Verkaufsentscheidung, keine Sync-Blöcke.
Wenn STEP A abgeschlossen ist, stoppe und warte auf "STEP B".
```

## STEP B — Score & Decision

```text
STEP B — Score & Decision.

Nutze STEP-A-Ergebnisse (inkl. Web-Kurse/Quellen/Volumen) + File-Daten.
Regeln:
- Score >= 80 Pflicht
- Kategorie-Minima: Catalyst >=18/25, Newsqualität >=7/10, Momentum >=8/15, Chance/Risiko >=3/5
- Kein kauf_pruefen bei Gate-Fail oder Minima-Fail
- Für Top-2-Kandidaten: ziel_pct/stop_pct/time_stop_days aus §3-Defaults setzen (+25% / -10% / 7T), wenn STEP A FEHLT hatte
- State Machine strikt: flat -> candidate -> buy_check -> position -> sell_check -> flat

Liefere:
- Scoring je Top-Kandidat (ohne Bitpanda-Spalte; Preisfilter <50 EUR separat)
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
