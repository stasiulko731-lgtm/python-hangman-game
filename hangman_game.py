import random
import tkinter as tk
from tkinter import messagebox, simpledialog

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("700x650")
        self.root.configure(bg="#2c3e50")
        
        self.words = ["python", "coding", "hangman", "developer", "programming", "algorithm", "database", "function"]
        self.word = random.choice(self.words)
        self.guessed = []
        self.attempts = 10
        self.game_over = False
        
        # Extended Hangman stages (11 stages total)
        self.hangman_stages = [
            """
               ------
               |    |
               |
               |
               |
               |
               |
               ---------
            """,
            """
               ------
               |    |
               |    O
               |
               |
               |
               |
               ---------
            """,
            """
               ------
               |    |
               |    O
               |    |
               |
               |
               |
               ---------
            """,
            """
               ------
               |    |
               |    O
               |   \\|
               |
               |
               |
               ---------
            """,
            """
               ------
               |    |
               |    O
               |   \\|/
               |
               |
               |
               ---------
            """,
            """
               ------
               |    |
               |    O
               |   \\|/
               |    |
               |
               |
               ---------
            """,
            """
               ------
               |    |
               |    O
               |   \\|/
               |    |
               |   /
               |
               ---------
            """,
            """
               ------
               |    |
               |    O
               |   \\|/
               |    |
               |   / \\
               |
               ---------
            """,
            """
               ------
               |    |
               |    O
               |   \\|/
               |    |
               |   / \\
               |  /
               ---------
            """,
            """
               ------
               |    |
               |    O
               |   \\|/
               |    |
               |   / \\
               |  / \\
               ---------
            """,
            """
               ------
               |    |
               |    O
               |   \\|/
               |    |
               |   / \\
               |  / \\ 
               --------- YOU LOSE!
            """
        ]
        
        self.setup_ui()
        self.update_display()
    
    def setup_ui(self):
        # Title
        title = tk.Label(self.root, text="🎮 HANGMAN GAME 🎮", 
                         font=("Arial", 24, "bold"), 
                         bg="#2c3e50", fg="#ecf0f1")
        title.pack(pady=15)
        
        # Hangman display
        self.hangman_label = tk.Label(self.root, text="", 
                                      font=("Courier", 9), 
                                      bg="#2c3e50", fg="#e74c3c")
        self.hangman_label.pack(pady=5)
        
        # Word display
        self.word_label = tk.Label(self.root, text="", 
                                   font=("Arial", 32, "bold"), 
                                   bg="#2c3e50", fg="#3498db")
        self.word_label.pack(pady=15)
        
        # Attempts counter
        self.attempts_label = tk.Label(self.root, text="", 
                                       font=("Arial", 14, "bold"), 
                                       bg="#2c3e50", fg="#f39c12")
        self.attempts_label.pack(pady=5)
        
        # Guessed letters
        self.guessed_label = tk.Label(self.root, text="", 
                                      font=("Arial", 10), 
                                      bg="#2c3e50", fg="#2ecc71", 
                                      wraplength=600)
        self.guessed_label.pack(pady=10)
        
        # Input frame for letter
        input_frame = tk.Frame(self.root, bg="#2c3e50")
        input_frame.pack(pady=15)
        
        tk.Label(input_frame, text="Guess a letter:", 
                 font=("Arial", 12), 
                 bg="#2c3e50", fg="#ecf0f1").pack(side=tk.LEFT, padx=5)
        
        self.input_entry = tk.Entry(input_frame, font=("Arial", 12), width=5)
        self.input_entry.pack(side=tk.LEFT, padx=5)
        self.input_entry.bind("<Return>", lambda event: self.guess_letter())
        
        guess_btn = tk.Button(input_frame, text="Guess Letter", 
                              command=self.guess_letter, 
                              font=("Arial", 10, "bold"),
                              bg="#3498db", fg="white", 
                              padx=15, relief=tk.RAISED)
        guess_btn.pack(side=tk.LEFT, padx=5)
        
        # Button frame
        button_frame = tk.Frame(self.root, bg="#2c3e50")
        button_frame.pack(pady=10)
        
        guess_word_btn = tk.Button(button_frame, text="Guess Word (-2)", 
                                   command=self.guess_word, 
                                   font=("Arial", 10, "bold"),
                                   bg="#9b59b6", fg="white", 
                                   padx=15, relief=tk.RAISED)
        guess_word_btn.pack(side=tk.LEFT, padx=5)
        
        new_game_btn = tk.Button(button_frame, text="New Game", 
                                 command=self.new_game, 
                                 font=("Arial", 10, "bold"),
                                 bg="#2ecc71", fg="white", 
                                 padx=15, relief=tk.RAISED)
        new_game_btn.pack(side=tk.LEFT, padx=5)
        
        quit_btn = tk.Button(button_frame, text="Quit", 
                             command=self.root.quit, 
                             font=("Arial", 10, "bold"),
                             bg="#e74c3c", fg="white", 
                             padx=15, relief=tk.RAISED)
        quit_btn.pack(side=tk.LEFT, padx=5)
    
    def guess_letter(self):
        if self.game_over:
            messagebox.showinfo("Game Over", 
                               "You Guessed. Click Enter to play again!")
            return
        
        guess = self.input_entry.get().lower()
        self.input_entry.delete(0, tk.END)
        
        if not guess or len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter!")
            return
        
        if guess in self.guessed:
            messagebox.showinfo("Already Guessed", f"You already guessed '{guess}'!")
            return
        
        self.guessed.append(guess)
        
        if guess not in self.word:
            self.attempts -= 1
        
        self.check_game_status()
        self.update_display()
    
    def guess_word(self):
        if self.game_over:
            messagebox.showinfo("Game Over", 
                               "You Guessed. Click Enter to play again!")
            return
        
        # Prompt user to enter the word
        word_guess = simpledialog.askstring("Guess the Word", "Enter the word (costs 2 attempts if wrong):")
        
        if word_guess is None:  # User clicked Cancel
            return
        
        word_guess = word_guess.lower().strip()
        
        if not word_guess:
            messagebox.showwarning("Invalid Input", "Please enter a word!")
            return
        
        if word_guess == self.word:
            self.game_over = True
            messagebox.showinfo("You Win! 🎉", 
                               f"Correct! The word was: {self.word}\n\nYou Guessed. Click Enter to play again!")
        else:
            self.attempts -= 2
            messagebox.showinfo("Wrong!", 
                               f"Wrong! You lost 2 attempts.\nAttempts remaining: {self.attempts}")
            self.check_game_status()
            self.update_display()
    
    def check_game_status(self):
        display = [c if c in self.guessed else "_" for c in self.word]
        
        if "_" not in display:
            self.game_over = True
            messagebox.showinfo("You Win! 🎉", 
                               f"Congratulations! The word was: {self.word}\n\nYou Guessed. Click Enter to play again!")
        elif self.attempts <= 0:
            self.game_over = True
            messagebox.showinfo("Game Over! 💀", 
                               f"Game Over! The word was: {self.word}\n\nYou Guessed. Click Enter to play again!")
    
    def update_display(self):
        # Update hangman drawing (capped at 10, so max index is 10)
        hangman_index = max(0, 10 - self.attempts)
        if hangman_index > 10:
            hangman_index = 10
        self.hangman_label.config(text=self.hangman_stages[hangman_index])
        
        # Update word display
        display = [c if c in self.guessed else "_" for c in self.word]
        self.word_label.config(text=" ".join(display))
        
        # Update attempts
        self.attempts_label.config(text=f"Attempts remaining: {self.attempts}")
        
        # Update guessed letters
        guessed_text = f"Guessed letters: {', '.join(sorted(self.guessed)) if self.guessed else 'None yet'}"
        self.guessed_label.config(text=guessed_text)
    
    def new_game(self):
        self.word = random.choice(self.words)
        self.guessed = []
        self.attempts = 10
        self.game_over = False
        self.input_entry.focus()
        self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
