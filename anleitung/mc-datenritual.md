# MC-Datenritual — vor jedem Operator-Chat

> Nur für **Mission Control** — nicht ins ChatGPT Project.

Ohne dieses Ritual bleibt der Operator im Modus `maintenance`.

---

## Checkliste (5 Min.)

- [ ] Bitpanda-Handelbarkeit bestätigt (ja/nein)
- [ ] Kurs unter 50 EUR verifiziert (zum Entscheidungszeitpunkt)
- [ ] Frische Primär-Newsquelle zum Katalysator notiert
- [ ] Volumen/Momentum-Check dokumentiert
- [ ] Entry/Target/Stop/Time-stop festgelegt
- [ ] OPERATOR_VIEW aktualisiert: `kapital`, `modus`, `state_machine`, `step_status`, `positionen_detail`
- [ ] Verlustserie (0–3) und Strategie-Status (aktiv/pause) in Log-Entwurf vorgeprüft

## A/B/C Handoff (pro Tageslauf)

- STEP A Input vollständig vorbereiten (Kurse, Katalysator-Quelle, Volumen, Gate-Felder).
- STEP B nur starten, wenn STEP A vollständig ist.
- STEP C nur übernehmen, wenn A und B konsistent abgeschlossen wurden.

---

## Formeln (Orientierung)

```
round_trip_eur ≈ 2 × fee + 2 × (position_eur × slippage_pct)
break_even_pct ≈ round_trip_eur / position_eur × 100
min_target_pct ≈ max(15-20%, break_even_pct + sicherheitsaufschlag)
```

Mit 100 EUR sind kleine Moves meist unattraktiv. Fees/Spread/FX vorab einpreisen.

---

## OPERATOR_VIEW nach Ritual

```text
modus: maintenance|thesis_scan|action
state_machine: flat|candidate|buy_check|position|sell_check
step_status: step_a=offen|ok|step_b=offen|ok|step_c=offen|ok
positionen_detail: TICKER pnl=... trigger_kurs=ok|alarm trigger_news=ok|watch next=...
```

- MC pflegt Kurs, pnl, next.
- Operator pflegt Trigger-Logik im Sync.

---

## Modus-Empfehlung

| Situation | modus |
|---|---|
| Datenlücken oder kein Setup >=80 | `maintenance` |
| Kandidat/Position wird auf Katalysator geprüft | `thesis_scan` |
| Kauf-/Verkauf-Trigger erfüllt | `action` |

Siehe auch: [`session-closeout.md`](session-closeout.md)
