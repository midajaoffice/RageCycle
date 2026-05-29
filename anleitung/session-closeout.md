# Session Closeout (~5 Min.)

> Nur für dich — **nicht** ins ChatGPT Project.

---

## Vor dem Chat

- [ ] [`mc-datenritual.md`](mc-datenritual.md) — A/B/C Inputs vollständig, `modus` + `state_machine` + `step_status` in OPERATOR_VIEW
- [ ] [`../täglich/portfolio-state.md`](../täglich/portfolio-state.md) — `OPERATOR_VIEW` + Status ok? (max. 1 Position, Verlustserie sichtbar)
- [ ] Neuer Chat → Project **RageCycle**
- [ ] Project-Dateien aktuell (`operator-core`, `operator-protocol`, täglich/)

**Prompt:** [`daily-prompt.md`](daily-prompt.md)

---

## Nach dem Chat

- [ ] STEP A, STEP B, STEP C in Reihenfolge gelaufen (keine Steps übersprungen)
- [ ] Nur STEP-C-Output wird in Dateien übernommen
- [ ] `# UPDATED_PORTFOLIO_STATE` → `portfolio-state.md` (ganze Datei, Kurse prüfen!)
- [ ] `# NEW_LOG_ENTRY` → `decision-log.md` **und** `decision-log-recent.md` (`Ausführung`, `verlustserie`, `strategie_status`, `no_trade_grund`, `step_a_ok`, `step_b_ok`, `step_c_ok` gesetzt?)
- [ ] `# UPDATED_WATCHLIST` bei Status / Kauf / Verkauf / Verwerfen
- [ ] `# REJECTED_IDEA` → `ideen/rejected-ideas.md` wenn verworfen
- [ ] Verkauf: §4 Zeile weg, Cash stimmt, nächster Kandidat sauber vorbereitet
- [ ] Project: `portfolio-state` + `decision-log-recent` **ersetzen**

---

## Monatlich

- [ ] Einträge > 14 Tage aus `decision-log-recent` → `archiv/`
- [ ] Project Memory prüfen ([`memory-seed.md`](memory-seed.md)) — keine Portfolio-Zahlen
