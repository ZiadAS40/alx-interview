#!/usr/bin/python3
""" the famous problem pascal triangle """

def pascal_triangle(n):
    """the pascal trangle"""

    if n <= 0:
        return []

    curr_list = [1]
    traingle = []
    for l in range(0, n):
        new_list = curr_list[:]
        traingle.insert(l, new_list)
        curr_list.insert(0, 0)
        curr_list.append(0)

        new_list = []
        for n in range(0, len(curr_list) - 1):
            new_list.insert(n, curr_list[n] + curr_list[n + 1])
        curr_list = new_list

    return traingle
