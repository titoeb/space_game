from __future__ import annotations

import abc
import dataclasses
from os import curdir
from typing import List

from pyparsing import Or

from space_game import game_state, game_texts


@dataclasses.dataclass(frozen=True, kw_only=True)
class Destinations:
    planets: List[Planet]


class Planet(abc.ABC):
    @abc.abstractstaticmethod
    def run(
        current_state: game_state.GameOptions,
    ) -> game_state.GameOptions:
        pass

    def __str__(self):
        return self.__class__.__name__


class Earth(Planet):
    EARTH_DESCRIPTION = "\nYou are on Earth. Beautiful is better than ugly."

    @staticmethod
    def run(current_state: game_state.GameOptions) -> game_state.GameOptions:
        print(Earth.EARTH_DESCRIPTION)
        return current_state


class Centauri(Planet):
    CENTAURI_DESCRIPTION = (
        "\nYou are on Alpha Centauri. All creatures are welcome here."
    )

    @staticmethod
    def run(current_state: game_state.GameOptions) -> game_state.GameOptions:
        print(Centauri.CENTAURI_DESCRIPTION)
        if not current_state.engines:
            print(game_texts.HYPERDRIVE_SHOPPING_QUESTION)
            if input() == "yes":
                if current_state.credits:
                    current_state.engines = True
                else:
                    print(game_texts.HYPERDRIVE_TOO_EXPENSIVE)
        return current_state


class Sirius(Planet):
    SIRIUS_DESCRIPTION = """You are on Sirius. The system is full of media companies and content delivery networks."""
    SIRIUS_QUIZ_QUESTION = """You manage to get a place in *Stellar* - the greatest quiz show in the universe.
Here is your question:

    Which star do you find on the shoulder of Orion?

[1] Altair
[2] Betelgeuse
[3] Aldebaran
[4] Andromeda
"""
    SIRIUS_QUIZ_CORRECT = """
*Correct!!!* You win a ton or credits.
"""
    SIRIUS_QUIZ_INCORRECT = """
Sorry, this was the wrong answer. Don't take it too sirius.
Better luck next time.
"""

    @staticmethod
    def run(current_state: game_state.GameOptions) -> game_state.GameOptions:
        print(Sirius.SIRIUS_DESCRIPTION)
        if not current_state.credits:
            print(Sirius.SIRIUS_QUIZ_QUESTION)
            answer = input()
            if answer == "2":
                print(Sirius.SIRIUS_QUIZ_CORRECT)
                current_state.credits = True
            else:
                print(Sirius.SIRIUS_QUIZ_INCORRECT)
        return current_state


class Orion(Planet):
    ORION_DESCRIPTION = """
You are on Orion. An icy world inhabited by furry sentients."""
    ORION_HIRE_COPILOT_QUESTION = """A tech-savvy native admires your spaceship.
They promise to join as a copilot if you can answer a question:

    What is the answer to question of life, the universe and everything?
    
What do you answer?"""

    @staticmethod
    def run(current_state: game_state.GameOptions) -> game_state.GameOptions:
        if not current_state.copilot:
            print(Orion.ORION_DESCRIPTION)
            print(Orion.ORION_HIRE_COPILOT_QUESTION)
            if input() == "42":
                print(game_texts.COPILOT_QUESTION_CORRECT)
                current_state.copilot = True
            else:
                print(game_texts.COPILOT_QUESTION_INCORRECT)
        else:
            print(Orion.ORION_DESCRIPTION)
        return current_state


class BlackHole(Planet):
    BLACK_HOLE_DESCRIPTION = """You are close to Black Hole #0997. Maybe coming here was a really stupid idea.
Do you want to examine the black hole closer? [yes/no]
"""
    BLACK_HOLE_CRUNCHED = """The black hole condenses your spaceship into a grain of dust.

    THE END
"""
    BLACK_HOLE_COPILOT_SAVES_YOU = """On the rim of the black hole your copilot blurts out:

    Turn left!

You ignite the next-gen hyperdrive, creating a time-space anomaly.
You travel through other dimensions and experience wonders beyond description.
"""

    def run(self, current_state: game_state.GameOptions) -> game_state.GameOptions:
        print(BlackHole.BLACK_HOLE_DESCRIPTION)
        if input() == "yes":
            if current_state.engines and current_state.copilot:
                print(BlackHole.BLACK_HOLE_COPILOT_SAVES_YOU)
                current_state.game_end = True
            else:
                print(BlackHole.BLACK_HOLE_CRUNCHED)
                current_state.game_end = True
        return current_state


def possible_destinations(current_planet: Planet) -> Destinations:
    match current_planet:
        case Earth():
            return Destinations(planets=[Centauri(), Sirius()])
        case Centauri():
            return Destinations(planets=[Earth(), Orion()])
        case Sirius():
            return Destinations(planets=[Orion(), Earth(), BlackHole()])
        case Orion():
            return Destinations(planets=[Centauri(), Sirius()])
        case BlackHole():
            return Destinations(planets=[Sirius()])
