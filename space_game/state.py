from __future__ import annotations

import dataclasses


@dataclasses.dataclass(kw_only=True)
class GameOptions:
    has_hyperdrive_engine: bool
    has_sufficient_credits: int
    has_copilot: bool
    game_is_over: bool
