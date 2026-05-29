# Portfolio State

**Letztes Update:** 2026-05-28
**Datenqualität:** B
**Modus:** Aggressive Catalyst Rotation / Research-Unterstützung

> **Einzige Quelle der Wahrheit** für Bestand, Cash und Kurse. ChatGPT Memory zählt nicht.

---

## OPERATOR_VIEW

> Operator: **zuerst nur diesen Block lesen.** Bei jedem Update vollständig aktualisieren.

```
north_star: 100→200|EUR|fortschritt:50.0%|luecke:100|tag:0/182|ziel_datum:2026-11-24
kapital: cash=100|investiert=0|pv=100|dq=B
modus: maintenance
state_machine: candidate
step_status: step_a=ok|step_b=ok|step_c=ok
positionen: keine
positionen_detail: keine_aktive_position|candidate=NIO|score=75|next=bitpanda_app_und_intraday_volumen_pruefen
watchlist_top: NIO
letzte_entscheidung: halten|score_unter_80|2026-05-28
gebuehren_modell: 1EUR/order|0.25pct_slippage|steuer_modell:27.5pct_AT
```

**Felder:** `modus` = maintenance | thesis_scan | action. `state_machine` = flat|candidate|buy_check|position|sell_check. `step_status` = step_a|step_b|step_c als offen|ok je Tageslauf. `positionen_detail` enthält Trigger- und Nächster-Schritt-Status.

---

## 0. North Star

| Feld                            | Wert                                   |
| ------------------------------- | -------------------------------------- |
| **Starsumme (Startkapital)**    | **100 EUR**                            |
| **Startdatum North Star**       | **2026-05-25**                         |
| **Zielhorizont**                | bis **2026-11-24**                     |
| **Ziel-Multiple**               | **2×** ohne Hebel                      |
| **Zielwert (TARGET_VALUE_EUR)** | **200 EUR**                            |
| **Aktueller Fortschritt %**     | **50,0 %** (100 ÷ 200)                 |
| **Lücke bis Ziel (EUR)**        | **100 EUR**                            |
| **Erforderliche Gesamtrendite** | +100 % in 6 Monaten, hoch ambitioniert |

### Kosten- & Steuer-Modell

| Feld                       | Wert                          |
| -------------------------- | ----------------------------- |
| Broker-Modell              | Bitpanda Real Stocks/ETFs     |
| Gebühr pro Order           | 1,00 EUR                      |
| Slippage-Annahme pro Seite | 0,25 %                        |
| Steuersatz Modell AT       | 27,5 % KESt                   |
| Steuer-Hinweis             | Modellannahme, keine Beratung |

---

## 1. Mission

Spekulatives Modellportfolio von 100 EUR mit schneller Catalyst-Rotation handeln. Fokus auf einzelne High-Conviction-Setups statt Diversifikation. North Star priorisiert, garantiert nichts.

**Erlaubt:** Aktien, ETFs, Rohstoff-ETPs/ETCs — Xetra, Frankfurt, NYSE, NASDAQ, Euronext
**Ausgeschlossen:** Krypto, Forex, CFDs, Optionen, Hebelprodukte, illiquide/unregulierte Märkte.

---

## 2. Kapital

| Feld                                |                                                                                                Wert |
| ----------------------------------- | --------------------------------------------------------------------------------------------------: |
| Startkapital                        |                                                                                                 100 |
| Aktueller geschätzter Portfoliowert |                                                                                                 100 |
| Verfügbares Cash                    |                                                                                                 100 |
| Investiertes Kapital                |                                                                                                   0 |
| Nicht verifizierte Werte            | Kandidaten-News, Bitpanda-App-Verfügbarkeit, Intraday-Volumen, finaler Spread/Fractional-Ausführung |

---

## 3. Portfolio-Regeln

* Keine echten Trades ohne menschliche Bestätigung.
* Max. **1** gleichzeitige Position in §4.
* Pro Trade nahezu **100 %** des verfügbaren Kapitals.
* Nur Bitpanda-Ticker mit Kurs **unter 50 EUR**.
* Kauf nur bei Score **>=80** und frischem Katalysator.
* Kein Trade mit Potenzial unter **15–20 %** (bevorzugt >=25 %).
* Stop-Loss **-8 % bis -15 %** vorab definieren.
* Time-stop: Exit, wenn Trade nach **5–10 Handelstagen** nicht trägt.
* Kein Nachkaufen im Verlust.
* Nach **3 Verlusttrades** in Folge: 1 Tag Pause.
* Bei Kapital **unter 50 EUR**: Strategie pausieren und neu bewerten.

---

## 4. Aktuelle Positionen

| Asset | Ticker | Markt | Kaufdatum | Kaufkurs | Aktueller Kurs | Positionsgröße | Positionswert | These | Katalysator | Trigger-Typ | Nächstes Event | Stop/Exit | Status | DQ |
| ----- | ------ | ----- | --------- | -------: | -------------: | -------------: | ------------: | ----- | ----------- | ----------- | -------------- | --------- | ------ | -- |
| Keine | —      | —     | —         |        — |              — |              — |             — | —     | —           | —           | —              | —         | Keine  | B  |

---

## 5. Watchlist-Zusammenfassung

| Asset              | Ticker | Markt  | Thema                           | Katalysator                                                         | Risiko                                        | Score | Status       | Nächster Prüfpunkt                                                                    |
| ------------------ | ------ | ------ | ------------------------------- | ------------------------------------------------------------------- | --------------------------------------------- | ----: | ------------ | ------------------------------------------------------------------------------------- |
| NIO                | NIO    | NYSE   | EV / China / Overseas Push      | ES9-/Overseas-Push, April-Lieferungen +22,8 % YoY, hohes Volumen    | EV-Wettbewerb, China-Makro, ADR-Risiko        |    75 | Beobachten   | Score >=80 nur bei stärkerem Momentum/Breakout; Bitpanda-App und Volumen final prüfen |
| Rigetti Computing  | RGTI   | NASDAQ | Quantum Computing               | LOI mit U.S. Commerce für bis zu 100 Mio. USD Quantum-R&D-Förderung | Bitpanda-App-Check offen, Verwässerungsrisiko |    77 | Daten prüfen | Bitpanda-App-Verfügbarkeit und finalen Volumencheck prüfen                            |
| SoundHound AI      | SOUN   | NASDAQ | Voice AI / KI                   | Q1-Umsatz +52 % YoY, FY26-Outlook bestätigt                         | Bitpanda-App-Check offen, KI-Multiple-Risiko  |    73 | Daten prüfen | Bitpanda-App-Verfügbarkeit prüfen                                                     |
| Riot Platforms     | RIOT   | NASDAQ | Bitcoin Mining / AI Data Center | Q1-/Data-Center-Shift, AMD Capacity-Option                          | Intraday-Volumen offen, BTC-Korrelation       |    65 | Daten prüfen | Intraday-Volumen gegen 50T-Avg prüfen                                                 |
| Archer Aviation    | ACHR   | NYSE   | eVTOL / Defense / Aviation      | FAA-/Midnight-Zertifizierung, Defense-/Partnerstory                 | Bitpanda-App-Check offen, Kapitalbedarf       |    66 | Daten prüfen | Bitpanda-App-Verfügbarkeit prüfen                                                     |
| D-Wave Quantum     | QBTS   | NYSE   | Quantum Computing               | U.S.-Förderpaket / Quantum-Funding-Story                            | Bitpanda-App-Check und Volumen offen          |    62 | Daten prüfen | Bitpanda-App und Volumencheck prüfen                                                  |
| Intuitive Machines | LUNR   | NASDAQ | Space / Lunar Infrastructure    | Lunar-Reconnaissance/Q1-Backlog, aber NASA-Rover-Negativkatalysator | Katalysator gemischt, Volumen offen           |    54 | Beobachten   | Nur bei klarer positiver Newsqualität neu prüfen                                      |
| DroneShield        | DRO    | ASX    | Counter-Drone / Defense         | Counter-drone-Nachfrage und Pipeline                                | ASIC-Probe, Volumen offen, Risk-Event         |    58 | Beobachten   | Risk-Event und Volumen klären                                                         |

---

## 6. Offene Prüfpunkte

- Bitpanda-App-Verfügbarkeit für RGTI, SOUN, QBTS, LUNR und ACHR prüfen.
- Intraday-Volumen für RIOT, DRO, QBTS und LUNR gegen Referenzvolumen prüfen.
- NIO nur als Kandidat beobachten; kein `buy_check`, solange Score unter 80 bleibt.
- Finalen EUR-Preis, Spread, Fractional-Ausführung und Ordergültigkeit vor jedem `buy_check` prüfen.

---

## 7. Bekannte Unsicherheiten

* DQ **B**: Markt-/Newsdaten teils zeitverzögert.
* Catalyst-Score ist heuristisch und kann schnell kippen.
* Gebühren/Steuer sind Modellannahmen.
* Bitpanda-Verfügbarkeit wurde browserseitig nicht für alle Kandidaten verifiziert.
* Kein Broker-Fill, kein Real-Order-Preview und keine echte Ausführung bestätigt.

---

## 8. Letzte Änderungen

* 2026-05-28: Clean-Slate-Reset durchgeführt (keine Positionen, Watchlist geleert).
* 2026-05-28: STEP A/B/C abgeschlossen; Watchlist mit 8 Kandidaten neu aufgebaut; NIO als `candidate`/Top-Beobachtung gesetzt; keine Kaufprüfung, keine Ausführung.
