import io

import pytest
from space_game import engine


@pytest.fixture
def solution_input():
    """Provide the solution of the game into a StringIO object so that it can
    easily be put into stdin."""
    return io.StringIO(
        "\n".join(  # the actual solution to the game
            [
                "2",
                "2",  # go to sirius and win quiz
                "1",
                "42",  # hire copilot on orion
                "1",
                "yes",  # go to centauri and buy GPU drive
                "2",
                "2",
                "3",
                "yes",  # jump into black hole
            ]
        )
    )


def test_travel(monkeypatch, solution_input):
    """Given the solution to the game, test that the game runs through."""
    monkeypatch.setattr("sys.stdin", solution_input)
    engine.run_space_game()


def test_output(monkeypatch, capsys, solution_input):
    """Given the actual solution to the game, test that the
    games outputs someting on stdout."""
    monkeypatch.setattr("sys.stdin", solution_input)

    engine.run_space_game()

    captured = capsys.readouterr()
    assert len(captured.out) > 0


def test_death_by_black_hole(monkeypatch, capsys):
    """Test that the player dies if he does jump into the blackout without having
    copilot and hyper-engine."""
    death_by_black_hole_stdin = io.StringIO(
        "\n".join(
            [
                "2",
                "2",  # go to sirius and win quiz
                "1",
                "41",  # hire copilot on orion
                "1",
                "yes",  # go to centauri and buy GPU drive
                "1",
                "2",
                "3",
                "yes",  # jump into black hole
            ]
        )
    )
    monkeypatch.setattr("sys.stdin", death_by_black_hole_stdin)

    engine.run_space_game()

    captured = capsys.readouterr()
    assert "grain of dust" in captured.out
    assert " wonders beyond description" not in captured.out


@pytest.mark.parametrize(
    "phrase",  # text sniplets that should appear literally in the output
    [
        "The stars are waiting for you",
        "Betelgeuse",
        "credits",
        "tech-savvy native",
        "copilot",
        "buy",
        "life, the universe and everything",
        "Black Hole",
        "stupid idea",
        "wonders beyond description",
        "THE END",
    ],
)
def test_output_phrases(monkeypatch, capsys, solution_input, phrase):
    """When running the successful solution, test that the game outputs
    some expected phrases."""
    monkeypatch.setattr("sys.stdin", solution_input)

    engine.run_space_game()

    captured = capsys.readouterr()
    assert phrase in captured.out
