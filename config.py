TITLE = 'Tetris'

FONT_FAMILY = 'arial'
FONT_SIZE = 60

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
FIELD_WIDTH = 300  # meaning 300 // 10 = 30 width per block
FIELD_HEIGHT = 600  # meaning 600 // 20 = 20 height per block
BLOCK_SIZE = 30
BORDER_SIZE = 4

GRID_HEIGHT = FIELD_HEIGHT / BLOCK_SIZE
GRID_WIDTH = FIELD_WIDTH / BLOCK_SIZE

TOP_LEFT_X = (SCREEN_WIDTH - FIELD_WIDTH) // 2
TOP_LEFT_Y = SCREEN_HEIGHT - FIELD_HEIGHT
