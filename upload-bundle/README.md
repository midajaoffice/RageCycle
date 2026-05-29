# Upload Bundle

Dieser Ordner bündelt die Upload-Dateien aus `chatgpt/` und `täglich/` in einer flachen Struktur.

Präfixe:

- `gpt_` = Datei stammt aus `chatgpt/` oder `chatgpt-instructions.md`
- `daily_` = Datei stammt aus `täglich/`

## Aktualisieren

Im Repo-Root ausführen:

```bash
python3 tools/build_upload_bundle.py
```

Danach sind folgende Dateien im Bundle:

- `gpt_operator-core.md`
- `gpt_operator-protocol.md`
- `gpt_chatgpt-instructions.md`
- `daily_portfolio-state.md`
- `daily_decision-log-recent.md`
- `daily_watchlist.md`
