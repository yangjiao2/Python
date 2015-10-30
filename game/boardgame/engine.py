import gamecode
import tkinter
import coordinate
import math

DOTS = []
##
WIDTH = 200
HEIGHT = 200
##
BLACKCOLOR = '#000000'
WHITECOLOR = '#FFFFFF'




class DotsApp:
    
    def _draw_one_disc(board, color, gap, pos):
        col = pos[0]
        row = pos[1]
        board.create_oval(gap *(col + 1), gap * (row + 1), gap * (col + 2), gap * (row + 2), fill = color, outline = BLACKCOLOR)
        return board



class Othello:
    def __init__(self, board, cols, rows, firstmove, topleft):      
        self._board = board
        self._cols = cols
        self._rows = rows
        self._turn = firstmove
        self._topleft = topleft
        self._logicboard = gamecode._get_new_board(self._turn, self._cols, self._rows, self._topleft)

    def _logic_board(self):
        return self._logicboard
    
    def _apply_discs_from_logic_board(self, board, logicboard):
        board_width = self._board.winfo_width()
        board_height = self._board.winfo_height()
        gapx = (board_width ) / (self._rows + 2)
        gapy = (board_height) / (self._cols + 2)
        self._gap = min(gapx, gapy)
        for col in range(self._cols):
            for row in range(self._rows):
                if gamecode._color_for_a_cell(logicboard, self._cols, self._rows, (col, row)) == 'b':
                    board = DotsApp._draw_one_disc(self._board, BLACKCOLOR, self._gap, (col, row))
                elif gamecode._color_for_a_cell(logicboard, self._cols, self._rows, (col, row)) == 'w':
                    board = DotsApp._draw_one_disc(self._board, WHITECOLOR, self._gap, (col, row))

        return self._board

    def _draw_initial_disc(self):
        self._board = self._apply_discs_from_logic_board(self._board, self._logicboard)

        

    def _draw_board(self):
        board_width = self._board.winfo_width()
        board_height = self._board.winfo_height()
        gapx = (board_width ) / (self._rows + 2)
        gapy = (board_height) / (self._cols + 2)
        self._gap = min(gapx, gapy)

        for i in range(1, self._cols + 1):
            self._board.create_rectangle(self._gap * i, self._gap, self._gap * (i + 1), self._gap * (self._rows + 1))
        for i in range(1, self._rows + 1):
            self._board.create_rectangle(self._gap, self._gap * i, self._gap * (self._cols + 1), self._gap * (i + 1))

        self._draw_initial_disc()
        return self._board


        

