# Did I Finish my Sudoku

Write a function `done_or_not/DoneOrNot` passing a board `(list[list_lines])` as parameter. If the board is valid return 'Finished!', otherwise return 'Try again!'

## Sudoku rules

Complete the Sudoku puzzle so that each and every row, column, and region contains the numbers one through nine only once.

### Rows

<div align="center"> 
<img width="90%" height="90%" src="https://github.com/ikostan/codewars/blob/master/img/Row.gif" hspace="20">
</div>

There are `9` rows in a traditional Sudoku puzzle. Every row must contain the numbers `1, 2, 3, 4, 5, 6, 7, 8, and 9`. There may not be any duplicate numbers in any row. In other words, there can not be any rows that are identical.

In the illustration the numbers `5, 3, 1, and 2` are the "givens". They can not be changed. The remaining numbers in black are the numbers that you fill in to complete the row.

### Columns

<div align="center"> 
<img width="90%" height="90%" src="https://github.com/ikostan/codewars/blob/master/img/Column.gif" hspace="20">
</div>

There are 9 columns in a traditional Sudoku puzzle. Like the Sudoku rule for rows, every column must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Again, there may not be any duplicate numbers in any column. Each column will be unique as a result.

In the illustration the numbers 7, 2, and 6 are the "givens". They can not be changed. You fill in the remaining numbers as shown in black to complete the column.

### Regions

<div align="center"> 
<img width="90%" height="90%" src="https://github.com/ikostan/codewars/blob/master/img/Region.gif" hspace="20">
</div>

A region is a 3x3 box like the one shown to the left. There are 9 regions in a traditional Sudoku puzzle.

Like the Sudoku requirements for rows and columns, every region must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Duplicate numbers are not permitted in any region. Each region will differ from the other regions.

In the illustration the numbers 1, 2, and 8 are the "givens". They can not be changed. Fill in the remaining numbers as shown in black to complete the region.

Valid board example:

<div align="center"> 
<img width="90%" height="90%" src="https://github.com/ikostan/codewars/blob/master/img/Sudoku_solution.png" hspace="20">
</div>

For those who don't know the game, here are some information about rules and how to play [Sudoku](http://en.wikipedia.org/wiki/Sudoku) and [here.](http://www.sudokuessentials.com/)

[Source](https://www.codewars.com/kata/53db96041f1a7d32dc0004d2/train/python)