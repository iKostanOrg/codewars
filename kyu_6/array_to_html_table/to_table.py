#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

TABLE: dict = {
    'start': '<table>',
    'end': '</table>',
    'head': {
        'start': '<thead>',
        'end': '</thead>'
    },
    'header': {
        'start': '<th>',
        'end': '</th>'
    },
    'body': {
        'start': '<tbody>',
        'end': '</tbody>'
    },
    'row': {
        'start': '<tr>',
        'end': '</tr>'
    },
    'column': {
        'start': '<td>',
        'end': '</td>'
    },
}


def to_table(data: list, header: bool = False, index: bool = False) -> str:
    """
    Takes three arguments: data, headers, index, and returns
    a string containing HTML tags representing the table.
    :param data: a 2D array (list)
    :param header: an optional boolean value. If True, the first row of
                   the array is considered a header, defaults to False
    :param index: an optional boolean value. If False, the first column
                  in the table should contain 1-based indices of the
                  corresponding row. If headers arguments is True, this
                  column should have empty header. Defaults to False.
    :return: a string containing HTML tags representing the table.
    """
    rows_and_columns: str = ''

    for i, row in enumerate(data):

        if header and i == 0:
            rows_and_columns = '{}{}{}'.format(rows_and_columns,
                                               TABLE['head']['start'],
                                               TABLE['row']['start'])
            if index:
                rows_and_columns = '{}{}{}'.format(rows_and_columns,
                                                   TABLE['header']['start'],
                                                   TABLE['header']['end'])

            for b, col in enumerate(row):
                rows_and_columns = '{}{}{}{}'.format(rows_and_columns,
                                                     TABLE['header']['start'],
                                                     col,
                                                     TABLE['header']['end'])

            rows_and_columns = '{}{}{}'.format(rows_and_columns,
                                               TABLE['row']['end'],
                                               TABLE['head']['end'])
        else:
            if TABLE['body']['start'] not in rows_and_columns:
                rows_and_columns = '{}{}'.format(rows_and_columns,
                                                 TABLE['body']['start'])

            rows_and_columns = '{}{}'.format(rows_and_columns,
                                             TABLE['row']['start'])

            if index:
                rows_and_columns = '{}{}{}{}'.format(rows_and_columns,
                                                     TABLE['column']['start'],
                                                     i if header else i + 1,
                                                     TABLE['column']['end'])

            for col in row:
                rows_and_columns = '{}{}{}{}'.format(rows_and_columns,
                                                     TABLE['column']['start'],
                                                     '' if col is None else col,
                                                     TABLE['column']['end'])

            rows_and_columns = '{}{}'.format(rows_and_columns,
                                             TABLE['row']['end'])

    return '{}{}{}{}'.format(TABLE['start'],
                             rows_and_columns,
                             TABLE['body']['end'],
                             TABLE['end'])
