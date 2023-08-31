#!/usr/bin/python3

"""This module contains code for the
island-perimeter alx-interview question
"""


def island_perimeter(grid):
    """Returns the perimeter of the island
    described in grid
    """

    bottom_boundary = len(grid)-1
    right_boundary = len(grid[0])-1

    # loop over grid from top to bottom, left to right

    perimeter = 0

    for y_pos, row in enumerate(grid):
        for x_pos, value in enumerate(row):

            if value == 0:
                continue

            perimeter += 4

            right_neighbour = get_right_neighbour(
                x_pos, y_pos, grid, right_boundary)

            if right_neighbour == 1:
                perimeter -= 2

            bottom_neighbour = get_bottom_neighbour(
                x_pos, y_pos, grid, bottom_boundary)

            if bottom_neighbour == 1:
                perimeter -= 2

    return perimeter


def get_right_neighbour(x_pos, y_pos,  grid, right_boundary):
    """Returns the adjacent cell to the right of
    the current cell
    """

    if right_boundary > x_pos:
        return grid[y_pos][x_pos+1]

    return None


def get_bottom_neighbour(x_pos, y_pos,  grid, bottom_boundary):
    """Returns the adjacent cell to the bottom of
    the current cell
    """

    if bottom_boundary > y_pos:
        return grid[y_pos+1][x_pos]

    return None
