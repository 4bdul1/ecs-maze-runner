"""
Runner.py module for the maze

This module creates a runner, allows access to the
runners x and y-coordinates, runners orientation, allows
the runner to turn, move forward, sense around walls, go
straight, move and explore.

"""

from typing import Tuple, Optional, List

import maze as mazeModule


def create_runner(x: int = 0, y: int = 0, orientation: str = "N") -> dict:
    """
    Creates a runner with given parameters.

    :param x: the x-coordinate
    :param y: the y-coordinate
    :param orientation: the direction runner faces e.g. N, S, E, W
    :return: runner as a dictionary
    """
    runner = {"x": x, "y": y, "orientation": orientation}

    return runner


def get_x(runner: dict) -> int:
    """returns the runners x-coordinate"""

    return runner["x"]


def get_y(runner: dict) -> int:
    """returns the runners y-coordinate"""

    return runner["y"]


def get_orientation(runner: dict) -> str:
    """returns the runners orientation"""
    return runner["orientation"]


def turn(runner: dict, direction: str) -> dict:
    """
    Turns the runner direction according to the given direction e.g. right or left

    :param runner: runner as a dictionary
    :param direction: left or right
    :return: runner as a dictionary
    """

    left_orientation = {"N": "W", "E": "N", "S": "E", "W": "S"}
    right_orientation = {"N": "E", "E": "S", "S": "W", "W": "N"}

    # change orientation depending on the direction passed
    if direction == "Left":
        runner["orientation"] = left_orientation[runner["orientation"]]

    elif direction == "Right":
        runner["orientation"] = right_orientation[runner["orientation"]]

    return runner


def forward(runner: dict) -> dict:
    """
    moves the runner forward one unit

    :param runner: runner as a dictionary
    :return: runner as a dictionary
    """

    # increment or decrement position based on orientation
    if runner["orientation"] == "N":
        runner["y"] += 1

    elif runner["orientation"] == "E":
        runner["x"] += 1

    elif runner["orientation"] == "S":
        runner["y"] -= 1

    elif runner["orientation"] == "W":
        runner["x"] -= 1

    return runner


def sense_walls(runner: dict, maze: dict) -> Tuple[bool, bool, bool]:
    """
    checks for walls around the runner

    :param runner: runner as a dictionary
    :param maze: maze as a dictionary
    :return: a tuple of booleans for walls around the runner
    """

    current_walls = mazeModule.get_walls(maze, runner["x"], runner["y"])
    """
    north = {"N": "front", "E": "right", "S": "back", "W": "left"}
    east = {"N": "left", "E": "front", "S": "right", "W": "back"}
    south = {"N": "back", "E": "left", "S": "front", "W": "right"}
    west = {"N": "right", "E": "back", "S": "left", "W": "front"}
    """
    # determines left, front and right using the notes and logic above
    walls = ()
    if runner["orientation"] == "N":
        walls = (current_walls[3], current_walls[0], current_walls[1])

    elif runner["orientation"] == "E":
        walls = (current_walls[0], current_walls[1], current_walls[2])

    elif runner["orientation"] == "S":
        walls = (current_walls[1], current_walls[2], current_walls[3])

    elif runner["orientation"] == "W":
        walls = (current_walls[2], current_walls[3], current_walls[0])

    return walls


def go_straight(runner: dict, maze: dict) -> dict:
    """
    moves the runner straight one unit if no walls around the runner

    :param runner: runner as a dictionary
    :param maze: maze as a dictionary
    :return: updated_runner as a dictionary
    """
    walls = sense_walls(runner, maze)

    # walls[1] is bool of a wall infront
    if not (walls[1]):
        updated_runner = forward(runner)

    else:
        raise ValueError("Wall straight ahead")

    return updated_runner


def move(runner: dict, maze: dict) -> Tuple[dict, str]:
    """
    uses the left hug alogorithm to move the runner

    :param runner: runner as a dictionary
    :param maze: maze as a dictionary
    :return: tuple of runner as a dictionary and actions of what the runner did
    """
    walls = sense_walls(runner, maze)
    actions = ""

    # trys left first
    if not (walls[0]):
        runner = turn(runner, "Left")
        actions += "L"
        runner = forward(runner)
        actions += "F"

    # trys front next
    elif not (walls[1]):
        runner = forward(runner)
        actions += "F"

    # trys right next
    elif not (walls[2]):
        runner = turn(runner, "Right")
        actions += "R"
        runner = forward(runner)
        actions += "F"

    # lastly tries back
    else:
        runner = turn(runner, "Left")
        runner = turn(runner, "Left")
        runner = forward(runner)
        actions += "B"

    return runner, actions


def explore(
    runner: dict, maze: dict, goal: Optional[Tuple[int, int]]
) -> List[Tuple[int, int, str]]:
    """
    explores the maze until runner reaches the goal

    move() is used to move the runner one unit at a time. The function
    returns a list of tuples.

    :param runner: runner as a dictionary
    :param maze: maze as a dictionary
    :param goal: tuple containing coordinates of the goal
    :return: list of tuples
    """

    # default goal is set to the top right of the maze
    if goal is None:
        goal = (maze["width"] - 1, maze["height"] - 1)

    movements = []

    # keeps exploring until goal is reached
    while (get_x(runner), get_y(runner)) != goal:

        current_x, current_y = get_x(runner), get_y(runner)
        runner, actions = move(runner, maze)
        movements.append((current_x, current_y, actions))

    return movements
