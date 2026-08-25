#!/usr/bin/env python3
"""Verify that an installed advance-business-module Skill matches its release manifest."""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "MANIFEST.sha256"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    if not MANIFEST.is_file():
        print(f"missing manifest: {MANIFEST}", file=sys.stderr)
        return 2

    invalid = False
    for raw in MANIFEST.read_text(encoding="utf-8").splitlines():
        if not raw or raw.startswith("#"):
            continue
        try:
            expected, relative = raw.split("  ", 1)
        except ValueError:
            print(f"invalid manifest row: {raw}", file=sys.stderr)
            invalid = True
            continue
        target = ROOT / relative
        if not target.is_file():
            print(f"missing file: {relative}", file=sys.stderr)
            invalid = True
        elif digest(target) != expected:
            print(f"hash mismatch: {relative}", file=sys.stderr)
            invalid = True

    if invalid:
        return 1
    print("Skill snapshot verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
