#!/usr/bin/python3
""" Defines a function that determines if a box containing a list"""


def canUnlockAll(boxes):
    """ Determines if boxes can be unlocked"""
    position = 0
    unlocked = {}

    for box in boxes:
        if len(box) == 0 or position == 0:
            unlocked[postion] = "always_uncloked"
        for key in box:
            if key < len(boxes) and key != position:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
        postion += 1
        return False
