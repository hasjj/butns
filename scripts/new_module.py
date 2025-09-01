#!/usr/bin/env python3
from __future__ import annotations

import argparse
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src" / "butns" / "modules"

TEMPLATE_INIT = ""  # 공개 API는 필요할 때만 노출
TEMPLATE_FEATURE = """from __future__ import annotations

def run(payload: dict | None = None) -> dict:
    \"\"\"모듈의 진입점. payload를 받아서 결과 dict를 반환합니다.\"\"\"
    return {"ok": True, "input": payload}
"""

TEMPLATE_TEST = textwrap.dedent(
    """
    import importlib

    def test_module_import():
        m = importlib.import_module("butns.modules.{name}.feature")
        assert hasattr(m, "run") and callable(m.run)
    """
)


def create_module(name: str) -> None:
    target = SRC / name
    (target / "adapters").mkdir(parents=True, exist_ok=True)
    (target / "__init__.py").write_text(TEMPLATE_INIT, encoding="utf-8")
    (target / "feature.py").write_text(TEMPLATE_FEATURE, encoding="utf-8")

    tests = ROOT / "tests"
    tests.mkdir(exist_ok=True)
    (tests / f"test_{name}.py").write_text(TEMPLATE_TEST.format(name=name), encoding="utf-8")

    print(f"Created: {target}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Scaffold a new BUTNS module")
    ap.add_argument("name", help="module name, e.g. 'reader'")
    args = ap.parse_args()
    create_module(args.name)


if __name__ == "__main__":
    main()
