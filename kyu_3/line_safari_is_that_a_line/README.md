# Line Safari - Is that a line

## Kata Task

You are given a grid, which always includes exactly two end-points
indicated by `X`.

You simply need to return true/false if you can detect a one and
only one "valid" line joining those points.

A line can have the following characters :

*   `-` = left / right
*   `|` = up / down
*   `+` = corner

## Rules for valid lines

*   The most basic kind of valid line is when the end-points are
already adjacent

```text
X
X
XX
```

*   The corner character (+) must be used for all corners (but only for corners).
*   It must be possible to follow the line with no ambiguity (lookahead of
    just one step, and never treading on the same spot twice).
*   The line may take any path between the two points.
*   Sometimes a line may be valid in one direction but not the other. Such a line
    is still considered valid.
*   Every line "character" found in the grid must be part of the line. If extras
    are found then the line is not valid.

## Examples

### Good lines

```text
X---------X
X
|
|
X

   +--------+
X--+        +--+
               |
               X
               
   +-------------+
   |             |
X--+      X------+    

   +-------+
   |      +++---+
X--+      +-+   X
```

### Bad lines

```text
X-----|----X
X
|
+
X
   |--------+
X---        ---+
               |
               X
   +------ 
   |              
X--+      X  
      +------+
      |      |
X-----+------+
      |
      X
```

### Hint

Imagine yourself walking a path where you can only see your very next step.
Can you know which step you must take, or not?

[Source](https://www.codewars.com/kata/59c5d0b0a25c8c99ca000237)