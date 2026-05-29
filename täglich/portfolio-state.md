# Portfolio State

**Letztes Update:** 2026-05-29
**Datenqualität:** B
**Modus:** Aggressive Catalyst Rotation / Research-Unterstützung

> **Einzige Quelle der Wahrheit** für Bestand, Cash und Kurse. ChatGPT Memory zählt nicht.

---

## OPERATOR_VIEW

> Operator: **zuerst nur diesen Block lesen.** Bei jedem Update vollständig aktualisieren.

```
north_star: 100→200|EUR|fortschritt:50.0%|luecke:100|tag=4/182|ziel_datum:2026-11-24
kapital: cash=100|investiert=0|pv=100|dq=B
modus: maintenance
state_machine: candidate
step_status: step_a=ok|step_b=ok|step_c=ok
positionen: keine
positionen_detail: keine_aktive_position|candidate=NIO|score=75|next=mc_prueft_intraday_volumen_RGTI_NIO_und_order_preview_nur_bei_score_>=80
watchlist_top: NIO
letzte_entscheidung: halten|score_unter_80_gate_fail|2026-05-29
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

| Feld                                |                                                                          Wert |
| ----------------------------------- | ----------------------------------------------------------------------------: |
| Startkapital                        |                                                                           100 |
| Aktueller geschätzter Portfoliowert |                                                                           100 |
| Verfügbares Cash                    |                                                                           100 |
| Investiertes Kapital                |                                                                             0 |
| Nicht verifizierte Werte            | Finaler Order-Preview, Spread/Fractional-Ausführung (nur MC bei echtem Trade) |

---

## 3. Portfolio-Regeln

* Keine echten Trades ohne menschliche Bestätigung.
* Max. **1** gleichzeitige Position in §4.
* Pro Trade nahezu **100 %** des verfügbaren Kapitals.
* Nur Ticker mit recherchiertem Kurs **unter 50 EUR** (STEP A: Web Search).
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

| Asset              | Ticker | Markt  | Thema                           | Katalysator                                                         | Risiko                                         | Score | Status       | Nächster Prüfpunkt                                                          |
| ------------------ | ------ | ------ | ------------------------------- | ------------------------------------------------------------------- | ---------------------------------------------- | ----: | ------------ | --------------------------------------------------------------------------- |
| NIO                | NIO    | NYSE   | EV / China / Overseas Push      | ES9-/Overseas-Push, April-Lieferungen +22,8 % YoY, hohes Volumen    | EV-Wettbewerb, China-Makro, ADR-Risiko         |    75 | Beobachten   | Score >=80; Ziel/Stop/Time-stop setzen; finaler Order-Preview vor buy_check |
| Rigetti Computing  | RGTI   | NASDAQ | Quantum Computing               | LOI mit U.S. Commerce für bis zu 100 Mio. USD Quantum-R&D-Förderung | Verwässerungsrisiko, Volumen schwach           |    77 | Daten prüfen | Volumencheck; Ziel/Stop/Time-stop; Score-Minima                             |
| SoundHound AI      | SOUN   | NASDAQ | Voice AI / KI                   | Q1-Umsatz +52 % YoY, FY26-Outlook bestätigt                         | KI-Multiple-Risiko, Volumen unter Durchschnitt |    73 | Daten prüfen | Volumen/Momentum; Score-Minima                                              |
| Riot Platforms     | RIOT   | NASDAQ | Bitcoin Mining / AI Data Center | Q1-/Data-Center-Shift, AMD Capacity-Option                          | Intraday-Volumen schwach, BTC-Korrelation      |    65 | Daten prüfen | Volumen gegen 50T-Avg; Catalyst-Minima                                      |
| Archer Aviation    | ACHR   | NYSE   | eVTOL / Defense / Aviation      | FAA-/Midnight-Zertifizierung, Defense-/Partnerstory                 | Kapitalbedarf, CRV offen                       |    66 | Daten prüfen | Ziel/Stop/Time-stop; Score-Minima                                           |
| D-Wave Quantum     | QBTS   | NYSE   | Quantum Computing               | U.S.-Förderpaket / Quantum-Funding-Story                            | Volumen schwach                                |    62 | Daten prüfen | Volumencheck; Catalyst-Minima                                               |
| Intuitive Machines | LUNR   | NASDAQ | Space / Lunar Infrastructure    | Lunar-Reconnaissance/Q1-Backlog, aber NASA-Rover-Negativkatalysator | Katalysator gemischt, Volumen offen            |    54 | Beobachten   | Nur bei klarer positiver Newsqualität neu prüfen                            |
| DroneShield        | DRO    | ASX    | Counter-Drone / Defense         | Counter-drone-Nachfrage und Pipeline                                | ASIC-Probe, Risk-Event offen                   |    58 | Beobachten   | Risk-Event und Volumen klären                                               |

---

## 6. Offene Prüfpunkte

* NIO nur als Kandidat beobachten; kein `buy_check`, solange Score unter 80 bleibt.
* RGTI nur weiter prüfen; kein `buy_check`, solange Score unter 80 bleibt oder Volumencheck nicht sauber bestätigt ist.
* Ziel_pct, Stop_pct und Time_stop_days vor jedem `buy_check` konkret setzen; STEP B-Defaults für Top-2: +25 % / -10 % / 7T.
* Fee-Gate erst nach finalem Order-Preview und Break-even-Check freigeben (Mission Control).
* Finalen EUR-Preis zum Order-Zeitpunkt, Spread, Fractional-Ausführung und Ordergültigkeit vor Ausführung prüfen (MC).

---

## 7. Bekannte Unsicherheiten

* DQ **B**: Markt-/Newsdaten teils zeitverzögert; Web-Recherche in STEP A, nicht in File gespeichert.
* Catalyst-Score ist heuristisch und kann schnell kippen.
* Gebühren/Steuer sind Modellannahmen.
* Kein Broker-Fill, kein Real-Order-Preview und keine echte Ausführung bestätigt.
* STEP-A-Volumendaten bei mehreren Kandidaten widersprüchlich; bei Widerspruch wurde `volume_check=fail` gesetzt.

---

## 8. Letzte Änderungen

* 2026-05-28: Clean-Slate-Reset durchgeführt (keine Positionen, Watchlist geleert).
* 2026-05-28: STEP A/B/C abgeschlossen; Watchlist mit 8 Kandidaten neu aufgebaut; NIO als `candidate`/Top-Beobachtung gesetzt; keine Kaufprüfung, keine Ausführung.
* 2026-05-29: STEP A/B/C abgeschlossen; Web-Gate geprüft; keine Position; keine Kaufprüfung wegen `score_unter_80_gate_fail`; state_machine bleibt `candidate`.
