from typing import List, Tuple

from space_game import game_state, game_texts, planets, write_to_user


def select_next_planet(destinations: planets.Destinations) -> planets.Planet:
    print("\nWhere do you want to travel?")
    position = 1
    for planet in destinations.planets:
        print(f"[{position}] {planet}")
        position += 1

    choice = input()
    return destinations.planets[int(choice) - 1]


def initial_state() -> Tuple[planets.Planet, game_state.GameOptions]:
    print(game_texts.OPENING_MESSAGE)

    return planets.Earth(), game_state.GameOptions(
        engines=False,
        credits=False,
        copilot=False,
        game_end=False,
    )


def start_space_game():

    current_planet, current_state_of_game = initial_state()
    while not current_state_of_game.game_end:
        write_to_user.display_inventory(
            credits=current_state_of_game.credits,
            engines=current_state_of_game.engines,
            copilot=current_state_of_game.engines,
        )
        current_state_of_game = current_planet.run(current_state_of_game)

        if not current_state_of_game.game_end:
            current_planet = select_next_planet(
                planets.possible_destinations(current_planet)
            )
    print(game_texts.END_CREDITS)
