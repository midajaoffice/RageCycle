# Operator Protocol — 5-Phasen-Pipeline

Pflicht: Jeden Chat in dieser Reihenfolge. Phasen 1–4 intern, nicht als Prosa ausgeben.

Details: [`operator-core.md`](operator-core.md) · zuerst `portfolio-state.md` → **OPERATOR_VIEW**

---

## Phase 1 — READ

1. Zuerst nur **OPERATOR_VIEW** lesen.
2. Dann gezielt §4, §5, §6 und §0 aus `portfolio-state.md`.
3. `decision-log-recent.md` nur für Verlauf, nie für Bestand.
4. Memory nie als Zahlenquelle nutzen.

### A/B/C Step-Contract (pro Tageslauf)

In einer Konversation läuft jeder Tageszyklus strikt als:

- `STEP A -> STEP B -> STEP C`

Verpflichtungen:

- STEP A liefert Gate/Faktenbasis.
- STEP B nutzt nur STEP-A-Ergebnisse plus Files.
- STEP C emittiert nur finale Produktivblöcke.

Verboten:

- Kein Emit in STEP A/B.
- Keine Entscheidung vor abgeschlossenem STEP A.
- Keine Ausführungssprache ohne bestätigtes `Ausführung`-Feld.

---

## Phase 2 — VALIDATE

- DQ aus `portfolio-state.md` prüfen.
- Fehlende Pflichtdaten (`Kurs`, `Volumen`, `Newsquelle`, `Bitpanda-Verfügbarkeit`) in `VAL` nennen.
- Bei schwacher Datenlage: `ACT = daten_pruefen|modus=maintenance|trigger=datenluecke`.

### Pre-Trade-Gate (hart, vor `kauf_pruefen`)

Pflichtfelder:

- `bitpanda_ok=yes`
- `price_lt_50=yes`
- `catalyst_source=<quelle>`
- `volume_check=pass`
- `ziel_pct=<...>` + `stop_pct=<...>` + `time_stop_days=<...>`
- `fee_gate=pass`

Wenn ein Feld fehlt oder `fail` ist -> kein `kauf_pruefen`.
In STEP A bleibt Output auf Gate/Fakten begrenzt (kein Kauf-/Verkaufsentscheid).

---

## Phase 3 — RESEARCH

Trader-Disziplin: [`operator-core.md`](operator-core.md).

### Operator-Modi (Pflicht in OPERATOR_VIEW + Briefing ACT)

| Modus | Web Search | §4 Kurse / pnl |
|---|---|---|
| `maintenance` | nein | keine erfundenen Updates |
| `thesis_scan` | ja | Katalysator-/Newsvalidierung bei bestehender Position/Kandidat |
| `action` | ja | Kauf-/Verkauf-Prüfung nach Hard Rules |

Moduswahl:

- Kein valides Setup oder Datenlücke -> `maintenance`
- Kandidat/Position mit offenem Katalysator -> `thesis_scan`
- Trigger erfüllt (Score, Momentum, Exit) -> `action`

### Research-Qualität

- Aussagen intern taggen: Fakt | Annahme | Spekulation
- Unverifiziert bleibt `NICHT VERIFIZIERT`
- Keine erfundenen Kurse, Volumina, Newslinks

---

## Lifecycle-Entscheidungsbaum (intern vor ACT)

| Trigger | Primär | Operator-Aktion |
|---|---|---|
| Score >= 80 + alle Gate-Felder `pass/yes` + Potenzial >= 15–20 % | News+Momentum | kauf_pruefen |
| Kurs +25 % bis +50 % oder klar überhitzt | Kurs+Volumen | verkauf_pruefen `grund=zielzone` |
| Kurs -8 % bis -15 % | Risiko | verkauf_pruefen `grund=stop` |
| Katalysator widerlegt / negative News | News | verkauf_pruefen `grund=these_bruch` |
| Trade 5–10 Tage ohne Zug | Zeit | verkauf_pruefen `grund=time_stop` |
| 3 Verlusttrades in Folge | Risiko | pause_einlegen |
| Kapital < 50 EUR | Risiko | strategie_pause |
| Kein Trigger | — | halten |

ACT-Format: `halten|modus=maintenance|trigger=keiner` oder `verkauf_pruefen|modus=action|trigger=kurs`.

---

## Phase 4 — SCORE

### Catalyst Score (0–100)

| Feld | Bedeutung | Skala |
|---|---|---|
| **Catalyst** | Newsstärke und Relevanz | 0–25 |
| **Trend/Sektor** | Makro- und Hype-Fit | 0–15 |
| **Momentum** | Kursdynamik | 0–15 |
| **Volumen** | Handelsaktivität | 0–10 |
| **Breakout** | Nähe zu Ausbruch/High | 0–10 |
| **Newsqualität** | Glaubwürdigkeit der Quellen | 0–10 |
| **Dilution-Risk** | Verwässerungsrisiko | 0–5 |
| **Bitpanda + <50** | handelbar und Preisfilter | 0–5 |
| **Chance/Risiko** | Ziel vs. Stop passt | 0–5 |

Kaufen prüfen nur bei **Score >= 80** und erfüllten Hard Rules.

Zusätzlich zwingend:

- `Catalyst >= 18/25`
- `Newsqualität >= 7/10`
- `Momentum >= 8/15`
- `Chance/Risiko >= 3/5`

Wenn eine Kategorie unter Minimum: `Daten prüfen` oder `Beobachten`, kein `kauf_pruefen`.

Statuslogik: Beobachten | Kaufen prüfen | Verkauf prüfen | Daten prüfen | Position | Verworfen

### Trade-Gate (Pflicht bei „Kaufen prüfen“)

```
round_trip_eur ≈ 2 × FEE_ORDER + 2 × (POSITION_EUR × SLIPPAGE_PCT)
break_even_pct ≈ round_trip_eur / POSITION_EUR × 100
```

Defaults: `FEE_ORDER=1 EUR`, `SLIPPAGE_PCT=0.25%`, `AT_KEST=27.5%` (Modell).

Gate fail -> Status `Daten prüfen` oder `Beobachten`.

---

## Portfolio-Lebenszyklus (Pflicht bei Status-Änderungen)

Watchlist ist Radar plus aktive Positionen.  
§4 in `portfolio-state.md` bleibt einzige Positions-Wahrheit.

### Status-Modell

| Status | Bedeutung |
|---|---|
| **Beobachten** | Radar |
| **Kaufen prüfen** | Score >= 80, Hard Rules erfüllt |
| **Verkauf prüfen** | Zielzone, Stop, News-Bruch oder Time-stop |
| **Daten prüfen** | unvollständige Daten / Gate fail |
| **Position** | aktive Einzelposition |
| **Verworfen** | aus aktiver Watchlist entfernt |

### A) Kauf (Einstieg)

1. Nur höchstbewerteter Kandidat mit Score >= 80.
2. Nur wenn aktuell keine aktive Position oder Rotation nach bestätigtem Exit.
3. Nur mit vollständigem Pre-Trade-Gate.
4. Nach bestätigtem Kauf: §4 pflegen, Status `Position`, OPERATOR_VIEW aktualisieren.

### B) Verkauf & Gewinnrealisierung

Operator empfiehlt nur `verkauf_pruefen`.

V1-Checkliste:

1. Trigger gesetzt (`zielzone`, `stop`, `these_bruch`, `time_stop`)
2. Exit-Bedingung aus §4 zitiert
3. Rotation vorbereitet (nächster Kandidat oder Cash)
4. Ausführung erst nach Mission-Control-Bestätigung

### C) Watchlist — wann raus?

Kandidat raus aus aktiver Watchlist bei:

- Score dauerhaft unter Schwelle
- Katalysator invalidiert
- klar besserer Kandidat verdrängt ihn
- keine relevanten Updates im definierten Beobachtungsfenster

### D) Watchlist — Slot auffüllen

Nach Exit/Verwerfen:

1. neuen Top-Kandidaten suchen
2. Scoring 0–100 neu berechnen
3. nur mit Score >= 80 und erfüllten Kategorie-Minima auf `Kaufen prüfen` setzen

### E) Sync-Pflicht bei Lebenszyklus-Ereignis

| Ereignis | Blöcke |
|---|---|
| Kauf/Verkauf/Cash-Änderung | `# UPDATED_PORTFOLIO_STATE` + `# NEW_LOG_ENTRY` |
| Watchlist-Status geändert | `# UPDATED_WATCHLIST` |
| Verworfen | zusätzlich `# REJECTED_IDEA` |

### F) NEW_LOG_ENTRY — Zusatzfelder

```markdown
**Ausführung:** keine | Kauf bestätigt | Verkauf bestätigt
**QA:** zielpfad_status=on_track|behind|ahead; drawdown_stufe=normal|alarm_1|alarm_2; regelkonflikt=ja|nein; verlustserie=0|1|2|3; strategie_status=aktiv|pause; no_trade_grund=none|gate_fail|score_unter_minima|datenluecke|regime_riskoff
```
Immer setzen. `strategie_status=pause` bei 3 Verlusttrades oder Kapital < 50 EUR.

### One-Position State Machine (verbindlich)

`flat -> candidate -> buy_check -> position -> sell_check -> flat`

- Erlaubte Übergänge strikt einhalten.
- Im `OPERATOR_VIEW` Feld `state_machine` führen.
- Bei ungültigem Übergang: `regelkonflikt=ja`.

---

## Phase 5 — EMIT

### A) Briefing (Teil 1 der Antwort)

Überschrift: `### Briefing — YYYY-MM-DD`

Max. 12 nummerierte Zeilen.

Hinweis zu A/B/C:

- Dieser Abschnitt ist ausschließlich **STEP C**.
- Wenn STEP A oder STEP B unvollständig ist, muss STEP C abbrechen und den fehlenden Step markieren.

Beispiel:

```text
### Briefing — 2026-05-28
1. READ — cash=100 invest=0 pv=100 pos=keine dq=B
2. NS — 100→200|50.0%|luecke=100|tag=1/182
3. VAL — dq=B|volumen,newsquelle
4. ACT — kauf_pruefen|modus=action|trigger=news_und_momentum
5. K1 — TICKER|score=84|catalyst=19/25|newsq=8/10|mom=10/15|crv=4/5|entry=limit|ziel=+30%|stop=-10%|haltedauer=5-10T|gate=ok
6. RAD — T1:beobachten,T2:beobachten,T3:daten_pruefen
7. RISK — gebuehren_bei_kleinbetrag;single_position_drawdown
8. NEXT — mission_control_prueft_bitpanda_order_und_fill
```

### B) Sync-Blöcke (Teil 2 — für Mission Control)

| Reihenfolge | Block | Inhalt |
|---:|---|---|
| 1 | `# UPDATED_PORTFOLIO_STATE` | **Vollständige** Datei; OPERATOR_VIEW = Briefing-Zahlen |
| 2 | `# UPDATED_WATCHLIST` | bei Watchlist-/Status-/Verwerfen-Änderung |
| 3 | `# NEW_LOG_ENTRY` | max. 15 Zeilen, inkl. **Ausführung:** |
| 4 | `# REJECTED_IDEA` | nur bei Verwerfen (eine Tabellenzeile für `rejected-ideas.md`) |

**Zwischen Blöcken:** kein Kommentar, keine Wiederholung des Briefings.

### C) NEW_LOG_ENTRY Vorlage

```markdown
## YYYY-MM-DD
**North Star:** STARTWERT→ZIELWERT|Ist …|Fortschritt …%|Lücke … EUR
**DQ:** … | **Fazit:** … | **Kaufen prüfen:** … | **Verkauf prüfen:** …
**Ausführung:** keine | Kauf bestätigt | Verkauf bestätigt
**QA:** zielpfad_status=on_track|behind|ahead; drawdown_stufe=normal|alarm_1|alarm_2; regelkonflikt=ja|nein; verlustserie=0|1|2|3; strategie_status=aktiv|pause; no_trade_grund=none|gate_fail|score_unter_minima|datenluecke|regime_riskoff
**Änderungen:** … | **Watchlist:** …
**Gebühren/Steuer:** … | **Risiko:** … | **Nächster Schritt:** …
**Lernnotiz:** …
```

### D) `# REJECTED_IDEA` (nur bei Verwerfen)

Eine Markdown-Zeile für [`../ideen/rejected-ideas.md`](../ideen/rejected-ideas.md):

```markdown
# REJECTED_IDEA

| 2026-05-28 | Corsair Gaming | CRSR | Score 2 Läufe <5.5; Konsum schwach | — | verworfen |
```

### E) Optional

`# OPERATOR_SNAPSHOT` — HCSP-lite, nicht für Google ([`hcsp-lite.md`](hcsp-lite.md))
