from __future__ import annotations

import os
from dataclasses import dataclass

try:
    from dotenv import load_dotenv  # type: ignore

    load_dotenv()
except Exception:
    # dotenv is optional
    pass


@dataclass(frozen=True)
class Settings:
    env: str = os.getenv("BUTNS_ENV", "dev")


settings = Settings()
