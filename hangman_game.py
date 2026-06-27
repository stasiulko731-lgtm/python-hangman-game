import random
import tkinter as tk
from tkinter import messagebox, simpledialog

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("800x700")
        self.root.configure(bg="#2c3e50")
        
        # Language settings
        self.languages = {
            "English (UK)": {
                "title": "HANGMAN GAME",
                "guess_letter": "Guess a letter:",
                "guess_letter_btn": "Guess Letter",
                "guess_word_btn": "Guess Word (-2)",
                "new_game_btn": "New Game",
                "quit_btn": "Quit",
                "attempts": "Attempts remaining:",
                "guessed_letters": "Guessed letters:",
                "none_yet": "None yet",
                "invalid_input_single": "Please enter a single letter!",
                "already_guessed": "You already guessed",
                "wrong_guess": "Wrong!",
                "lost_attempts": "You lost 2 attempts.\nAttempts remaining:",
                "you_win": "You Win!",
                "correct": "Correct! The word was:",
                "you_guessed": "You Guessed. Click Enter to play again!",
                "game_over": "Game Over!",
                "word_was": "The word was:",
                "language": "Language:",
                "category": "Category:",
                "categories": {
                    "Animals": ["elephant", "penguin", "butterfly", "crocodile", "kangaroo"],
                    "Programming": ["python", "coding", "hangman", "developer", "programming", "algorithm", "database", "function"],
                    "Countries": ["poland", "england", "france", "germany", "spain", "italy"],
                    "Food": ["pizza", "sandwich", "chocolate", "strawberry", "hamburger"]
                }
            },
            "English (US)": {
                "title": "HANGMAN GAME",
                "guess_letter": "Guess a letter:",
                "guess_letter_btn": "Guess Letter",
                "guess_word_btn": "Guess Word (-2)",
                "new_game_btn": "New Game",
                "quit_btn": "Quit",
                "attempts": "Attempts remaining:",
                "guessed_letters": "Guessed letters:",
                "none_yet": "None yet",
                "invalid_input_single": "Please enter a single letter!",
                "already_guessed": "You already guessed",
                "wrong_guess": "Wrong!",
                "lost_attempts": "You lost 2 attempts.\nAttempts remaining:",
                "you_win": "You Win!",
                "correct": "Correct! The word was:",
                "you_guessed": "You Guessed. Click Enter to play again!",
                "game_over": "Game Over!",
                "word_was": "The word was:",
                "language": "Language:",
                "category": "Category:",
                "categories": {
                    "Animals": ["elephant", "penguin", "butterfly", "crocodile", "kangaroo"],
                    "Programming": ["python", "coding", "hangman", "developer", "programming", "algorithm", "database", "function"],
                    "Countries": ["usa", "canada", "mexico", "brazil", "argentina"],
                    "Food": ["pizza", "hamburger", "hotdog", "pancake", "donut"]
                }
            },
            "Polski": {
                "title": "GRA HANGMAN",
                "guess_letter": "Odgadnij literę:",
                "guess_letter_btn": "Odgadnij Literę",
                "guess_word_btn": "Odgadnij Słowo (-2)",
                "new_game_btn": "Nowa Gra",
                "quit_btn": "Wyjście",
                "attempts": "Pozostałe próby:",
                "guessed_letters": "Odgadnięte litery:",
                "none_yet": "Żadna",
                "invalid_input_single": "Proszę wpisać pojedynczą literę!",
                "already_guessed": "Już odgadłeś",
                "wrong_guess": "Źle!",
                "lost_attempts": "Straciłeś 2 próby.\nPozostałe próby:",
                "you_win": "Wygrałeś!",
                "correct": "Poprawnie! Słowem było:",
                "you_guessed": "Odgadłeś! Naciśnij Enter aby zagrać ponownie!",
                "game_over": "Koniec Gry!",
                "word_was": "Słowem było:",
                "language": "Język:",
                "category": "Kategoria:",
                "categories": {
                    "Zwierzęta": ["słoń", "pingwin", "motyl", "krokodyl", "kangur"],
                    "Programowanie": ["python", "kodowanie", "hangman", "developer", "algorytm", "baza", "funkcja"],
                    "Kraje": ["polska", "anglia", "francja", "niemcy", "włochy"],
                    "Jedzenie": ["pizza", "kanapka", "czekolada", "truskawka", "hamburger"]
                }
            }
        }
        
        self.current_language = "English (UK)"
        self.current_category = "Programming"
        self.word = ""
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
        self.new_game()
    
    def get_text(self, key):
        """Get translated text for current language"""
        return self.languages[self.current_language].get(key, key)
    
    def setup_ui(self):
        # Title
        title = tk.Label(self.root, text="🎮 HANGMAN GAME 🎮", 
                         font=("Arial", 24, "bold"), 
                         bg="#2c3e50", fg="#ecf0f1")
        title.pack(pady=10)
        
        # Language and Category frame
        settings_frame = tk.Frame(self.root, bg="#2c3e50")
        settings_frame.pack(pady=10)
        
        tk.Label(settings_frame, text="Language:", 
                 font=("Arial", 10), 
                 bg="#2c3e50", fg="#ecf0f1").pack(side=tk.LEFT, padx=5)
        
        self.language_var = tk.StringVar(value=self.current_language)
        language_menu = tk.OptionMenu(settings_frame, self.language_var, 
                                      *self.languages.keys(),
                                      command=self.change_language)
        language_menu.config(font=("Arial", 10), bg="#3498db", fg="white")
        language_menu.pack(side=tk.LEFT, padx=5)
        
        tk.Label(settings_frame, text="Category:", 
                 font=("Arial", 10), 
                 bg="#2c3e50", fg="#ecf0f1").pack(side=tk.LEFT, padx=15)
        
        self.category_var = tk.StringVar(value=self.current_category)
        self.category_menu = tk.OptionMenu(settings_frame, self.category_var, 
                                           *self.languages[self.current_language]["categories"].keys(),
                                           command=self.change_category)
        self.category_menu.config(font=("Arial", 10), bg="#9b59b6", fg="white")
        self.category_menu.pack(side=tk.LEFT, padx=5)
        
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
        
        self.guess_letter_label = tk.Label(input_frame, text="Guess a letter:", 
                 font=("Arial", 12), 
                 bg="#2c3e50", fg="#ecf0f1")
        self.guess_letter_label.pack(side=tk.LEFT, padx=5)
        
        self.input_entry = tk.Entry(input_frame, font=("Arial", 12), width=5)
        self.input_entry.pack(side=tk.LEFT, padx=5)
        self.input_entry.bind("<Return>", lambda event: self.guess_letter())
        
        self.guess_btn = tk.Button(input_frame, text="Guess Letter", 
                              command=self.guess_letter, 
                              font=("Arial", 10, "bold"),
                              bg="#3498db", fg="white", 
                              padx=15, relief=tk.RAISED)
        self.guess_btn.pack(side=tk.LEFT, padx=5)
        
        # Button frame
        button_frame = tk.Frame(self.root, bg="#2c3e50")
        button_frame.pack(pady=10)
        
        self.guess_word_btn = tk.Button(button_frame, text="Guess Word (-2)", 
                                   command=self.guess_word, 
                                   font=("Arial", 10, "bold"),
                                   bg="#9b59b6", fg="white", 
                                   padx=15, relief=tk.RAISED)
        self.guess_word_btn.pack(side=tk.LEFT, padx=5)
        
        self.new_game_btn = tk.Button(button_frame, text="New Game", 
                                 command=self.new_game, 
                                 font=("Arial", 10, "bold"),
                                 bg="#2ecc71", fg="white", 
                                 padx=15, relief=tk.RAISED)
        self.new_game_btn.pack(side=tk.LEFT, padx=5)
        
        self.quit_btn = tk.Button(button_frame, text="Quit", 
                             command=self.root.quit, 
                             font=("Arial", 10, "bold"),
                             bg="#e74c3c", fg="white", 
                             padx=15, relief=tk.RAISED)
        self.quit_btn.pack(side=tk.LEFT, padx=5)
    
    def change_language(self, language):
        """Change the game language"""
        self.current_language = language
        self.update_ui_text()
        # Update category menu with new categories
        categories = list(self.languages[self.current_language]["categories"].keys())
        self.current_category = categories[0]
        self.category_var.set(self.current_category)
        
        self.category_menu['menu'].delete(0, 'end')
        for cat in categories:
            self.category_menu['menu'].add_command(label=cat, 
                                                   command=tk.StringVar.set(self.category_var, cat))
        
        self.new_game()
    
    def change_category(self, category):
        """Change the game category"""
        self.current_category = category
        self.new_game()
    
    def update_ui_text(self):
        """Update all UI text based on current language"""
        self.guess_letter_label.config(text=self.get_text("guess_letter"))
        self.guess_btn.config(text=self.get_text("guess_letter_btn"))
        self.guess_word_btn.config(text=self.get_text("guess_word_btn"))
        self.new_game_btn.config(text=self.get_text("new_game_btn"))
        self.quit_btn.config(text=self.get_text("quit_btn"))
    
    def guess_letter(self):
        if self.game_over:
            messagebox.showinfo(self.get_text("game_over"), 
                               self.get_text("you_guessed"))
            return
        
        guess = self.input_entry.get().lower()
        self.input_entry.delete(0, tk.END)
        
        if not guess or len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", self.get_text("invalid_input_single"))
            return
        
        if guess in self.guessed:
            messagebox.showinfo("Already Guessed", f"{self.get_text('already_guessed')} '{guess}'!")
            return
        
        self.guessed.append(guess)
        
        if guess not in self.word:
            self.attempts -= 1
        
        self.check_game_status()
        self.update_display()
    
    def guess_word(self):
        if self.game_over:
            messagebox.showinfo(self.get_text("game_over"), 
                               self.get_text("you_guessed"))
            return
        
        # Prompt user to enter the word
        word_guess = simpledialog.askstring("Guess the Word", 
                                            f"{self.get_text('guess_word_btn')}\n({self.get_text('lost_attempts').split(chr(10))[0]}):")
        
        if word_guess is None:  # User clicked Cancel
            return
        
        word_guess = word_guess.lower().strip()
        
        if not word_guess:
            messagebox.showwarning("Invalid Input", "Please enter a word!")
            return
        
        if word_guess == self.word:
            self.game_over = True
            messagebox.showinfo(f"{self.get_text('you_win')} 🎉", 
                               f"{self.get_text('correct')} {self.word}\n\n{self.get_text('you_guessed')}")
        else:
            self.attempts -= 2
            messagebox.showinfo(self.get_text("wrong_guess"), 
                               f"{self.get_text('lost_attempts')} {self.attempts}")
            self.check_game_status()
            self.update_display()
    
    def check_game_status(self):
        display = [c if c in self.guessed else "_" for c in self.word]
        
        if "_" not in display:
            self.game_over = True
            messagebox.showinfo(f"{self.get_text('you_win')} 🎉", 
                               f"{self.get_text('correct')} {self.word}\n\n{self.get_text('you_guessed')}")
        elif self.attempts <= 0:
            self.game_over = True
            messagebox.showinfo(f"{self.get_text('game_over')} 💀", 
                               f"{self.get_text('game_over')}\n{self.get_text('word_was')} {self.word}\n\n{self.get_text('you_guessed')}")
    
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
        self.attempts_label.config(text=f"{self.get_text('attempts')} {self.attempts}")
        
        # Update guessed letters
        guessed_text = f"{self.get_text('guessed_letters')} {', '.join(sorted(self.guessed)) if self.guessed else self.get_text('none_yet')}"
        self.guessed_label.config(text=guessed_text)
    
    def new_game(self):
        categories = self.languages[self.current_language]["categories"]
        self.word = random.choice(categories[self.current_category])
        self.guessed = []
        self.attempts = 10
        self.game_over = False
        self.input_entry.delete(0, tk.END)
        self.input_entry.focus()
        self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
