"""
Created on Fri Oct 25 12:07:22 2024
"""

__author__ = "Son Hoang"
__copyright__ = "Copyright (c) 2024, University of Southampton"
__credits__ = ["Son Hoang"]
__licence__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Son Hoang"
__email__ = "T.S.Hoang@soton.ac.uk"
__status__ = "Prototype"


from runner import (  # type: ignore
    create_runner,
    get_orientation,
    get_x,
    get_y,
    turn,
    forward,
)


def test_create_runner() -> None:
    """A Unit test for :py:func:`~runner.create_runner`

    Below is the test sequence:

    1. Create a runner at position (1,2), facing South.

    2. Assert the x, y positions (1, 2), and the orientation ("S") of the newly
    created runner.
    """
    runner = create_runner(1, 2, "S")
    assert get_x(runner) == 1
    assert get_y(runner) == 2
    assert get_orientation(runner) == "S"


def test_turn() -> None:
    """A Unit test for :py:func:`~runner.turn`

    Below is the test sequence:

    1. Create a runner at position (1,2), facing South.

    2. Let the runner turn to the Left.

    3. Assert the x, y positions (1, 2), and the orientation ("E") of the runner.
    """
    runner = create_runner(1, 2, "S")
    runner = turn(runner, "Left")
    assert get_x(runner) == 1
    assert get_y(runner) == 2
    assert get_orientation(runner) == "E"


def test_forward() -> None:
    """A Unit test for :py:func:`~runner.forward`

    Below is the test sequence:

    1. Create a runner at position (1,2), facing South.

    2. Let the runner more forward.

    3. Assert the x, y positions (1, 1), and the orientation ("S") of the runner.
    """
    runner = create_runner(1, 2, "S")
    runner = forward(runner)
    assert get_x(runner) == 1
    assert get_y(runner) == 1
    assert get_orientation(runner) == "S"


# my additional tests
def test_create_default_runner() -> None:
    """A Unit test for :py:func:`~runner.create_runner`
    Below is the test sequence:
    1. Create a runner at default position
    2. Pass no parameters
    3. Assert the x, y positions (0, 0), and the orientation ("N") of the runner.
    """
    runner = create_runner()
    assert get_x(runner) == 0
    assert get_y(runner) == 0
    assert get_orientation(runner) == "N"


def test_turn_right() -> None:
    """A Unit test for :py:func:`~runner.turn
    and :py:func:`~runner.turn `
    Below is the test sequence:
    1. Create a runner at position (1,2), facing North
    2. Let the runner turn to the right.
    3. Assert the x, y positions (1, 2), and the orientation ("E") of the runner."""

    runner = create_runner(1, 2, "N")
    runner = turn(runner, "Right")
    assert get_orientation(runner) == "E"
    assert get_x(runner) == 1
    assert get_y(runner) == 2


def test_forward_north() -> None:
    """A Unit test for :py:func:`~runner.forward`
    Below is the test sequence:
    1. Create a runner at position (3,3), facing North
    2. Let the runner forward.
    3. Assert the x, y positions (3, 4), and the orientation ("N") of the runner.
    """

    runner = create_runner(3, 3, "N")
    runner = forward(runner)
    assert get_x(runner) == 3
    assert get_y(runner) == 4
    assert get_orientation(runner) == "N"


def test_forward_east() -> None:
    """A Unit test for :py:func:`~runner.forward`
    Below is the test sequence:
    1. Create a runner at position (3, 3), facing East
    2. Let the runner forward.
    3. Assert the x, y positions (4, 3), and the orientation ("E") of the runner."""

    runner = create_runner(3, 3, "E")
    runner = forward(runner)
    assert get_x(runner) == 4
    assert get_y(runner) == 3
    assert get_orientation(runner) == "E"


def test_forward_west() -> None:
    """A Unit test for :py:func:`~runner.forward`
    Below is the test sequence:
    1. Create a runner at position (3, 3), facing West
    2. Let the runner forward.
    3. Assert the x, y positions (4, 3), and the orientation ("W") of the runner.
    """

    runner = create_runner(3, 3, "W")
    runner = forward(runner)
    assert get_x(runner) == 2
    assert get_y(runner) == 3
    assert get_orientation(runner) == "W"
