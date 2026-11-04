"""
Created on Tue Nov 05 18:38:42 2024
"""

__author__ = "Son Hoang"
__copyright__ = "Copyright (c) 2024, University of Southampton"
__credits__ = ["Son Hoang"]
__licence__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Son Hoang"
__email__ = "T.S.Hoang@soton.ac.uk"
__status__ = "Prototype"

from maze import (  # type: ignore
    create_maze,
    get_dimensions,
    get_walls,
    add_horizontal_wall,
    add_vertical_wall,
)


def test_create_maze_get_dimensions() -> None:
    """A Unit test for :py:func:`~maze.create_maze` and
    :py:func:`~maze.get_dimensions`.

    Below is the test sequence:

    1. Create a maze of size (11, 5).

    2. Assert the width (11) and height (5) of the newly created maze.
    created runner.
    """
    maze = create_maze(11, 5)
    width, height = get_dimensions(maze)
    assert width == 11
    assert height == 5


def test_create_maze_get_walls() -> None:
    """A Unit test for :py:func:`~maze.create_maze` and
    :py:func:`~maze.get_walls`

    Below is the test sequence:

    1. Create a maze of size (11, 5).

    2. Assert that there are no walls at the (4, 2)-coordinate.
    """
    maze = create_maze(11, 5)
    assert get_walls(maze, 4, 2) == (False, False, False, False)


def test_add_horizontal_wall() -> None:
    """A Unit test for :py:func:`~maze.add_horizontal_wall` and
    :py:func:`~maze.get_walls`

    Below is the test sequence:

    1. Create a maze of size (11, 5).

    2. Add a horizontal wall at (5, 2).

    4. Assert that there are no walls at the (5, 2)-coordinate, except the South.
    """
    maze = create_maze(11, 5)
    maze = add_horizontal_wall(maze, 5, 2)

    assert get_walls(maze, 5, 2) == (False, False, True, False)


def test_add_vertical_wall() -> None:
    """A Unit test for :py:func:`~maze.add_vertical_wall` and
    :py:func:`~maze.get_walls`

    Below is the test sequence:

    1. Create a maze of size (11, 5).

    2. Add a vertical wall at (2, 4).

    3. Assert that there are no walls at the (4, 2)-coordinate, except the West.
    """
    maze = create_maze(11, 5)
    maze = add_vertical_wall(maze, 2, 4)
    assert get_walls(maze, 4, 2) == (False, False, False, True)


# my additional tests:
def test_create_default_maze() -> None:
    """A Unit test for :py:func:`~maze.create_maze
    and :py:func:`~maze.get_dimensions`
    Below is the test sequence:
    1. Create a maze of default size
    2. get dimensions
    3. assert get_dimensions(maze) == (5, 5)
    """

    maze = create_maze()
    width, height = get_dimensions(maze)
    assert width == 5
    assert height == 5


def test_external_walls() -> None:
    """A Unit test for :py:func:`~maze.create_maze
    and :py:func:`~maze.get_walls`
    Below is the test sequence:
    1. Create a maze of size (5, 4)
    2. assert get_walls for specific values
    """

    maze = create_maze(5, 4)

    # bottom left corner, south and west walls
    assert get_walls(maze, 0, 0)[2] == True
    assert get_walls(maze, 0, 0)[3] == True

    # top edge, north wall
    assert get_walls(maze, 2, 3)[0] == True


def test_add_wall_effects() -> None:
    """A Unit test for :py:func:`~maze.create_maze
    and :py:func:`~maze.add_horizontal_wall`
    Below is the test sequence:
    1. Create a maze of size (6, 6)
    2. Add a horizontal wall at (3, 2)
    3. assert get_walls for specific values."""

    maze = create_maze(6, 6)
    maze = add_horizontal_wall(maze, 3, 2)

    # check different coordinate
    assert get_walls(maze, 1, 1) == (False, False, False, False)
