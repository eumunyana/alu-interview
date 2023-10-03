0. Rain
1. 
Given a list of non-negative integers representing the heights of walls with unit width 1, as if viewing the cross-section of a relief map, calculate how many square units of water will be retained after it rains.

Prototype: def rain(walls)
walls is a list of non-negative integers.
Return: Integer indicating total amount of rainwater retained.
Assume that the ends of the list (before index 0 and after index walls[-1]) are not walls, meaning they will not retain water.
If the list is empty return 0.

Visual representation of the walls [0, 1, 0, 2, 0, 3, 0, 4]
![image](https://github.com/eumunyana/alu-interview/assets/116874050/f78f007a-ec35-44f1-94ff-5551dd42c804)

Visual representation of the walls [2, 0, 0, 4, 0, 0, 1, 0]
![image](https://github.com/eumunyana/alu-interview/assets/116874050/af8812ed-62f0-4850-bae7-d91059a10ba9)

