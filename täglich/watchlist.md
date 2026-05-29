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
| Pre-Trade-Gate                                    | price_lt_50, catalyst_source, volume_check, ziel/stop/time_stop, fee_gate müssen vollständig erfüllt sein (STEP A: Web für Kurs/News/Volumen) |
| Operator-Pipeline                                 | `operator-protocol.md` (Catalyst-Score + Lifecycle)                                                                    |

## Aktive Watchlist

| Asset              | Ticker | Markt  | Thema                           | Fakt / Annahme / Spekulation                              | Katalysator                                                         | Warum interessant?                                                              | Hauptrisiko                                            | Score | Status       | Nächster Prüfpunkt                                                                    | DQ |
| ------------------ | ------ | ------ | ------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------ | ----: | ------------ | ------------------------------------------------------------------------------------- | -- |
| NIO                | NIO    | NYSE   | EV / China / Overseas Push      | Fakt: Top-Kandidat; Score 75; Defaults +25/-10/7T           | ES9-/Overseas-Push, April-Lieferungen +22,8 % YoY, hohes Volumen    | Top-Beobachtung; kein buy_check bis Score >=80                                 | EV-Wettbewerb, China-Makro, gate_fail score            |    75 | Beobachten   | MC Intraday-Volumen; Score >=80; Order-Preview nur bei buy_check                        | B  |
| Rigetti Computing  | RGTI   | NASDAQ | Quantum Computing               | Annahme: starker Katalysator; Score 77; Volumen fail      | LOI mit U.S. Commerce für bis zu 100 Mio. USD Quantum-R&D-Förderung | Quantum-Hype; Defaults +25/-10/7T gesetzt                                     | Score <80, volume_check fail                           |    77 | Daten prüfen | MC Intraday-Volumen; Score >=80 für buy_check                                             | B  |
| SoundHound AI      | SOUN   | NASDAQ | Voice AI / KI                   | Annahme: Growth-Katalysator; Volumen fail                   | Q1-Umsatz +52 % YoY, FY26-Outlook bestätigt                         | KI-Narrativ, Umsatzwachstum                                                     | Multiple-/Volatilität, Minima fail                     |    73 | Daten prüfen | Volumen/Momentum; Score-Minima                                                          | B  |
| Riot Platforms     | RIOT   | NASDAQ | Bitcoin Mining / AI Data Center | Fakt: Preis <50 EUR external; Volumen fail                  | Q1-/Data-Center-Shift, AMD Capacity-Option                          | BTC-/AI-Infrastruktur-Kombination                                               | BTC-Korrelation, Catalyst-Minima                       |    65 | Daten prüfen | Volumen gegen 50T-Avg; Catalyst-Minima                                                  | B  |
| Archer Aviation    | ACHR   | NYSE   | eVTOL / Defense / Aviation      | Annahme: Volumen pass external; CRV offen                   | FAA-/Midnight-Zertifizierung, Defense-/Partnerstory                 | eVTOL- und Defense-Narrativ                                                     | Kapitalbedarf, Minima fail                             |    66 | Daten prüfen | Ziel/Stop/Time-stop; Score-Minima                                                       | B  |
| D-Wave Quantum     | QBTS   | NYSE   | Quantum Computing               | Annahme: Sektor-Katalysator; Volumen fail                    | U.S.-Förderpaket / Quantum-Funding-Story                            | Quantum-Momentum                                                                | Volumen schwach, Minima fail                           |    62 | Daten prüfen | Volumencheck; Catalyst-Minima                                                           | B  |
| Intuitive Machines | LUNR   | NASDAQ | Space / Lunar Infrastructure    | Spekulation: gemischter Katalysator                       | Lunar-Reconnaissance/Q1-Backlog, aber NASA-Rover-Negativkatalysator | Space-Narrativ mit Event-Potenzial                                              | Katalysator gemischt, Volumen fail                     |    54 | Beobachten   | Nur bei klarer positiver Newsqualität neu prüfen                                        | B  |
| DroneShield        | DRO    | ASX    | Counter-Drone / Defense         | Fakt: Preis/Volumen external ok; Risk-Event offen         | Counter-drone-Nachfrage und Pipeline                                | Defense-/Counter-drone-Momentum                                                 | ASIC-Probe, Risk-Event, Ziel/Stop fehlt                |    58 | Beobachten   | Risk-Event klären; Ziel/Stop setzen                                                     | B  |

## Themenradar

| Thema                        | Katalysatoren                                           | Risiko                                                | Status |
| ---------------------------- | ------------------------------------------------------- | ----------------------------------------------------- | ------ |
| Quantum Computing            | U.S.-Funding, Regierungsprogramme, Defense-/R&D-Budgets | Verwässerung, Hype-Reversal, Broker-Verfügbarkeit     | aktiv  |
| AI Voice / Application AI    | Umsatzwachstum, Enterprise-AI-Adoption                  | hohe Multiples, schnelle Sentimentwechsel             | aktiv  |
| EV China                     | Lieferzahlen, neue Modelle, Overseas-Push               | Margendruck, China-Makro, ADR-Risiko                  | aktiv  |
| Defense / Counter-Drone      | Nachfrage durch geopolitische Lage, Order-Pipeline      | politische Headline-Risiken, regulatorische Prüfungen | aktiv  |
| Space / Lunar Infrastructure | NASA-/Defense-Aufträge, Backlog, Missionsnews           | Auftragsverluste, Event-Risiko, hohe Volatilität      | aktiv  |
