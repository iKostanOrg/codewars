# Array to HTML table

The task is simple - given a 2D array (list), generate an HTML
table representing the data from this array.

You need to write a function called `to_table`/`toTable`, that
takes three arguments:

-   `data` - a 2D array (list),
-   `headers` - an optional boolean value. If `True`, the first row
     of the array is considered a header. Defaults to False,
-   `index` - an optional boolean value. If `True`, the first column
     in the table should contain 1-based indices of the corresponding row.
     If `headers` arguments is `True`, this column should have empty header.
     Defaults to False.

and returns a string containing HTML tags representing the table.

HTML table is structured like this:

```html
<table>
  <thead>                 <!-- an optional table header -->
    <tr>                  <!-- a header row -->
      <th>header1</th>    <!-- a single header cell -->
      <th>header2</th>
    </tr>
  </thead>
  <tbody>                 <!-- a table's body -->
    <tr>                  <!-- a table's row -->
      <td>row1, col1</td> <!-- a row's cell -->
      <td>row1, col2</td>
    </tr>
    <tr>
      <td>row2, col1</td>
      <td>row2, col2</td>
    </tr>
  </tbody>
</table>
```

The table header is optional. If `header` argument is `False` then the
table starts with `<tbody>` tag, ommiting `<thead>`.

So, for example:

```text
to_table([["lorem", "ipsum"], ["dolor", "sit amet"]], True, True)
```

returns
<!-- markdownlint-disable MD013 -->

```html
<table><thead><tr><th></th><th>lorem</th><th>ipsum</th></tr></thead><tbody><tr><td>1</td><td>dolor</td><td>sit amet</td></tr></tbody></table>
```
<!-- markdownlint-enable MD013 -->

As you can see, no linebreaks or whitespaces (except for the ones present
in the array values) are included, so the HTML code is minified.

**IMPORTANT NOTE:** if the value in the array happens to be `None`, the
value of the according cell in the table should be en empty string (`""`)!
Otherwise, just use a string representation of the given value, so, dependent
on the language, the output can be slightly different. No additional parsing
is needed on the data.

For your convenience, there is a preloaded function `esc_html/escHtml` that
takes a string with HTML tags and escape them; it is necessary if you want to
use `print/console.log` on your resulting strings, else Codewars processes HTML
tags, so they appear invisible in the stdout.

Test cases will always provide valid data, that is - up to three arguments, first
a NxM array (list) with N and M > 0, second and third a boolean. The values in the
array will always be either `string`, `number`, `bool` or `None/null`.

For more examples, see test cases.

P.S.: I understand, that with larger inputs checking for mismatches in the expected
and actual output can be cumbersome, but as of now I can hardly come up with something
that would make this easier. Any ideas would be helpful!

[Source](https://www.codewars.com/kata/5e7e4b7cd889f7001728fd4a)