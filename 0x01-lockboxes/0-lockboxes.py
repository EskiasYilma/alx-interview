#!/usr/bin/python3
"""
A function that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    A function that determines if all the boxes can be opened
    """
    n = len(boxes)
    visited_boxes = set()
    queued_boxes = [0]

    for box in queued_boxes:
        if box in visited_boxes:
            continue

        visited_boxes.add(box)
        keys = boxes[box]

        for key in keys:
            if key < n:
                queued_boxes.append(key)

    return len(visited_boxes) == n
