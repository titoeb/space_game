from typing import List, Tuple

from space_game import game_state, text, write_to_user


def apply_planet_logic(
    *,
    planet: str,
    engines: bool,
    credits: bool,
    copilot: bool,
    game_end: bool,
) -> Tuple[List[str], game_state.GameState]:
    if planet == "earth":
        destinations = ["centauri", "sirius"]
        print(text.EARTH_DESCRIPTION)

    if planet == "centauri":
        print(text.CENTAURI_DESCRIPTION)
        destinations = ["earth", "orion"]

        if not engines:
            print(text.HYPERDRIVE_SHOPPING_QUESTION)
            if input() == "yes":
                if credits:
                    engines = True
                else:
                    print(text.HYPERDRIVE_TOO_EXPENSIVE)

    if planet == "sirius":
        print(text.SIRIUS_DESCRIPTION)
        destinations = ["orion", "earth", "black_hole"]

        if not credits:
            print(text.SIRIUS_QUIZ_QUESTION)
            answer = input()
            if answer == "2":
                print(text.SIRIUS_QUIZ_CORRECT)
                credits = True
            else:
                print(text.SIRIUS_QUIZ_INCORRECT)

    if planet == "orion":
        destinations = ["centauri", "sirius"]
        if not copilot:
            print(text.ORION_DESCRIPTION)
            print(text.ORION_HIRE_COPILOT_QUESTION)
            if input() == "42":
                print(text.COPILOT_QUESTION_CORRECT)
                copilot = True
            else:
                print(text.COPILOT_QUESTION_INCORRECT)
        else:
            print(text.ORION_DESCRIPTION)

    if planet == "black_hole":
        print(text.BLACK_HOLE_DESCRIPTION)
        destinations = ["sirius"]
        if input() == "yes":
            if engines and copilot:
                print(text.BLACK_HOLE_COPILOT_SAVES_YOU)
                game_end = True
            else:
                print(text.BLACK_HOLE_CRUNCHED)
                game_end = True

    return destinations, planet, engines, credits, copilot, game_end


def select_next_planet(destinations: List[str]) -> str:
    print("\nWhere do you want to travel?")
    position = 1
    for d in destinations:
        print(f"[{position}] {d}")
        position += 1

    choice = input()
    return destinations[int(choice) - 1]


def game_setup() -> game_state.GameState:
    print(text.OPENING_MESSAGE)
    return game_state.GameState(
        planet="earth", engines=False, credits=False, copilot=False, game_end=False
    )


def travel():

    state_of_game = game_setup()
    while not state_of_game.game_end:

        write_to_user.display_inventory(
            credits=state_of_game.credits,
            engines=state_of_game.engines,
            copilot=state_of_game.engines,
        )
        (
            possible_destinations,
            planet,
            engines,
            credits,
            copilot,
            game_end,
        ) = apply_planet_logic(
            planet=state_of_game.planet,
            engines=state_of_game.engines,
            copilot=state_of_game.copilot,
            credits=state_of_game.credits,
            game_end=state_of_game.game_end,
        )

        state_of_game = game_state.GameState(
            planet=planet,
            engines=engines,
            credits=credits,
            copilot=copilot,
            game_end=game_end,
        )

        if not state_of_game.game_end:
            state_of_game = state_of_game.travel_to_planet(
                select_next_planet(possible_destinations)
            )

        print(text.END_CREDITS)
