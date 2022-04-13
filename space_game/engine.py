from typing import Tuple

from space_game import planets, state, texts, write_to_user


def select_next_planet(destinations: planets.Destinations) -> planets.Planet:
    print("\nWhere do you want to travel?")
    position = 1
    for planet in destinations.planets:
        print(f"[{position}] {planet}")
        position += 1

    choice = input()
    return destinations.planets[int(choice) - 1]()


def setup_game() -> Tuple[planets.Planet, state.GameOptions]:
    print(texts.OPENING_MESSAGE)

    return planets.Earth(), state.GameOptions(
        has_hyperdrive_engine=False,
        has_sufficient_credits=False,
        has_copilot=False,
        game_is_over=False,
    )


def wrap_up_game() -> None:
    print(texts.END_CREDITS)


def run_space_game() -> None:
    current_planet, current_state_of_game = setup_game()
    while not current_state_of_game.game_is_over:
        write_to_user.display_inventory(
            has_sufficient_credits=current_state_of_game.has_sufficient_credits,
            has_hyperdrive_engine=current_state_of_game.has_hyperdrive_engine,
            has_copilot=current_state_of_game.has_hyperdrive_engine,
        )
        current_state_of_game = current_planet.run(current_state_of_game)

        if not current_state_of_game.game_is_over:
            current_planet = select_next_planet(
                planets.possible_destinations(current_planet)
            )
    wrap_up_game()
