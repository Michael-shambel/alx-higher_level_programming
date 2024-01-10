#!/usr/bin/python3
"""pascal triangle function"""


def pascal_triangle(n):
    """define pascal triangle representation in size of n"""

    if n < 0:
        return []

    tria = [[1]]

    for i in range(1, n):
        pr_row = tria[-1]
        new_row = [1]

        for j in range(1, i):
            new_row.append(pr_row[j - 1] + pr_row[j])

        new_row.append(1)
        tria.append(new_row)

    return tria
