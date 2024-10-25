# Sports League Table Ranking

<!-- markdownlint-disable MD013 -->
`Note`: There is a harder version [(Sports League Table Ranking (with Head-to-head))](https://www.codewars.com/kata/5e0e17220d5bc9002dc4e9c4) of this.
<!-- markdownlint-enable MD013 -->

## Description

You organize a sports league in a round-robin-system. Each team meets all
other teams. In your league a win gives a team 2 points, a draw gives both
teams 1 point. After some games you have to compute the order of the teams
in your league. You use the following criteria to arrange the teams:

*   Points
*   Scoring differential (the difference between goals scored and those conceded)
*   Goals scored

First you sort the teams by their points. If two or more teams reached the
same number of points, the second criteria comes into play and so on. Finally,
if all criteria are the same, the teams share a place.

### Input

*   `number`: Number of teams in your league.
*   `games`: An array of arrays. Each item represents a played game with an
* array of four elements `[TeamA,TeamB,GoalA,GoalB]` (TeamA played against
* TeamB and scored GoalA goals and conceded GoalB goals ).

### Output

positions: An array of positions. The i-th item should be the position of
the i-th team in your league.

### Example

```text
number = 6
games = [[0, 5, 2, 2],   // Team 0 - Team 5 => 2:2
         [1, 4, 0, 2],   // Team 1 - Team 4 => 0:2
         [2, 3, 1, 2],   // Team 2 - Team 3 => 1:2
         [1, 5, 2, 2],   // Team 1 - Team 5 => 2:2
         [2, 0, 1, 1],   // Team 2 - Team 0 => 1:1
         [3, 4, 1, 1],   // Team 3 - Team 4 => 1:1
         [2, 5, 0, 2],   // Team 2 - Team 5 => 0:2
         [3, 1, 1, 1],   // Team 3 - Team 1 => 1:1
         [4, 0, 2, 0]]   // Team 4 - Team 0 => 2:0
```

You may compute the following table:

```text
Rank	Team	For : Against	GD	Points
1.	    Team 4	5 : 1	        +4	5
2.	    Team 5	6 : 4	        +2	4
3.	    Team 3	4 : 3	        +1	4
4.	    Team 0	3 : 5	        -2	2
4.	    Team 1	3 : 5	        -2	2
6.	    Team 2	2 : 5	        -3	1
```

Team 5 and Team 3 reached the same number of points. But since Team 5 got a
better scoring differential, it ranks better than Team 3. All values of Team
0 and Team 1 are the same, so these teams share the fourth place.

In this example you have to return the array `[4, 4, 6, 3, 1, 2].`

[Source](https://www.codewars.com/kata/5e0baea9d772160032022e8c)
