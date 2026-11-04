"""
Created on Wed Nov 20 16:01:45 2024
"""

__author__ = "Son Hoang"
__copyright__ = "Copyright (c) 2024, University of Southampton"
__credits__ = ["Son Hoang"]
__licence__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Son Hoang"
__email__ = "T.S.Hoang@soton.ac.uk"
__status__ = "Prototype"

from maze import create_maze, add_horizontal_wall, add_vertical_wall  # type: ignore
from maze_runner import shortest_path  # type: ignore


def test_shortest_path() -> None:
    """A Unit test for :py:func:`~maze_runner.shortest_path`

    Below is the test sequence:

    1. Create a maze of size (11, 5).

    2. Add a horizontal wall at (0, 1).

    3. Add a vertical wall at (1, 1).

    4. Run short_path function to get the path (with default start and goal).

    5. Check that the result is a valid path, starting from (0,0) and end at
       (10, 4).
    """
    maze = create_maze(11, 5)
    maze = add_horizontal_wall(maze, 0, 1)
    maze = add_vertical_wall(maze, 1, 1)
    path = shortest_path(maze)
    assert path[0] == (0, 0, "RF")
    assert path[-1] == (9, 4, "F")
    prefix = []
    for location in path:
        x, y, a = location
        assert (x, y) not in prefix, f"{location} is repeated"
        prefix.append((x, y))


'''
def test_shortest_path_custom() -> None:
    """A Unit test for :py:func:`~maze_runner.shortest_path`
    Below is the test sequence:
    1. Create a maze of size (6, 6).
    2. Set custom starting and goal
    3. assert first entry and last entry"""

    maze = create_maze(6, 6)

    path = shortest_path(maze, starting=(1, 1), goal=(4, 4))

    assert path[0][0:2] == (1, 1)

    last_x, last_y, action = path[-1]
    assert abs(last_x - 4) + abs(last_y - 4) == 1
'''


def test_shortest_path_excludes_goal() -> None:
    """A Unit test for :py:func:`~maze_runner.shortest_path`
    Below is the test sequence:
    1. Create a maze of size (5, 5).
    2. Find shortest path starting from (0,0)
    3. assert final path excludes goal"""

    maze = create_maze(5, 5)
    path = shortest_path(maze)

    assert (4, 4) not in [(x, y) for x, y, _ in path]


def test_shortest_path_empty_maze() -> None:
    """A Unit test for :py:func:`~maze_runner.shortest_path`
    Below is the test sequence:
    1. Create a maze of size (4, 3)
    2. Find shortest path starting from (0,0)
    3. assert final path starts with (0,0)
    4. assert final path ends adjacent to the goal"""

    maze = create_maze(4, 3)
    path = shortest_path(maze)

    # Must start at (0,0)
    assert path[0][0:2] == (0, 0)

    # Must reach cell adjacent to (3,2)
    x, y, _ = path[-1]
    assert abs(x - 3) + abs(y - 2) == 1
