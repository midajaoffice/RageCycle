# Decision Logic Redline — 2x in 6 Monaten

Zweck: Widersprüche zwischen Altlogik und neuem Zielsystem auflösen, bevor Prompts/Protokoll synchronisiert werden.

## Redline-Liste

| Altregel / Altanker | Neuregel (verbindlich) | Betroffene Datei(en) | Risiko ohne Fix |
|---|---|---|---|
| North Star `500→5000`, `10×`, `12 Monate`, `tag x/365` | North Star wird aus `portfolio-state.md` gelesen; aktuell `4.148,25→8.296,50`, `2×`, `182 Tage`, `tag x/182` | `chatgpt-instructions.md`, `chatgpt/operator-core.md`, `chatgpt/operator-protocol.md` | Widersprüchliche Briefings und falscher Zielpfad |
| Beispiel-NS in Briefing-Vorlagen auf 10×/365 | Beispiele auf 2×/182 oder neutrales Platzhalterformat | `chatgpt/operator-protocol.md`, `chatgpt-instructions.md` | Modell übernimmt falsche Anchors aus Beispielen |
| Trigger nur `pnl<=-15%` / `pnl>=+30%` | ETF-Core-Regime: Drawdown-Stufen + relative Performance + News/These; PnL-Schwellen nur optionaler Zusatz | `chatgpt/operator-protocol.md`, `chatgpt-instructions.md`, `anleitung/daily-prompt.md` | Unterreaktion bei Regimewechsel oder Überreaktion bei ETF-Schwankung |
| Positionsgrößen für 500€-Mikrotickets | Prozent-/Risikobudget-Logik für reales Portfolio (`portfolio-state.md` maßgeblich) | `chatgpt/operator-protocol.md`, `chatgpt/operator-core.md` | Regelwerk passt nicht zum tatsächlichen Depot |
| Harte Min-Cash-Regel 20 % ohne Override | Cash-Regel bleibt Standard, aber temporärer Override bei dokumentierter Zielstrategie erlaubt | `chatgpt/operator-core.md`, `chatgpt/operator-protocol.md` | System meldet permanent Regelbruch ohne Handlungsanleitung |
| Wöchentliche Aktion primär „Freitag“ | `action` bei Trigger-Ereignis (Drawdown-Stufe, Rebalance-Schwelle, Event), nicht primär kalendarisch | `chatgpt/operator-core.md`, `anleitung/daily-prompt.md` | Verzögerte Reaktion trotz klarer Signale |
| `NEW_LOG_ENTRY` ohne feste QA-Felder | QA-Mikroformat mit `zielpfad_status`, `drawdown_stufe`, `regelkonflikt` | `chatgpt/operator-protocol.md`, `chatgpt-instructions.md`, Log-Dateien | Schwache Nachvollziehbarkeit und Drift |

## Single Source of Strategy

1. `portfolio-state.md` ist einzige Zahlenquelle und enthält operative Schwellen in §6.  
2. `operator-core.md` ist normative Regelquelle (Interpretation, Priorität, Risiko).  
3. `operator-protocol.md` steuert Pipeline/Output, ohne eigene widersprüchliche Strategiewerte.  
4. `daily-prompt.md` bleibt kompakt und verweist auf Core + Protocol.
