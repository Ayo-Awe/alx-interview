# Lockboxes

You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

- Prototype: def canUnlockAll(boxes)
- boxes is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
  - There can be keys that do not have boxes
- The first box boxes[0] is unlocked
- Return True if all boxes can be opened, else return False

## Algorithm

visted - A list of visted boxes/ used keys
queue - A list of keys to be checked
available boxes = A list of boxes

Initialise: queue = [0], visited = []

- While queue is not empty

  - Take a key from the key
  - Check if key has a box
    - no => skip key
    - yes => Check if box with key has been visited
      - yes => skip key
      - no => Add keys in box to queue and add box to visited boxes

- is visted boxes equal to available boxes
  - yes => return true
  - no => return false
