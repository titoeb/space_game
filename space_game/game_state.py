from __future__ import annotations

import dataclasses


@dataclasses.dataclass(frozen=True, kw_only=True)
class GameState:
    planet: str
    engines: bool
    credits: bool
    copilot: bool
    game_end: bool

    def travel_to_planet(self, planet: str) -> GameState:
        return GameState(
            planet=planet,
            engines=self.engines,
            credits=self.credits,
            copilot=self.copilot,
            game_end=self.game_end,
        )
