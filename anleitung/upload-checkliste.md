# ChatGPT Project — Upload-Checkliste

Project-Name: **`RageCycle`**

---

## 1. Instructions

[`chatgpt-instructions.md`](../chatgpt-instructions.md) → Project **Instructions** kopieren (Trader-Disziplin, Operator-Modi, Lifecycle)

---

## 2. Project Files (5 Dateien)

| # | Datei |
|---|---|
| 1 | `chatgpt/operator-core.md` |
| 2 | `chatgpt/operator-protocol.md` |
| 3 | `täglich/portfolio-state.md` |
| 4 | `täglich/decision-log-recent.md` |
| 5 | `täglich/watchlist.md` |

Alternativ als flaches Bundle (mit Präfixen `gpt_`/`daily_`):

- Ordner: `upload-bundle/`
- Aktualisieren mit: `python3 tools/build_upload_bundle.py`
- Entsprechende Dateien:
  - `upload-bundle/gpt_operator-core.md`
  - `upload-bundle/gpt_operator-protocol.md`
  - `upload-bundle/gpt_chatgpt-instructions.md`
  - `upload-bundle/daily_portfolio-state.md`
  - `upload-bundle/daily_decision-log-recent.md`
  - `upload-bundle/daily_watchlist.md`

**Nicht hochladen:** `operator-rules.md`, `north-star.md` (Redirects), `hcsp-lite.md`, `anleitung/`, `archiv/`, `decision-log.md` (nur Git/lokal), `ideen/rejected-ideas.md` (Mission Control)

**Nach Lebenszyklus-Update:** `operator-protocol.md` + `operator-core.md` einmal neu ins Project laden.

---

## 3. Tools

Web Search **an** · Code Interpreter **aus** · Memory **an** mit [`memory-seed.md`](memory-seed.md) (keine Portfolio-Zahlen in Memory; monatlich prüfen)

---

## 4. Nach jedem Tag ersetzen

- `täglich/portfolio-state.md`
- `täglich/decision-log-recent.md`
