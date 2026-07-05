import tkinter as tk
from tkinter import messagebox
import random

class ArcadeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Game Arcade")
        
        # Main container variable for the active screen
        self.current_frame = None
        self.show_master_menu()

    def show_master_menu(self):
        # Clear any existing game screen frames safely
        if self.current_frame:
            self.current_frame.destroy()
            
        # Create Master Hub box container
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack(padx=40, pady=40)
        
        title = tk.Label(self.current_frame, text="🕹️ MAIN ARCADE 🕹️", font=("Arial", 22, "bold"))
        title.pack(pady=20)
        
        btn_ttt = tk.Button(self.current_frame, text="Play Tic-Tac-Toe", font=("Arial", 14), width=25, height=2,
                             command=self.load_tic_tac_toe)
        btn_ttt.pack(pady=10)
        
        btn_mem = tk.Button(self.current_frame, text="Play Memory Match", font=("Arial", 14), width=25, height=2,
                             command=self.load_memory_game)
        btn_mem.pack(pady=10)

    def load_tic_tac_toe(self):
        self.current_frame.destroy()
        # Launch Tic-Tac-Toe inside this window instance, passing menu function as callback
        TicTacToeEngine(self.root, self.show_master_menu)

    def load_memory_game(self):
        self.current_frame.destroy()
        # Launch Memory Game inside this window instance, passing menu function as callback
        MemoryEngine(self.root, self.show_master_menu)


class TicTacToeEngine:
    def __init__(self, root, exit_callback):
        self.root = root
        self.exit_to_arcade = exit_callback
        
        # Setup Data Lockers
        self.game_mode = None  
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.is_board_locked = False  
        
        self.win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical Columns
            (0, 4, 8), (2, 4, 6)              # Diagonal Lines
        ]
        
        # Sub-frames to avoid layout manager overlap crashes
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20)
        self.menu_frame = None
        self.game_frame = None
        
        self.show_menu()

    def show_menu(self):
        self.menu_frame = tk.Frame(self.main_frame)
        self.menu_frame.pack()
        
        title = tk.Label(self.menu_frame, text="Tic-Tac-Toe Mode", font=("Arial", 16, "bold"))
        title.pack(pady=10)
        
        tk.Button(self.menu_frame, text="2 Players", font=("Arial", 12), width=18,
                  command=lambda: self.start_game("2player")).pack(pady=5)
        tk.Button(self.menu_frame, text="Vs Computer", font=("Arial", 12), width=18,
                  command=lambda: self.start_game("computer")).pack(pady=5)
        tk.Button(self.menu_frame, text="⬅ Back to Arcade", font=("Arial", 12), bg="gray", width=18,
                  command=self.quit_engine).pack(pady=15)

    def start_game(self, mode):
        self.game_mode = mode
        self.menu_frame.destroy()
        
        self.game_frame = tk.Frame(self.main_frame)
        self.game_frame.pack()
        
        for i in range(9):
            row = i // 3
            col = i % 3
            btn = tk.Button(self.game_frame, text="", font=("Arial", 20, "bold"), width=5, height=2,
                            command=lambda idx=i: self.on_click(idx))
            btn.grid(row=row, column=col, padx=4, pady=4)
            self.buttons.append(btn)

    def on_click(self, index):
        if self.is_board_locked or self.board[index] != "":
            return
            
        self.make_move(index, self.current_player)
        
        if self.check_game_over():
            return
            
        if self.game_mode == "2player":
            self.current_player = "O" if self.current_player == "X" else "X"
        elif self.game_mode == "computer":
            self.current_player = "O"
            self.is_board_locked = True  
            self.root.after(400, self.computer_turn)  

    def make_move(self, index, player):
        self.board[index] = player
        self.buttons[index].config(text=player, state="disabled", disabledforeground="black")

    def computer_turn(self):
        choice = self.get_smart_move()
        if choice is not None:
            self.make_move(choice, "O")
        self.is_board_locked = False  
        if not self.check_game_over():
            self.current_player = "X"

    def get_smart_move(self):
        # PRIORITY 1: Check for active AI Win paths
        for combo in self.win_conditions:
            p1, p2, p3 = combo
            line = [self.board[p1], self.board[p2], self.board[p3]]
            if line.count("O") == 2 and line.count("") == 1:
                for idx in combo:
                    if self.board[idx] == "": return idx
                    
        # PRIORITY 2: Check for Human Block requirements
        for combo in self.win_conditions:
            p1, p2, p3 = combo
            line = [self.board[p1], self.board[p2], self.board[p3]]
            if line.count("X") == 2 and line.count("") == 1:
                for idx in combo:
                    if self.board[idx] == "": return idx
                    
        # PRIORITY 3: Lock down the Center Square
        center_idx = 4
        if self.board[center_idx] == "": return center_idx
        
        # PRIORITY 4: Claim remaining open Corners
        corners = (0, 2, 6, 8)
        open_corners = [c for c in corners if self.board[c] == ""]
        if open_corners: return random.choice(open_corners)
        
        # PRIORITY 5: Grab fallback leftover slots
        leftovers = [i for i in range(9) if self.board[i] == ""]
        if leftovers: return random.choice(leftovers)
        return None

    def check_game_over(self):
        for combo in self.win_conditions:
            p1, p2, p3 = combo
            if self.board[p1] == self.board[p2] == self.board[p3] != "":
                messagebox.showinfo("Victory", f"Player {self.board[p1]} wins!")
                self.reset_or_exit()
                return True
        if "" not in self.board:
            messagebox.showinfo("Tie", "It's a draw!")
            self.reset_or_exit()
            return True
        return False

    def reset_or_exit(self):
        self.game_frame.destroy()
        self.buttons = []
        self.board = [""] * 9
        self.current_player = "X"
        self.is_board_locked = False
        self.show_menu()

    def quit_engine(self):
        self.main_frame.destroy()
        self.exit_to_arcade()


class MemoryEngine:
    def __init__(self, root, exit_callback):
        self.root = root
        self.exit_to_arcade = exit_callback
        
        # FIXED FOREVER: Using tuple conversion syntax to prevent markdown number stripping bugs!
        self.cards = list((1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8))
        random.shuffle(self.cards)
        
        self.buttons = []
        self.first_clicked_idx = None
        self.lock_board = False
        
        # Base Frames
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20)
        
        self.create_board()

    def create_board(self):
        # Grid Container Box
        self.grid_frame = tk.Frame(self.main_frame)
        self.grid_frame.pack()
        
        for i in range(16):
            row = i // 4
            col = i % 4
            btn = tk.Button(self.grid_frame, text="?", font=("Arial", 18, "bold"), width=5, height=2,
                            command=lambda idx=i: self.on_click(idx))
            btn.grid(row=row, column=col, padx=4, pady=4)
            self.buttons.append(btn)
            
        # Bottom Utility Menu Box
        self.util_frame = tk.Frame(self.main_frame)
        self.util_frame.pack(pady=15)
        tk.Button(self.util_frame, text="⬅ Exit to Arcade Hub", font=("Arial", 11), bg="gray",
                  command=self.quit_engine).pack()

    def on_click(self, index):
        if self.lock_board or self.buttons[index]["text"] != "?":
            return
        
        card_val = self.cards[index]
        self.buttons[index].config(text=str(card_val))
        
        if self.first_clicked_idx is None:
            self.first_clicked_idx = index
        else:
            self.check_match(index)

    def check_match(self, second_idx):
        first_idx = self.first_clicked_idx
        if self.cards[first_idx] == self.cards[second_idx]:
            self.buttons[first_idx].config(state="disabled", disabledforeground="green")
            self.buttons[second_idx].config(state="disabled", disabledforeground="green")
            self.first_clicked_idx = None
            self.check_win()
        else:
            self.lock_board = True
            self.root.after(1000, lambda: self.hide_cards(first_idx, second_idx))

    def hide_cards(self, idx1, idx2):
        self.buttons[idx1].config(text="?")
        self.buttons[idx2].config(text="?")
        self.first_clicked_idx = None
        self.lock_board = False

    def check_win(self):
        if all(btn["text"] != "?" for btn in self.buttons):
            messagebox.showinfo("Victory!", "You matched all cards!")
            self.quit_engine()

    def quit_engine(self):
        self.main_frame.destroy()
        self.exit_to_arcade()


if __name__ == "__main__":
    window = tk.Tk()
    app = ArcadeApp(window)
    window.mainloop()