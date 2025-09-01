from __future__ import annotations

import logging
import sys

_FMT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"


def setup_logger(level: int = logging.INFO) -> None:
    """Idempotent logging setup."""
    if getattr(setup_logger, "_configured", False):
        return
    logging.basicConfig(stream=sys.stdout, level=level, format=_FMT)
    setup_logger._configured = True  # type: ignore[attr-defined]
