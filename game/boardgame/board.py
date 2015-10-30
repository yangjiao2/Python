import tkinter
import gamecode
import engine

BLACK = 'b'
WHITE = 'w'
##
WIDTH = 200
HEIGHT = 200
##
COLS = 6
ROWS = 6
##
FONT_WIDTH = 12
FONT = ("Helvetica", FONT_WIDTH)
##
BLACKCOLOR = '#000000'
WHITECOLOR = '#FFFFFF'
GRAY = '#C0C0C0'
DARKGRAY = '#808080'
BROWNCOLOR = '#855500'
##

class PopUpError:
    def __init__(self, errormessage):
            self._popup_window = tkinter.Toplevel()
            self._popup_window.title('Error')
            lack_of_information_label = tkinter.Label(master = self._popup_window, text = errormessage, font = FONT)
            lack_of_information_label.grid(row = 0, column = 0, sticky = tkinter.N + tkinter.W + tkinter.E + tkinter.S)
            lack_of_information_ok_button = tkinter.Button(master = self._popup_window, text = 'OK', font = FONT, command = self._lack_of_information_button_clicked)
            lack_of_information_ok_button.grid(sticky = tkinter.S, padx = 10, pady = 20)

    def _show_error(self):
        self._popup_window.grab_set()
        self._popup_window.wait_window()
        
    def _lack_of_information_button_clicked(self):
        self._popup_window.destroy()
        
class GetInfoWindow:
    def __init__(self):
        self._dialog_window = tkinter.Toplevel()
        self._dialog_window.title('Initalize the game')
        self._info = tkinter.Label(master = self._dialog_window, text = 'Please input new game information', font = FONT)
        self._info.grid(row = 0 , column = 0 , columnspan = 2, sticky = tkinter.W + tkinter.N)
        
        self._row_label = tkinter.Label(master = self._dialog_window, text = 'Column: (4 - 16)', font = FONT)
        self._row_label.grid(row = 1, column = 0, sticky = tkinter.W + tkinter.N)
        self._row_entry = tkinter.Entry(master = self._dialog_window, width = FONT_WIDTH, font = FONT)
        self._row_entry.grid(row = 1, column = 1, sticky = tkinter.W + tkinter.E)
        
        self._col_label = tkinter.Label(master = self._dialog_window, text = 'Row: (4 - 16)', font = FONT)
        self._col_label.grid(row = 2, column = 0, sticky = tkinter.W + tkinter.N)
        self._col_entry = tkinter.Entry(master = self._dialog_window, width = FONT_WIDTH, font = FONT)
        self._col_entry.grid(row = 2, column = 1, sticky = tkinter.W + tkinter.E)
        
        self._topleft_label = tkinter.Label(master = self._dialog_window, text = 'Top left color: ', font = FONT)
        self._topleft_label.grid(row = 3, column = 0, sticky = tkinter.W + tkinter.N)
        self._topleft_frame = tkinter.Frame(master = self._dialog_window)
        self._topleft_frame.grid(row = 3, column = 1, rowspan = 2, sticky = tkinter.W + tkinter.N, pady = 3)
        self._topleft_black_button = tkinter.Button(master = self._topleft_frame, text = 'Black', font = FONT, padx = 20, command = self._topleft_is_black)
        self._topleft_white_button = tkinter.Button(master = self._topleft_frame, text = 'White', font = FONT, padx = 20, command = self._topleft_is_white)
        self._topleft_black_button.grid(row = 0, column = 0, sticky = tkinter.W + tkinter.N, padx = 10)
        self._topleft_white_button.grid(row = 0, column = 1, sticky = tkinter.W + tkinter.N, padx = 10)
        
        self._firstmove_label = tkinter.Label(master = self._dialog_window, text = 'First move color: ', font = FONT)
        self._firstmove_label.grid(row = 5, column = 0, sticky = tkinter.W + tkinter.N)
        self._firstmove_frame = tkinter.Frame(master = self._dialog_window)
        self._firstmove_frame.grid(row = 5, column = 1, rowspan = 2, sticky = tkinter.W + tkinter.N, pady = 3)
        self._firstmove_black_button = tkinter.Button(master = self._firstmove_frame, text = 'Black', font = FONT, padx = 20, command = self._firstmove_is_black)
        self._firstmove_white_button = tkinter.Button(master = self._firstmove_frame, text = 'White', font = FONT, padx = 20, command = self._firstmove_is_white)
        self._firstmove_black_button.grid(row = 0, column = 0, sticky = tkinter.W + tkinter.N, padx = 10)
        self._firstmove_white_button.grid(row = 0, column = 1, sticky = tkinter.W + tkinter.N, padx = 10)

        self._rule_label = tkinter.Label(master = self._dialog_window, text = 'Rule: ', font = FONT)
        self._rule_label.grid(row = 7, column = 0, sticky = tkinter.W + tkinter.N)
        self._rule_frame = tkinter.Frame(master = self._dialog_window)
        self._rule_frame.grid(row = 7, column = 1, rowspan = 2, sticky = tkinter.W + tkinter.N, pady = 3)
        self._moredics_button = tkinter.Button(master = self._rule_frame, text = 'More', font = FONT, padx = 22, command = self._moredics_win)
        self._lessdics_button = tkinter.Button(master = self._rule_frame, text = 'Less', font = FONT, padx = 22, command = self._lessdics_win)
        self._moredics_button.grid(row = 0, column = 0, sticky = tkinter.W + tkinter.N, padx = 10)
        self._lessdics_button.grid(row = 0, column = 1, sticky = tkinter.W + tkinter.N, padx = 13)

        self._ok_cancel_button_frame = tkinter.Frame(master = self._dialog_window)
        self._ok_cancel_button_frame.grid(row = 9, column = 1, sticky = tkinter.E, pady = 3)
        self._ok_button = tkinter.Button(master = self._ok_cancel_button_frame, text = 'Start game', font = FONT, padx = 20, command = self._on_start_game)
        self._ok_button.grid(row = 0, column = 0, sticky = tkinter.E, padx = 10)
        self._cancel_button = tkinter.Button(master = self._ok_cancel_button_frame, text = 'Cancel', font = FONT, padx = 20, command = self._on_cancel)
        self._cancel_button.grid(row = 0, column = 1, sticky = tkinter.E)

        self._dialog_window.columnconfigure(1, weight = 5)

        #default
        self._start_game_clicked = False
        self._rule_clicked = False
        self._firstmove_clicked = False
        self._topleft_clicked = False
        self._rows = ROWS
        self._cols = COLS
        self._rule = 1
        self._firstmove = 'b'
        self._topleft = 'b'
        
    def _show(self):
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

    def _lack_of_information_button_clicked(self):
        self._pop_up_window.destroy()
    
    def _on_start_game(self):
        self._start_game_clicked = True
        try: 
            self._cols = int(self._col_entry.get())
            self._rows = int(self._row_entry.get())
            if (self._rule_clicked and self._firstmove_clicked and self._topleft_clicked and
                gamecode._is_an_even_number_between_4_and_16(self._cols) and gamecode._is_an_even_number_between_4_and_16(self._rows)):
                self._dialog_window.destroy()
            
            else:
                LACK_OF_INFORMATION = ''
                if not gamecode._is_an_even_number_between_4_and_16(self._cols):
                    LACK_OF_INFORMATION += 'Column number is not an even number.\n'
                if not gamecode._is_an_even_number_between_4_and_16(self._rows):
                    LACK_OF_INFORMATION += 'Row number is not an even number.\n'
                if not self._rule_clicked:
                    LACK_OF_INFORMATION += 'Did not select Rule.\n'
                if not self._firstmove_clicked:
                    LACK_OF_INFORMATION += 'Did not select First move color.\n'
                if not self._topleft_clicked:
                    LACK_OF_INFORMATION += 'Did not selectTop left move.'
                pop_up_window = PopUpError(LACK_OF_INFORMATION)
                pop_up_window._show_error()
        except:
            LACK_OF_INFORMATION = ''
            try:
                self._cols = int(self._col_entry.get())
            except:
                LACK_OF_INFORMATION += 'Column number should be an integer'
            else:
                try:
                    self._rows = int(self._row_entry.get())
                except:
                    LACK_OF_INFORMATION += 'Row number should be an integer'
                finally:
                    if not self._rule_clicked:
                        LACK_OF_INFORMATION += 'Did not select Rule.\n'
                    if not self._firstmove_clicked:
                        LACK_OF_INFORMATION += 'Did not select First move color.\n'
                    if not self._topleft_clicked:
                        LACK_OF_INFORMATION += 'Did not selectTop left move.'
                    pop_up_window = PopUpError(LACK_OF_INFORMATION)
                    pop_up_window._show_error()
                    
    def _on_cancel(self):
        self._dialog_window.destroy()
        
    def _moredics_win(self):
        self._rule_clicked = True
        self._rule = 1

    def _lessdics_win(self):
        self._rule_clicked = True
        self._rule = 2

    def _firstmove_is_black(self):
        self._firstmove_clicked = True
        self._firstmove = BLACK

    def _firstmove_is_white(self):
        self._firstmove_clicked = True
        self._firstmove = WHITE

    def _topleft_is_black(self):
        self._topleft_clicked = True
        self._topleft = BLACK

    def _topleft_is_white(self):
        self._topleft_clicked = True
        self._topleft = WHITE
        
class Board:
    
    def _on_start(self):
        self._board.delete(tkinter.ALL)
        self._on_start_clicked = True
        dialogue_window = GetInfoWindow()
        dialogue_window._show()
        self._cols = dialogue_window._cols
        self._rows = dialogue_window._rows
        self._topleft = dialogue_window._topleft
        self._turn = dialogue_window._firstmove
        if self._turn == BLACK:
            self._gamereport.set('It is Black\'s turn!')
        else:
            self._gamereport.set('It is White\'s turn!')
        self._rule = dialogue_window._rule
        self._play_game()

    def _choose_the_winner(self):
        if gamecode._game_is_over(self._turn, self._cols, self._rows, self._logicboard):
            winner = gamecode.choose_the_winner(self._cols, self._rows, self._logicboard, self._rule)
            self._gamereport.set(winner + ' wins!')
        
    def _on_mouse_click(self, event):
        if self._have_drew_board:
            board_width = self._board.winfo_width()
            board_height = self._board.winfo_height()
            gapx = (board_width ) / (self._rows + 2)
            gapy = (board_height) / (self._cols + 2)
            self._gap = min(gapx, gapy)
            self._logic_row = int(event.x//self._gap) - 1
            self._logic_column = int(event.y //self._gap) - 1
            self._logicpos = (int(event.x//self._gap) - 1, int(event.y //self._gap) - 1)
            
            if not gamecode._game_is_over(self._turn, self._cols, self._rows, self._logicboard):
                if gamecode._is_in_the_board(self._cols, self._rows, self._logic_column, self._logic_row):

                    if gamecode._is_a_valid_move(self._turn, self._cols, self._rows, self._logicboard, self._logicpos):
                        self._logicboard = gamecode.place_a_disc(self._turn, self._cols, self._rows, self._logicboard, self._logicpos)
                        self._turn = gamecode._opposite_turn(self._turn)
                        self._board = engine.Othello._apply_discs_from_logic_board(self, self._board, self._logicboard)
                        if gamecode._no_valid_move_on_the_board(self._turn, self._cols, self._rows, self._logicboard):
                            if self._turn == BLACK:
                                self._turn = gamecode._opposite_turn(self._turn)
                                self._gamereport.set('No valid move for Black.\nChange to White\'s turn.')
                            elif self._turn == WHITE:
                                self._turn = gamecode._opposite_turn(self._turn)
                                self._gamereport.set('No valid move for White.\nChange to Black\'s turn.')
                        else:
                            if self._turn == BLACK:
                                self._gamereport.set('It is Black\'s turn!')
                            else:
                                self._gamereport.set('It is White\'s turn!')
                        counter = gamecode.counter(self._logicboard, self._cols, self._rows)
                        self._blackreport.set('Black: '+ str(counter['b']))
                        self._whitereport.set('White: ' + str(counter['w']))
                        self._choose_the_winner()
                else:
                    pass
            else:
                pass

        else:
            pass

    def _redraw_board_and_discs(self, event):
        if self._have_drew_board:
            self._board.delete(tkinter.ALL)
            GameApp = engine.Othello(self._board, self._cols, self._rows, self._turn, self._topleft)
            self._board = engine.Othello._draw_board(GameApp)
            
            self._board = engine.Othello._apply_discs_from_logic_board(self, self._board, self._logicboard)
        else:
            pass
        
        
    def _play_game(self):

        GameApp = engine.Othello(self._board, self._cols, self._rows, self._turn, self._topleft)
        self._board = engine.Othello._draw_board(GameApp)

        self._logicboard = engine.Othello._logic_board(GameApp)
        self._have_drew_board = True
        self._blackreport.set('Black: 2')
        self._whitereport.set('White: 2')
        
    def _on_quit(self):
        self._root_window.destroy()
        
    def __init__(self):
        self._root_window = tkinter.Tk()
        
        self._board = tkinter.Canvas(master = self._root_window, width=WIDTH - 4, height=HEIGHT - 4, background=BROWNCOLOR)
        self._board.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._gamereport = tkinter.StringVar()
        self._gamereport.set('Are u ready?')
        self._blackreport = tkinter.StringVar()
        self._blackreport.set('Black:')
        self._whitereport = tkinter.StringVar()
        self._whitereport.set('White:')
        
        self._Data = tkinter.Frame(master = self._root_window)
        self._Data.grid(row = 0, column = 1, padx = 5, pady = 5, sticky =  tkinter.W + tkinter.E)
        self._black_label = tkinter.Label(master = self._Data, font = FONT, textvariable = self._blackreport)
        self._white_label = tkinter.Label(master = self._Data, font = FONT, textvariable = self._whitereport)
        self._turn_label = tkinter.Label(master = self._Data, font = FONT, textvariable = self._gamereport)
        self._black_label.grid(row = 0, column = 1, sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E )
        self._white_label.grid(row = 1, column = 1, sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E )
        self._turn_label.grid(row = 2, column = 1, sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        
        self._Buttons = tkinter.Frame(master = self._root_window)
        self._Buttons.grid(row = 1, column = 0, columnspan = 2, sticky = tkinter.E)
        self._Start_Button = tkinter.Button(self._Buttons, padx = 10, text = 'Start', font = FONT, command = self._on_start)
        self._Start_Button.grid(row = 1 , column = 0, padx = 5, sticky = tkinter.E)
        self._Quit_Button = tkinter.Button(self._Buttons, text = 'Quit', font = FONT, padx = 10, command = self._on_quit)
        self._Quit_Button.grid(row = 1 , column = 1, padx = 5, sticky = tkinter.E)
        
        self._on_start_clicked = False
        self._have_drew_board = False

        self._board.bind('<Configure>', self._redraw_board_and_discs)
        self._board.bind('<Button-1>', self._on_mouse_click)
        
        self._root_window.columnconfigure(0, weight = 10)
        self._root_window.columnconfigure(1, weight = 1)
        self._root_window.rowconfigure(0, weight = 10)
        self._root_window.rowconfigure(1, weight = 1)


    def _start(self):
        self._root_window.mainloop()

if __name__ == '__main__':
    b = Board()
    b._start()