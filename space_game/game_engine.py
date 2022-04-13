from space_game import text, write_to_user


def travel():

    print(text.TEXT["OPENING_MESSAGE"])

    planet = "earth"
    engines = False
    copilot = False
    credits = False
    game_end = False

    while not game_end:

        write_to_user.display_inventory(
            credits=credits, engines=engines, copilot=copilot
        )

        #
        # interaction with planets
        #
        if planet == "earth":
            destinations = ["centauri", "sirius"]
            print(text.TEXT["EARTH_DESCRIPTION"])

        if planet == "centauri":
            print(text.TEXT["CENTAURI_DESCRIPTION"])
            destinations = ["earth", "orion"]

            if not engines:
                print(text.TEXT["HYPERDRIVE_SHOPPING_QUESTION"])
                if input() == "yes":
                    if credits:
                        engines = True
                    else:
                        print(text.TEXT["HYPERDRIVE_TOO_EXPENSIVE"])

        if planet == "sirius":
            print(text.TEXT["SIRIUS_DESCRIPTION"])
            destinations = ["orion", "earth", "black_hole"]

            if not credits:
                print(text.TEXT["SIRIUS_QUIZ_QUESTION"])
                answer = input()
                if answer == "2":
                    print(text.TEXT["SIRIUS_QUIZ_CORRECT"])
                    credits = True
                else:
                    print(text.TEXT["SIRIUS_QUIZ_INCORRECT"])

        if planet == "orion":
            destinations = ["centauri", "sirius"]
            if not copilot:
                print(text.TEXT["ORION_DESCRIPTION"])
                print(text.TEXT["ORION_HIRE_COPILOT_QUESTION"])
                if input() == "42":
                    print(text.TEXT["COPILOT_QUESTION_CORRECT"])
                    copilot = True
                else:
                    print(text.TEXT["COPILOT_QUESTION_INCORRECT"])
            else:
                print(text.TEXT["ORION_DESCRIPTION"])

        if planet == "black_hole":
            print(text.TEXT["BLACK_HOLE_DESCRIPTION"])
            destinations = ["sirius"]
            if input() == "yes":
                if engines and copilot:
                    print(text.TEXT["BLACK_HOLE_COPILOT_SAVES_YOU"])
                    game_end = True
                else:
                    print(text.TEXT["BLACK_HOLE_CRUNCHED"])
                    return

        if not game_end:
            # select next planet
            print("\nWhere do you want to travel?")
            position = 1
            for d in destinations:
                print(f"[{position}] {d}")
                position += 1

            choice = input()
            planet = destinations[int(choice) - 1]

    print(text.TEXT["END_CREDITS"])
