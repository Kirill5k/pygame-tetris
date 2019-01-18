def field_cell_iterator(field):
    for row_number in range(len(field)):
        for cell_number in range(len(field[row_number])):
            yield row_number, cell_number
