import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        
        # Create buttons for the board
        self.buttons = [[tk.Button(root, text='', font=('Arial', 24), height=2, width=5, 
                                   command=lambda r=i, c=j: self.make_move(r, c)) 
                         for j in range(3)] for i in range(3)]
        
        # Place buttons in grid
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j)
    
    def make_move(self, row, col):
        if self.board[row][col] == '' and not self.check_winner():
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
                return
            
            if self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
                return

            self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != '':
                return True
        
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != '':
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '':
            return True
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '':
            return True
        
        return False

    def is_draw(self):
        return all(self.board[i][j] != '' for i in range(3) for j in range(3))
    
    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ''
                self.buttons[i][j].config(text='')
        self.current_player = "X"

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
