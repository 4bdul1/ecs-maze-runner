"""
maze.py module for the maze

This module creates a maze, adds walls to the maze, allows
access to the walls and dimensions.

"""

from typing import Tuple


def create_maze(width: int = 5, height: int = 5) -> dict:
    """
    creates a maze with the given width and height

    :param width: integer value for the width of the maze
    :param height: integer value for the height of the maze
    :return: maze as a dictionary
    """

    maze = {
        "width": width,
        "height": height,
        "horizontal_wall": set(),
        "vertical_wall": set(),
    }

    return maze


def add_horizontal_wall(maze: dict, x_coordinate: int, horizontal_line: int) -> dict:
    """
    adds a horizontal wall to the maze

    :param maze: maze as a dictionary
    :param x_coordinate: integer value for the x coordinate of the wall
    :param horizontal_line: integer value for the horizontal line of the wall
    :return: updated maze as a dictionary
    """
    maze["horizontal_wall"].add((x_coordinate, horizontal_line))

    return maze


def add_vertical_wall(maze: dict, y_coordinate: int, vertical_line: int) -> dict:
    """
    adds a vertical wall to the maze

    :param maze: maze as a dictionary
    :param y_coordinate: integer value for the y coordinate of the wall
    :param vertical_line: integer value for the vertical line of the wall
    :return: updated maze as a dictionary
    """
    maze["vertical_wall"].add((vertical_line, y_coordinate))

    return maze


def get_dimensions(maze: dict) -> Tuple[int, int]:
    """
    returns the dimensions of the maze

    :param maze: maze as a dictionary
    :return: tuple of the dimensions of the maze
    """
    dimensions = (maze["width"], maze["height"])

    return dimensions


def get_walls(
    maze: dict, x_coordinate: int, y_coordinate: int
) -> Tuple[bool, bool, bool, bool]:
    """
    returns whether the walls exist around a cell at given coordinates

    :param maze: maze as a dictionary
    :param x_coordinate: integer value for the x coordinate of the cell
    :param y_coordinate: integer value for the y coordinate of the cell
    :return: tuple of boolean values for the walls exist
    """

    # all bool set to false to start with
    north = False
    east = False
    south = False
    west = False

    # checks for wall on the north
    if (
        y_coordinate == maze["height"] - 1
        or (x_coordinate, y_coordinate + 1) in maze["horizontal_wall"]
    ):
        north = True

    # checks for wall on the east
    if (
        x_coordinate == maze["width"] - 1
        or (x_coordinate + 1, y_coordinate) in maze["vertical_wall"]
    ):
        east = True

    # checks for walls on the south
    if y_coordinate == 0 or (x_coordinate, y_coordinate) in maze["horizontal_wall"]:
        south = True

    # checks for walls on the west
    if x_coordinate == 0 or (x_coordinate, y_coordinate) in maze["vertical_wall"]:
        west = True

    return north, east, south, west
