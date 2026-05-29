# Watchlist

Ideen und Kandidaten zur Beobachtung. Keine Kaufempfehlung.

## Regeln (Radar + Positionen)

| Regel                                             | Wert                                                                                                                   |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Radar (Beobachten / Kaufen prüfen / Daten prüfen) | 5–8 Ticker                                                                                                             |
| Offene Positionen                                 | max. 1 (Wahrheit in `portfolio-state.md` §4)                                                                           |
| Status Position                                   | bleibt bis Verkauf bestätigt                                                                                           |
| Status Verworfen                                  | Zeile entfernen und in `rejected-ideas.md` dokumentieren                                                               |
| Auffüllen                                         | nach Exit/Verwerfen: nächster Top-Score-Kandidat                                                                       |
| Kaufen prüfen                                     | nur bei Score >= 80 und Trade-Gate                                                                                     |
| Kategorie-Minima                                  | Catalyst >=18/25, Newsqualität >=7/10, Momentum >=8/15, Chance/Risiko >=3/5                                            |
| Pre-Trade-Gate                                    | bitpanda_ok, price_lt_50, catalyst_source, volume_check, ziel/stop/time_stop, fee_gate müssen vollständig erfüllt sein |
| Operator-Pipeline                                 | `operator-protocol.md` (Catalyst-Score + Lifecycle)                                                                    |

## Aktive Watchlist

| Asset              | Ticker | Markt  | Thema                           | Fakt / Annahme / Spekulation                              | Katalysator                                                         | Warum interessant?                                                              | Hauptrisiko                                            | Score | Status       | Nächster Prüfpunkt                                                                    | DQ |
| ------------------ | ------ | ------ | ------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------ | ----: | ------------ | ------------------------------------------------------------------------------------- | -- |
| NIO                | NIO    | NYSE   | EV / China / Overseas Push      | Fakt: STEP-A-Gate ok; Score unter 80                      | ES9-/Overseas-Push, April-Lieferungen +22,8 % YoY, hohes Volumen    | Einziger Kandidat mit vollständigem STEP-A-Gate; Momentum und Volumen plausibel | EV-Wettbewerb, China-Makro, ADR-Risiko, Score nur 75   |    75 | Beobachten   | Score >=80 nur bei stärkerem Momentum/Breakout; Bitpanda-App und Volumen final prüfen | B  |
| Rigetti Computing  | RGTI   | NASDAQ | Quantum Computing               | Annahme: starker Katalysator; Gate offen                  | LOI mit U.S. Commerce für bis zu 100 Mio. USD Quantum-R&D-Förderung | Quantum-Hype und Funding-Katalysator                                            | Bitpanda-App-Check offen, Verwässerungsrisiko          |    77 | Daten prüfen | Bitpanda-App-Verfügbarkeit und finalen Volumencheck prüfen                            | B  |
| SoundHound AI      | SOUN   | NASDAQ | Voice AI / KI                   | Annahme: Growth-Katalysator; Gate offen                   | Q1-Umsatz +52 % YoY, FY26-Outlook bestätigt                         | KI-Narrativ, Umsatzwachstum, hohes Interesse                                    | Bitpanda-App-Check offen, Multiple-/Volatilitätsrisiko |    73 | Daten prüfen | Bitpanda-App-Verfügbarkeit prüfen                                                     | B  |
| Riot Platforms     | RIOT   | NASDAQ | Bitcoin Mining / AI Data Center | Fakt/Annahme: Bitpanda + Preisfilter ok; Volumen offen    | Q1-/Data-Center-Shift, AMD Capacity-Option                          | BTC-/AI-Infrastruktur-Kombination                                               | Intraday-Volumen offen, BTC-Korrelation                |    65 | Daten prüfen | Intraday-Volumen gegen 50T-Avg prüfen                                                 | B  |
| Archer Aviation    | ACHR   | NYSE   | eVTOL / Defense / Aviation      | Annahme: thematisch stark; Gate offen                     | FAA-/Midnight-Zertifizierung, Defense-/Partnerstory                 | eVTOL- und Defense-Narrativ                                                     | Bitpanda-App-Check offen, Kapitalbedarf                |    66 | Daten prüfen | Bitpanda-App-Verfügbarkeit prüfen                                                     | B  |
| D-Wave Quantum     | QBTS   | NYSE   | Quantum Computing               | Annahme: Sektor-Katalysator; Gate offen                   | U.S.-Förderpaket / Quantum-Funding-Story                            | Quantum-Momentum, Spekulationsinteresse                                         | Bitpanda-App-Check und Volumen offen                   |    62 | Daten prüfen | Bitpanda-App und Volumencheck prüfen                                                  | B  |
| Intuitive Machines | LUNR   | NASDAQ | Space / Lunar Infrastructure    | Spekulation: gemischter Katalysator                       | Lunar-Reconnaissance/Q1-Backlog, aber NASA-Rover-Negativkatalysator | Space-Narrativ mit Event-Potenzial                                              | Katalysator gemischt, Volumen offen                    |    54 | Beobachten   | Nur bei klarer positiver Newsqualität neu prüfen                                      | B  |
| DroneShield        | DRO    | ASX    | Counter-Drone / Defense         | Fakt/Annahme: Bitpanda + Preisfilter ok; Risk-Event offen | Counter-drone-Nachfrage und Pipeline                                | Defense-/Counter-drone-Momentum                                                 | ASIC-Probe, Volumen offen, Risk-Event                  |    58 | Beobachten   | Risk-Event und Volumen klären                                                         | B  |

## Themenradar

| Thema                        | Katalysatoren                                           | Risiko                                                | Status |
| ---------------------------- | ------------------------------------------------------- | ----------------------------------------------------- | ------ |
| Quantum Computing            | U.S.-Funding, Regierungsprogramme, Defense-/R&D-Budgets | Verwässerung, Hype-Reversal, Broker-Verfügbarkeit     | aktiv  |
| AI Voice / Application AI    | Umsatzwachstum, Enterprise-AI-Adoption                  | hohe Multiples, schnelle Sentimentwechsel             | aktiv  |
| EV China                     | Lieferzahlen, neue Modelle, Overseas-Push               | Margendruck, China-Makro, ADR-Risiko                  | aktiv  |
| Defense / Counter-Drone      | Nachfrage durch geopolitische Lage, Order-Pipeline      | politische Headline-Risiken, regulatorische Prüfungen | aktiv  |
| Space / Lunar Infrastructure | NASA-/Defense-Aufträge, Backlog, Missionsnews           | Auftragsverluste, Event-Risiko, hohe Volatilität      | aktiv  |
