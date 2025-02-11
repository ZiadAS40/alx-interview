#!/usr/bin/python3
""" the famous problem pascal triangle """
import copy


def pascal_triangle(n):
    """the pascal trangle"""

    if n <= 0:
        return []

    curr_list = [1]
    traingle = []
    for l in range(0, n):
        traingle.insert(l, copy.deepcopy(curr_list))
        curr_list.insert(0, 0)
        curr_list.append(0)

        new_list = []
        for n in range(0, len(curr_list) - 1):
            new_list.insert(n, curr_list[n] + curr_list[n + 1])
        curr_list = new_list

    return traingle
