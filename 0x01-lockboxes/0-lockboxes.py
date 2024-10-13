#!/usr/bin/python3
"""locked boxes"""


def canUnlockAll(boxes):
    """
    a method that determines if all the boxes can be opened.
    """
    visited = []
    keys = {0}

    for n in range(0, len(boxes)):
        if n not in visited and n in keys:

            def visit(box):
                """
                define the function to visit the boxes
                """
                visited.append(box)
                keys.update(boxes[box])

            visit(n)

            new_keys = keys - set(visited)
            if new_keys:
                for key in new_keys:
                    visit(key)

    if len(visited) is len(boxes):
        return True
    else:
        return False
