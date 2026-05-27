# Portfolio State

**Letztes Update:** 2026-05-27
**Datenqualität:** A-
**Modus:** Reales Broker-Portfolio / Bestandsführung

> **Einzige Quelle der Wahrheit** für Bestand, Cash und Kurse. ChatGPT Memory zählt nicht.

---

## OPERATOR_VIEW

> Operator: **zuerst nur diesen Block lesen.** Bei jedem Update vollständig aktualisieren.

```
north_star: 4148.25→8296.50|EUR|fortschritt:50.0%|luecke:4148.25|tag:1/182|ziel_datum:2026-11-27
kapital: cash=0|investiert=4148.25|pv=4148.25|dq=A-
modus: maintenance
positionen: IE00063FT9K6,IE00B53SZB19
positionen_detail: IE00063FT9K6 pnl=0.08% trigger_kurs=ok trigger_news=copper_miners next=rohstoffzyklus_update|IE00B53SZB19 pnl=28.71% trigger_kurs=ok trigger_news=nasdaq_earnings next=makro_us_rates
watchlist_top: IE00B53SZB19,IE00063FT9K6
letzte_entscheidung: framework|6m_2x_execution_regeln_aktiviert|2026-05-27
gebuehren_modell: broker_real_export|steuer_modell:26.375pct_DE
```

**Felder:** `modus` = maintenance | thesis_scan | action (MC setzt vor Chat, siehe `anleitung/mc-datenritual.md`). `positionen_detail` — MC: pnl, next; Operator: trigger_kurs, trigger_news.

---

## 0. North Star

| Feld | Wert |
|---|---|
| **Starsumme (Startkapital)** | **4.148,25 EUR** |
| **Startdatum North Star** | **2026-05-27** |
| **Zielhorizont** | bis **2026-11-27** |
| **Ziel-Multiple** | **2×** in 6 Monaten |
| **Zielwert (TARGET_VALUE_EUR)** | **8.296,50 EUR** |
| **Aktueller Fortschritt %** | **50,0 %** (4.148,25 ÷ 8.296,50) |
| **Lücke bis Ziel (EUR)** | **4.148,25 EUR** |
| **Erforderliche Gesamtrendite** | +100 % in 6 Monaten (sehr ambitioniert) |

### Kosten- & Steuer-Modell

| Feld | Wert |
|---|---|
| Broker-Modell | Reales Broker-Depot (CSV-Export) |
| Gebühr pro Order | 1,00 EUR |
| Slippage-Annahme pro Seite | 0,25 % |
| Steuersatz Modell DE | 26,375 % |
| Freistellungsauftrag | 1.000 EUR/Jahr |
| Kirchensteuer | nein |

---

## 1. Mission

Reales Broker-Portfolio wird als operative Basis geführt. North Star ist ab sofort: Portfolio in 6 Monaten verdoppeln (4.148,25 EUR auf 8.296,50 EUR); Bestand und Kurse werden aus Broker-Exporten übernommen.

**Erlaubt:** Aktien, ETFs, Rohstoff-ETPs/ETCs — Xetra, Frankfurt, NYSE, NASDAQ, Euronext  
**Ausgeschlossen:** Krypto, Forex, CFDs, Optionen, Hebelprodukte, illiquide/unregulierte Märkte.

---

## 2. Kapital

| Feld | Wert |
|---|---:|
| Startkapital | 500 |
| Aktueller geschätzter Portfoliowert | 4.148,25 |
| Verfügbares Cash | 0 |
| Investiertes Kapital | 4.148,25 |
| Nicht verifizierte Werte | Cashbestand nicht separat im Export ausgewiesen |

---

## 3. Portfolio-Regeln

- Keine echten Trades ohne menschliche Bestätigung.
- Max. **4** gleichzeitige Positionen in §4.
- Min. **20 %** Cash-Reserve am PV (Standard; temporärer Override nur mit Log-Begründung).
- Keine Position über 30 % des Portfolios (Standard; temporärer Override nur für dokumentierten Rebalance-Pfad).
- Hype-Ideen maximal 5–10 %, normale Spekulationen 10–20 % (nur für neue Satelliten-Ideen, nicht für bestehende Kern-ETFs).
- Keine Nachkäufe aus Hoffnung.
- Jede Position braucht These, Katalysator und **Exit-Kriterium** (Stop/These in §4).
- **Gewinnmitnahme:** optional prüfen; bei ETF-Core primär Rebalancing-/Risikostufen aus §6 nutzen.
- Keine Kaufprüfung ohne aktuelle Kursprüfung.
- Watchlist-Radar: **5–8** Namen (Beobachten/Kaufen prüfen); Verworfenes → `ideen/rejected-ideas.md`.
- Lebenszyklus-Details: `chatgpt/operator-protocol.md` → **Portfolio-Lebenszyklus**.
- Jede neue Allokationsentscheidung muss auf das 6-Monats-Ziel einzahlen (Renditepotenzial vs. Drawdown-Risiko explizit dokumentieren).
- Bei aktivem Regelkonflikt (Cash/Positionsgewicht) gilt: keine Risikoerhöhung bis Rückkehr in Standardgrenzen oder dokumentierter MC-Override.

---

## 4. Aktuelle Positionen

| Asset | Ticker | Markt | Kaufdatum | Kaufkurs | Aktueller Kurs | Positionsgröße | Positionswert | These | Katalysator | Trigger-Typ | Nächstes Event | Stop/Exit | Status | DQ |
|---|---|---|---|---:|---:|---:|---:|---|---|---|---|---|---|---|
| iShares Copper Miners UCITS ETF | IE00063FT9K6 | Direkthandel | 2026-05-27 | 9,5445 EUR | 9,552 EUR | 2.872,88 EUR | 2.875,15 | Kupferminen-Exposure als Rohstoff-/Elektrifizierungs-Beta | Kupferpreiszyklus, Minenmargen | Beides | Rohstoffzyklus / China-Nachfrage | Verkauf prüfen bei Trendbruch Kupfer + strukturellem Underperformance-Regime | Offen | A- |
| iShares Nasdaq 100 UCITS ETF (Acc) | IE00B53SZB19 | Direkthandel | 2026-05-27 | 1.149,2442 EUR | 1.479,20 EUR | 989,12 EUR | 1.273,10 | Breites US-Tech-Momentum mit Qualitätsfokus | US-Earnings, AI-Capex-Zyklus | Beides | US-Makro / Earnings-Saison | Verkauf prüfen bei klarer Regimewende Growth/Tech oder Risikoabbau nötig | Offen | A- |

---

## 5. Watchlist-Zusammenfassung

| Asset | Ticker | Markt | Thema | Katalysator | Risiko | Story | Setup | Score | Status | Nächster Prüfpunkt |
|---|---|---|---|---|---|---:|---:|---:|---|---|
| iShares Nasdaq 100 UCITS ETF (Acc) | IE00B53SZB19 | Direkthandel | US-Tech-Beta | US-Earnings, AI-Capex, Fed-Pfad | Bewertungs-/Makro-Risiko | 7.0 | 7.0 | 7.0 | Position | Earnings + Fed-Tonlage prüfen |
| iShares Copper Miners UCITS ETF | IE00063FT9K6 | Direkthandel | Rohstoffe/Kupferminen | Kupferpreis, China-Nachfrage, Minenmargen | Zyklizität/China-Risiko | 6.6 | 6.6 | 6.6 | Position | Kupfer-Trend + China-Daten prüfen |
| AST SpaceMobile | ASTS | NASDAQ | Space/Satcom | 2026 Revenue Guidance, FCC, Satelliten-Ramp | Launch-/Capex-Risiko | 6.6 | 6.6 | 6.6 | Beobachten | BlueBird-Launch-Kadenz prüfen |
| Red Cat | RCAT | NASDAQ | Defense/Drohnen | Army/SRR, Q1 Umsatzsprung | Earnings-Miss, Margen | 6.5 | 6.5 | 6.5 | Beobachten | Q2 Margen/Army-Deliveries |
| Kratos Defense | KTOS | NASDAQ | Defense/Unmanned | Q1 Wachstum, Guidance erhöht | hohe Bewertung | 6.4 | 6.4 | 6.4 | Beobachten | neue Contracts/Backlog |
| Super Micro | SMCI | NASDAQ | KI-Infrastruktur | AI-Server-Umsatz, FY26 Sales-Guidance | Cashflow/Review/Margen | 6.2 | 6.2 | 6.2 | Beobachten | Cashflow + Export-Control-Review |
| Vertiv | VRT | NYSE | KI-Infrastruktur | Data-center sales +30 %, Guidance erhöht | Preis > 150 € ohne Fractionals, Bewertung | 6.1 | 6.1 | 6.1 | Daten prüfen | Fractional möglich? Bewertung prüfen |
| Corsair Gaming | CRSR | NASDAQ | Gaming/Hardware | Q1 Umsatz +10 %, profitabler Turnaround | Konsum/PC-Zyklus | 5.8 | 5.8 | 5.8 | Beobachten | Gaming-Hardware-Nachfrage |

---

## 6. 6-Monats-Execution-Framework (2x-Ziel)

### 6.1 Risikobudget

| Regel | Schwelle |
|---|---|
| Max. Portfolio-Drawdown vom letzten Hoch | **-12 %** |
| Alarmstufe 1 (Risiko reduzieren) | bei **-8 %** Drawdown |
| Alarmstufe 2 (Defense-Modus) | bei **-12 %** Drawdown |
| Max. Einzelpositionsgewicht | **70 %** vom PV |
| Ziel-Exposure (investiert) | **80–100 %** je nach Regime |

### 6.2 Rebalancing-Logik (wöchentlich)

| Situation | Aktion |
|---|---|
| IE00B53SZB19 Outperformance > 15 %-Punkte vs. IE00063FT9K6 | 5–10 %-Punkte in Underperformer umschichten (nur wenn Trend intakt) |
| IE00063FT9K6 Outperformance > 15 %-Punkte vs. IE00B53SZB19 | 5–10 %-Punkte in Underperformer umschichten (nur wenn Trend intakt) |
| Beide Trends intakt (keine Alarmstufe) | Zielmix **60/40 bis 70/30** (Nasdaq/Copper) halten |
| Alarmstufe 1 aktiv | Risiko um **10–20 %** senken (Teilgewinne/leichte Cash-Quote) |
| Alarmstufe 2 aktiv | Defense-Modus: Risiko deutlich senken, bis Drawdown < -8 % |

### 6.3 Exit- und Gewinnsicherungsregeln

- **Trendbruch-Regel:** Zwei schwache Wochen in Folge + Makro-/Themenbruch -> Verkauf prüfen.
- **Trailing-Ansatz:** Nach starken Anstiegen Teilgewinn realisieren, Restposition mit engem Review weiterlaufen lassen.
- **Keine Hoffnungstrades:** Verlierer nicht aufstocken, wenn These/Regime schwächer wird.
- **Re-Entry nur mit Trigger:** Rückkauf erst bei bestätigter Trendstabilisierung.

### 6.4 Operativer Rhythmus

- **Wöchentlich (Pflicht):** Performance Delta der zwei Positionen, Drawdown-Stufe, Zielpfad-Check.
- **Monatlich (Pflicht):** Zielpfad vs. Ist (2x in 182 Tagen), ggf. Risiko neu kalibrieren.
- **Event-basiert:** Fed, CPI, große US-Earnings, China-/Kupferdaten -> außerplanmäßige Prüfung.

### 6.5 Offene Prüfpunkte

- Cashbestand separat aus Broker-App bestätigen (CSV zeigt nur Positionswerte).
- Für IE00063FT9K6 und IE00B53SZB19 Börsenkürzel im Broker eindeutig dokumentieren.
- Prüfen, ob Warrant-/Restpositionen bewusst ausgeschlossen bleiben.
- **Ohne neuen Broker-Export:** Operator bleibt in `modus: maintenance` (kein erfundenes pnl). Ritual: [`anleitung/mc-datenritual.md`](../anleitung/mc-datenritual.md).

---

## 7. Bekannte Unsicherheiten

- Portfolio auf zwei ETF-Positionen aus Broker-CSV reduziert; Intraday kann bis zum nächsten Export abweichen.
- DQ **A-**: Werte stammen aus Broker-Export, Cash separat noch offen.
- PV basiert auf ausgewiesenem Kurswert der zwei übernommenen Positionen.
- Verdopplung in 6 Monaten ist sehr ambitioniert und keine Garantie.
- Steuer bleibt Modellannahme; Brokerdaten selbst sind Echtbestand.

---

## 8. Letzte Änderungen

- 2026-05-27: Wechsel auf reales Broker-Portfolio; RKLB/UEC entfernt, IE00063FT9K6 + IE00B53SZB19 als Bestand übernommen; PV auf 4.148,25 EUR gesetzt.
- 2026-05-27: North Star auf neues Ziel gesetzt: 2× in 6 Monaten (4.148,25 EUR -> 8.296,50 EUR bis 2026-11-27).
- 2026-05-27: 6-Monats-Execution-Framework ergänzt (Risikobudget, Rebalancing, Exit- und Review-Rhythmus).
- 2026-05-26: RKLB (125 EUR) und UEC (100 EUR) gekauft; Cash 273 EUR; 2× 1 EUR Gebühr.
- 2026-05-25: Ursprungsportfolio; Watchlist mit 8 Kandidaten; RKLB/UEC „Kaufen prüfen“, keine Positionen.
