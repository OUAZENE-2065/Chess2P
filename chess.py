import customtkinter as ctk
from json import load
from copy import deepcopy

ctk.set_appearance_mode('dark')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        with open('data.json', 'r') as file:
            self.data = load(file)
        
        self.title('Chess 2P')
        self.geometry(f'{self.data["width"]}x{self.data["height"]}+50+0')
        
        self.board = {}
        self.history = {}
        
        self.begin_app()
        
        
        
        self.mainloop()
    
    def begin_app(self):
        self.hello_frame = ctk.CTkFrame(self, corner_radius=0, border_width=0, fg_color='transparent')
        self.hello_frame.place(x=0, y=0, relwidth=1, relheight=1)
        ctk.CTkButton(self.hello_frame,text='New Game', command=self.new_game).pack(expand=True)
        
    def create_init_board(self):
        self.board = board()
        self.board.write()
        print()
        self.board.move((1, 1), (8, 8), True)
        self.board.write()
        
    def new_game(self):
        self.create_init_board()
        self.begin_game()
        
    def begin_game(self):
        self.game_frame = ctk.CTkFrame(self, corner_radius=0, border_width=0, fg_color='transparent')
        self.game_frame.place(x=0, y=0, relwidth=1, relheight=1)

class board:
    def __init__(self, board = None, killed_pieces = None, history = None) -> None:
        self.void = {
                    'name' : None,
                    'color' : None, # Black or White
                    'option' : None
                }
        if board == None:
            self.board = {}
            for i in range(1, 9):
                self.board[i] = {}
                for j in range(1, 9):
                    self.board[i][j] = deepcopy(self.void)
            for i in range(1, 9):
                self[1,i]['color'] = 'White'
                self[2,i]['color'] = 'White'
                self[7,i]['color'] = 'Black'
                self[8,i]['color'] = 'Black'
                self[2,i]['name'] = 'Pawn'
                self[7,i]['name'] = 'Pawn'
                if (i == 1) or (i == 8):
                    self[1,i]['name'] = 'Rock'
                    self[8,i]['name'] = 'Rock'
                elif (i == 2) or (i == 7):
                    self[1,i]['name'] = 'Knight'
                    self[8,i]['name'] = 'Knight'
                elif (i == 3) or (i == 6):
                    self[1,i]['name'] = 'Bishop'
                    self[8,i]['name'] = 'Bishop'
                elif i == 5: 
                    self[1,i]['name'] = 'Queen'
                    self[8,i]['name'] = 'Queen'
                else :
                    self[1,i]['name'] = 'King'
                    self[8,i]['name'] = 'King'
            self.killed_pieces = {
                'Black' : [],
                'White' : []
            }
            self.history = []
        else :
            self.board = board
            self.killed_pieces = killed_pieces
            self.history = history
        
    
    def __getitem__(self, args : tuple):
        return self.board[args[0]][args[1]]
    
    def move(self, pos1, pos2, kill= False):
        if kill:
            if self[pos2]['name'] != None:
                self.killed_pieces[self[pos2]['color']].append(self[pos2])
        self._set_(pos2, self[pos1])
        self._set_(pos1, deepcopy(self.void))
        print()
        print(self.killed_pieces)
        print()
        
    def write(self):
        for i in range(8, 0, -1):
            for j in range(1, 9):
                print(f"{self[i, j]['name'] + '_' + self[i, j]['color'][0] if self[i, j]['name'] != None else 'None':10}", end='   ')
            print()

    def _set_(self, pos, data):
        self.board[pos[0]][pos[1]] = data
    
    

if __name__ == '__main__':
    App()