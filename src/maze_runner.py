"""
maze_runner.py modul for the maze

This module finds the shortest path, reads files to display
the maze from them and provides a command line interface.
Validation for the files is also done raising errors
when necessary.
"""

from typing import Tuple, Optional, List
import argparse


from maze import create_maze, add_horizontal_wall, add_vertical_wall
from runner import create_runner, explore


def shortest_path(
    maze: dict,
    starting: Optional[Tuple[int, int]] = None,
    goal: Optional[Tuple[int, int]] = None,
) -> List[Tuple[int, int, str]]:
    """
    finds the shortest path between starting and goal

    left hug algorithm is used to find the shortest path between
    starting and goal, using the explore function. The repetitions
    are removed from the list to find minimal path.

    :param maze: maze as a dictionary
    :param starting: tuple of the starting coordinates
    :param goal: tuple of the goal coordinates
    :return: list of tuples
    """

    if starting is None:
        starting = (0, 0)

    if goal is None:
        goal = (maze["width"] - 1, maze["height"] - 1)

    # create new runner at the starting position
    runner = create_runner(starting[0], starting[1], "N")

    # explore maze using left hug algorithm
    explored = explore(runner, maze, goal)

    # stack holds the minimal path
    stack = []
    seen = {}

    # cycles removed to display teh minimal path
    for x, y, action in explored:
        position = (x, y)

        if position in seen:
            last_index = seen[position]

            while len(stack) > last_index + 1:
                removed = stack.pop()
                seen.pop((removed[0], removed[1]))

        else:
            stack.append((x, y, action))
            seen[position] = len(stack) - 1

    return stack


def maze_reader(maze_file: str) -> dict:
    """
    reads a maze from a file

    A maze is read from a file where validation is done.
    The maze format is validated, consistent dimensions
    validated, checks external walls and checks internal
    wall positions.

    :param maze_file: name of the file
    :return: maze as a dictionary
    """
    try:
        # opening file in read mode
        with open(maze_file, "r") as file:
            # stripping all the lines
            read_lines = [line.rstrip("\n") for line in file]

    except FileNotFoundError:
        raise IOError(f"File {maze_file} not found.")

    if not read_lines:
        raise ValueError(f"{maze_file} is empty.")

    ascii_width = len(read_lines[0])
    ascii_height = len(read_lines)

    # validating all lines of same length
    for line in read_lines:
        if len(line) != ascii_width:
            raise ValueError(f"{maze_file} has missing data.")

    # maze ascii has odd dimensions
    if ascii_height % 2 == 0 or ascii_width % 2 == 0:
        raise ValueError("Maze dimensions are invalid")

    width = (ascii_width - 1) // 2
    height = (ascii_height - 1) // 2

    maze = create_maze(width, height)

    # validating top and bottom external walls
    if any(c != "#" for c in read_lines[0]) or any(c != "#" for c in read_lines[-1]):
        raise ValueError(f"{maze_file} is invalid: external walls are invalid")

    # validating left and right external walls
    for line in read_lines:
        if line[0] != "#" or line[-1] != "#":
            raise ValueError(f"{maze_file} is invalid: external walls are invalid")

    # making the internal wall set
    for y in range(height):
        for x in range(width):

            horizontal_line = 2 * y
            horizontal_character = 2 * x + 1

            if horizontal_line + 1 < ascii_height:
                if read_lines[horizontal_line][horizontal_character] == "#":
                    add_horizontal_wall(maze, x, y + 1)

            vertical_line = 2 * y + 1
            vertical_character = 2 * x + 2

            if vertical_line < ascii_height:
                if vertical_character < ascii_width:
                    if read_lines[vertical_line][vertical_character] == "#":
                        add_vertical_wall(maze, x + 1, y)

    return maze


def main() -> None:
    """
    running the maze runner from the command line

    This function loads maze file, gets the start and goal coordinates, finds
    the shortest path between starting and goal, and then writes
    to the exploration and statistic files.

    :return: None
    """
    parser = argparse.ArgumentParser(description="ECS Maze Runner")
    parser.add_argument("maze", help="The name of the maze file, e.g., maze1.mz")
    parser.add_argument(
        "--starting", help="The starting position, e.g., '2, 1'", default=None
    )
    parser.add_argument("--goal", help="The goal position, e.g., '4, 5' ", default=None)

    args = parser.parse_args()

    try:
        maze = maze_reader(args.maze)

        # processing the optional starting argument
        if args.starting is not None:
            try:
                x, y = args.starting.split(",")
                starting = (int(x), int(y))

            except:
                raise ValueError("Invalid starting position")

            if not (
                0 <= starting[0] < maze["width"] and 0 <= starting[1] < maze["height"]
            ):
                raise ValueError("Invalid starting position")

        else:
            starting = None

        # processing the optional goal argument
        if args.goal is not None:
            try:
                x, y = args.goal.split(",")
                goal = (int(x), int(y))

            except:
                raise ValueError("Invalid goal position")

            if not (0 <= goal[0] < maze["width"] and 0 <= goal[1] < maze["height"]):
                raise ValueError("Invalid goal position")

        else:
            goal = None

        # finds shortest path
        path = shortest_path(maze, starting, goal)

        # printing the path for the user
        for a in path:
            print(a)

    except:
        raise ValueError

    # generating exploration path
    runner = create_runner(starting[0], starting[1], "N")
    explored = explore(runner, maze, goal)

    # writing to exploration file
    with open("exploration.csv", "w") as file:
        file.write("Step,x-coordinate,y-coordinate,Actions\n")
        for a, (x, y, action) in enumerate(explored, start=1):
            file.write(f"{a},{x},{y},{action}\n")

    exploration_steps = len(explored)
    path_length = len(path)
    score = exploration_steps / 4 + path_length

    # writing to statistics file
    with open("statistics.txt", "w") as file:
        file.write(f"{args.maze}\n")
        file.write(f"{score}\n")
        file.write(f"{exploration_steps}\n")
        file.write(f"{path}\n")
        file.write(f"{path_length}\n")


if __name__ == "__main__":
    main()
