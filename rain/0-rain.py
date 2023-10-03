#!/usr/bin/python3
"""Calculating the square units of rain that will be retained after it rains:"""

def rain(walls):
    """Calculate how many square units of water
    will be retained"""
    if len(walls) == 0:
        return 0
    water = 0
    for i in range(1, len(walls) - 1):
        left = walls[i]
        for k in range(i):
            left = max(left, walls[k])
        right = walls[i]
        for k in range(i + 1, len(walls)):
            right = max(right, walls[k])
        water += min(left, right) - walls[i]
    return water

if __name__ == "__main__":
    walls = [0, 1, 0, 2, 0, 3, 0, 4]
    print(rain(walls))
    walls = [2, 0, 0, 4, 0, 0, 1, 0]
    print(rain(walls))
