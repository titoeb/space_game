from typing import List, Tuple

from space_game import game_state, planets, text, write_to_user


def select_next_planet(destinations: planets.Destinations) -> planets.Planet:
    print("\nWhere do you want to travel?")
    position = 1
    for planet in destinations.planets:
        print(f"[{position}] {planet}")
        position += 1

    choice = input()
    return destinations.planets[int(choice) - 1]


def initial_state() -> game_state.GameState:
    print(text.OPENING_MESSAGE)
    return game_state.GameState(
        planet=planets.Earth,
        engines=False,
        credits=False,
        copilot=False,
        game_end=False,
    )


def travel():

    state_of_game = initial_state()
    while not state_of_game.game_end:

        write_to_user.display_inventory(
            credits=state_of_game.credits,
            engines=state_of_game.engines,
            copilot=state_of_game.engines,
        )

        state_of_game = state_of_game.planet.run(state_of_game)

        if not state_of_game.game_end:
            state_of_game = state_of_game.travel_to_planet(
                select_next_planet(planets.possible_destinations(state_of_game.planet))
            )
    print(text.END_CREDITS)
