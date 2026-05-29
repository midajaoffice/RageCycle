# Decision Logic Redline — Aggressive Catalyst Rotation

Zweck: Widersprüche zwischen Altlogik und neuem Zielsystem auflösen, bevor Prompts/Protokoll synchronisiert werden.

## Redline-Liste

| Altregel / Altanker | Neuregel (verbindlich) | Betroffene Datei(en) | Risiko ohne Fix |
|---|---|---|---|
| Mehrpositions-Logik (`max 4`) | Single-Position-Logik (`max 1`) | `operator-core.md`, `operator-protocol.md`, `chatgpt-instructions.md`, `portfolio-state.md` | Strategie driftet in altes Verhalten |
| Story/Setup 1–10 als Primärfilter | Catalyst-Score 0–100, Kauf erst ab `>=80` | `operator-protocol.md`, `watchlist.md`, `daily-prompt.md` | Zu frühe Einstiege mit schwacher Edge |
| K1/K2-Mehrfachkäufe je Lauf | Nur ein Kaufkandidat pro Lauf (Rotation) | `operator-protocol.md`, `chatgpt-instructions.md` | Overtrading mit kleinem Kapital |
| Unklare Exit-Logik | Zielzone +25 bis +50, Stop -8 bis -15, Time-stop 5–10 Tage | `operator-core.md`, `operator-protocol.md`, `portfolio-state.md` | Verluste laufen lassen |
| DE-Steuer-Modell 26,375 % | AT-KESt-Modell 27,5 % (Hinweis, keine Beratung) | `operator-core.md`, `portfolio-state.md`, Log-Hinweise | falsche Netto-Erwartung |
| QA ohne Serien-/Pause-Status | QA erweitert um `verlustserie`, `strategie_status` | `operator-protocol.md`, Log-Dateien | fehlende Risikobremse |

## Single Source of Strategy

1. `portfolio-state.md` ist einzige Zahlenquelle.  
2. `operator-core.md` ist normative Regelquelle.  
3. `operator-protocol.md` steuert Pipeline/Output und bleibt schema-kompatibel.  
4. `daily-prompt.md` bleibt kompakt und verweist auf Core + Protocol.
