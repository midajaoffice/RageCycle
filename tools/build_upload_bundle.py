#!/usr/bin/env python3
"""Build a flat upload bundle with prefixed files."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUNDLE_DIR = ROOT / "upload-bundle"

FILES_TO_COPY: dict[str, Path] = {
    "gpt_operator-core.md": ROOT / "chatgpt" / "operator-core.md",
    "gpt_operator-protocol.md": ROOT / "chatgpt" / "operator-protocol.md",
    "gpt_chatgpt-instructions.md": ROOT / "chatgpt-instructions.md",
    "daily_portfolio-state.md": ROOT / "täglich" / "portfolio-state.md",
    "daily_decision-log-recent.md": ROOT / "täglich" / "decision-log-recent.md",
    "daily_watchlist.md": ROOT / "täglich" / "watchlist.md",
}


def main() -> None:
    BUNDLE_DIR.mkdir(exist_ok=True)

    for target_name, source_path in FILES_TO_COPY.items():
        if not source_path.is_file():
            raise FileNotFoundError(f"Source file missing: {source_path}")
        content = source_path.read_text(encoding="utf-8")
        target_path = BUNDLE_DIR / target_name
        target_path.write_text(content, encoding="utf-8")
        print(f"Wrote {target_path.relative_to(ROOT)}")

    print("Upload bundle refreshed.")


if __name__ == "__main__":
    main()
