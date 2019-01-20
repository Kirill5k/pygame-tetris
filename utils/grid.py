from content.color import Color


def create_empty_row(width):
    return [Color.BLACK] * width


def create_empty_rows(width, count):
    return [create_empty_row(width) for _ in range(count)]


def grid_iterator(columns_count, rows_count):
    for row_num in range(rows_count):
        for column_num in range(columns_count):
            yield row_num, column_num
