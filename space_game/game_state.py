from __future__ import annotations

import dataclasses


@dataclasses.dataclass(kw_only=True)
class GameOptions:
    engines: bool
    credits: bool
    copilot: bool
    game_end: bool
