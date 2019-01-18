from content.color import Color


def create_empty_row(width):
    return [Color.BLACK.value] * width


def grid_iterator(rows_count, columns_count):
    for row_num in range(rows_count):
        for column_num in range(columns_count):
            yield row_num, column_num
