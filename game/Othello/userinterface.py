

import tkinter
import board

class OthelloApplication:

    def __init__(self):

        self._root_window = tkinter.Tk()
        self._board = board.Board._get_board(board.Board())

##        self._button.pack()




    def _start(self):
        self._root_window.mainloop()



if __name__ == '__main__':
    app = OthelloApplication()
    app._start()