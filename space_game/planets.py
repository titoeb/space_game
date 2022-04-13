from __future__ import annotations

import abc
import dataclasses
from typing import List

from space_game import state, texts


@dataclasses.dataclass(frozen=True, kw_only=True)
class Destinations:
    planets: List[Planet]


class Planet(abc.ABC):
    @abc.abstractstaticmethod
    def run(
        current_state: state.GameOptions,
    ) -> state.GameOptions:
        pass

    def __str__(self):
        return self.__class__.__name__


class Earth(Planet):
    DESCRIPTION = "\nYou are on Earth. Beautiful is better than ugly."

    @staticmethod
    def run(current_state: state.GameOptions) -> state.GameOptions:
        print(Earth.DESCRIPTION)
        return current_state


class Centauri(Planet):
    DESCRIPTION = "\nYou are on Alpha Centauri. All creatures are welcome here."

    @staticmethod
    def run(current_state: state.GameOptions) -> state.GameOptions:
        print(Centauri.DESCRIPTION)
        if not current_state.has_hyperdrive_engine:
            print(texts.HYPERDRIVE_SHOPPING_QUESTION)
            if input() == "yes":
                if current_state.has_sufficient_credits:
                    current_state.has_hyperdrive_engine = True
                else:
                    print(texts.HYPERDRIVE_TOO_EXPENSIVE)
        return current_state


class Sirius(Planet):
    DESCRIPTION = """You are on Sirius. The system is full of media companies and content delivery networks."""
    QUIZ_QUESTION = """You manage to get a place in *Stellar* - the greatest quiz show in the universe.
Here is your question:

    Which star do you find on the shoulder of Orion?

[1] Altair
[2] Betelgeuse
[3] Aldebaran
[4] Andromeda
"""
    QUIZ_CORRECT = """
*Correct!!!* You win a ton or credits.
"""
    QUIZ_INCORRECT = """
Sorry, this was the wrong answer. Don't take it too sirius.
Better luck next time.
"""

    @staticmethod
    def run(current_state: state.GameOptions) -> state.GameOptions:
        print(Sirius.DESCRIPTION)
        if not current_state.has_sufficient_credits:
            print(Sirius.QUIZ_QUESTION)
            answer = input()
            if answer == "2":
                print(Sirius.QUIZ_CORRECT)
                current_state.has_sufficient_credits = True
            else:
                print(Sirius.QUIZ_INCORRECT)
        return current_state


class Orion(Planet):
    DESCRIPTION = """
You are on Orion. An icy world inhabited by furry sentients."""
    HIRE_COPILOT_QUESTION = """A tech-savvy native admires your spaceship.
They promise to join as a copilot if you can answer a question:

    What is the answer to question of life, the universe and everything?

What do you answer?"""

    @staticmethod
    def run(current_state: state.GameOptions) -> state.GameOptions:
        if not current_state.has_copilot:
            print(Orion.DESCRIPTION)
            print(Orion.HIRE_COPILOT_QUESTION)
            if input() == "42":
                print(texts.COPILOT_QUESTION_CORRECT)
                current_state.has_copilot = True
            else:
                print(texts.COPILOT_QUESTION_INCORRECT)
        else:
            print(Orion.DESCRIPTION)
        return current_state


class BlackHole(Planet):
    DESCRIPTION = """You are close to Black Hole #0997. Maybe coming here was a really stupid idea.
Do you want to examine the black hole closer? [yes/no]
"""
    CRUNCHED = """The black hole condenses your spaceship into a grain of dust.

    THE END
"""
    COPILOT_SAVES_YOU = """On the rim of the black hole your copilot blurts out:

    Turn left!

You ignite the next-gen hyperdrive, creating a time-space anomaly.
You travel through other dimensions and experience wonders beyond description.
"""

    def run(self, current_state: state.GameOptions) -> state.GameOptions:
        print(BlackHole.DESCRIPTION)
        if input() == "yes":
            if current_state.has_hyperdrive_engine and current_state.has_copilot:
                print(BlackHole.COPILOT_SAVES_YOU)
                current_state.game_is_over = True
            else:
                print(BlackHole.CRUNCHED)
                current_state.game_is_over = True
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
