"""
Created on Wed Nov 13 15:32:28 2024
"""

__author__ = "Son Hoang"
__copyright__ = "Copyright (c) 2024, University of Southampton"
__credits__ = ["Son Hoang"]
__licence__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Son Hoang"
__email__ = "T.S.Hoang@soton.ac.uk"
__status__ = "Prototype"

from maze import create_maze, add_horizontal_wall  # type: ignore
from runner import (  # type: ignore
    create_runner,
    sense_walls,
    go_straight,
    get_x,
    get_y,
    turn,
    get_orientation,
    move,
    explore,
)


def test_runner_sense_walls() -> None:
    """A Unit test for :py:func:`~runner.sense_walls`

    Below is the test sequence:

    1. Create a maze of size (11, 5).

    2. Add a horizontal wall at (5, 2).

    3. Add a runner at (5, 2) facing East

    4. Assert that the runner sense no walls on the left and in the front, but
    there is a wall on the right.
    """
    maze = create_maze(11, 5)
    maze = add_horizontal_wall(maze, 5, 2)
    runner = create_runner(5, 2, "E")
    assert sense_walls(runner, maze) == (False, False, True)


def test_runner_go_straight() -> None:
    """A Unit test for :py:func:`~runner.go_straight`

    Below is the test sequence:

    1. Create a maze of size (11, 5).

    2. Add a horizontal wall at (5, 2).

    3. Add a runner at (5, 2) facing East

    4. Let the runner go straight

    4. Assert that the runner is at (6, 2)
    """
    maze = create_maze(11, 5)
    maze = add_horizontal_wall(maze, 5, 2)

    runner = create_runner(5, 2, "E")

    runner = go_straight(runner, maze)

    assert get_x(runner) == 6
    assert get_y(runner) == 2


def test_move() -> None:
    """A Unit test for :py:func:`~runner.move`

    Below is the test sequence:

    1. Create a maze of size (11, 5).

    2. Add a horizontal wall at (5, 2).

    3. Add a runner at (5, 2) facing South (toward the wall)

    4. Let the runner move and get the (new) runner and the actions.

    5. Assert that the new runner is at (6, 2) facing East

    6. Assert that the actions to get there were LF
    """
    maze = create_maze(11, 5)

    maze = add_horizontal_wall(maze, 5, 2)

    runner = create_runner(5, 2, "S")

    runner, actions = move(runner, maze)

    assert (get_x(runner), get_y(runner)) == (6, 2), f"Incorrect move for runner"
    assert get_orientation(runner) == "E"

    assert actions == "LF"


def test_explore() -> None:
    """
    The test for :py:func:~runner.explore should be similar to test_move() above
    (i.e., replaying the action to see if a test runner can follow the action to
    get to the target destination. This will left as an exercise for any keen
    testers.
    """
    maze = create_maze(5, 5)
    runner = create_runner(0, 0, "N")

    path = explore(runner, maze, goal=(4, 4))

    assert len(path) > 0

    x0, y0, _ = path[0]
    assert (x0, y0) == (0, 0)

    xf, yf, _ = path[-1]
    assert abs(xf - 4) + abs(yf - 4) == 1


def test_explore_minimal() -> None:
    """
    The test for :py:func:~runner.explore should be similar to test_move() above
    Below is the test sequence:
    1. Create a maze of size (5, 5).
    2. Create a runner at (0, 0) facing North
    3. explore the maze
    4. assert list is nonempty
    5. assert first tuple matches the starting point
    6. assert final tuple is adjacent to goal
    """
    maze = create_maze(5, 5)
    runner = create_runner(0, 0, "N")

    explored = explore(runner, maze, goal=(4, 4))

    assert len(explored) > 0

    x, y, _ = explored[0]
    assert (x, y) == (0, 0)

    xf, yf, _ = explored[-1]
    assert abs(xf - 4) + abs(yf - 4) == 1
