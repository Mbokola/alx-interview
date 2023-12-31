#!/usr/bin/python3
""" 0-lockboxes module """


def canUnlockAll(boxes):
    """ Checks if all boxes can be unlocked """
    keys = [*boxes[0]]
    locked_boxes = []

    for count in range(1, len(boxes)):
        if (count in keys):
            keys += boxes[count]
        else:
            locked_boxes.append(count)

    for box in locked_boxes:
        if box not in keys:
            return False
        keys += boxes[box]
    return True
