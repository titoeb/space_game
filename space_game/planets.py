from __future__ import annotations

import abc
import dataclasses
from os import curdir
from typing import List

from space_game import game_state, text


@dataclasses.dataclass(frozen=True, kw_only=True)
class Destinations:
    planets: List[Planet]


class Planet(abc.ABC):
    @abc.abstractstaticmethod
    def run(
        current_state: game_state.GameState,
    ) -> game_state.GameState:
        pass

    def __str__(self):
        return self.__class__.__name__


class Earth(Planet):
    @staticmethod
    def run(current_state: game_state.GameState) -> game_state.GameState:
        print(text.EARTH_DESCRIPTION)
        return current_state


class Centauri(Planet):
    @staticmethod
    def run(current_state: game_state.GameState) -> game_state.GameState:
        print(text.CENTAURI_DESCRIPTION)
        if not current_state.engines:
            print(text.HYPERDRIVE_SHOPPING_QUESTION)
            if input() == "yes":
                if current_state.credits:
                    current_state.engines = True
                else:
                    print(text.HYPERDRIVE_TOO_EXPENSIVE)
        return current_state


class Sirius(Planet):
    @staticmethod
    def run(current_state: game_state.GameState) -> game_state.GameState:
        print(text.SIRIUS_DESCRIPTION)
        if not current_state.credits:
            print(text.SIRIUS_QUIZ_QUESTION)
            answer = input()
            if answer == "2":
                print(text.SIRIUS_QUIZ_CORRECT)
                current_state.credits = True
            else:
                print(text.SIRIUS_QUIZ_INCORRECT)
        return current_state


class Orion(Planet):
    @staticmethod
    def run(current_state: game_state.GameState) -> game_state.GameState:
        if not current_state.copilot:
            print(text.ORION_DESCRIPTION)
            print(text.ORION_HIRE_COPILOT_QUESTION)
            if input() == "42":
                print(text.COPILOT_QUESTION_CORRECT)
                current_state.copilot = True
            else:
                print(text.COPILOT_QUESTION_INCORRECT)
        else:
            print(text.ORION_DESCRIPTION)
        return current_state


class BlackHole(Planet):
    def run(self, current_state: game_state.GameState) -> game_state.GameState:
        print(text.BLACK_HOLE_DESCRIPTION)
        if input() == "yes":
            if current_state.engines and current_state.copilot:
                print(text.BLACK_HOLE_COPILOT_SAVES_YOU)
                current_state.game_end = True
            else:
                print(text.BLACK_HOLE_CRUNCHED)
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
