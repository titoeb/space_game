"""Capture the state of the current Game."""
from __future__ import annotations

import dataclasses


@dataclasses.dataclass(kw_only=True)
class GameOptions:
    """These different options describe the current state of the `SpaceGame`-state."""

    has_hyperdrive_engine: bool
    has_sufficient_credits: bool
    has_copilot: bool
    game_is_over: bool
