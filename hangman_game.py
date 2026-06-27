import random
import tkinter as tk
from tkinter import messagebox, simpledialog

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        
        # Get screen dimensions and set window size responsively
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = int(screen_width * 0.95)
        window_height = int(screen_height * 0.95)
        
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.configure(bg="#1a252f")
        
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
                "settings": "Settings",
                "language": "Language:",
                "close_settings": "Close",
                "available_words": "Available words:",
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
                "settings": "Settings",
                "language": "Language:",
                "close_settings": "Close",
                "available_words": "Available words:",
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
                "settings": "Ustawienia",
                "language": "Język:",
                "close_settings": "Zamknij",
                "available_words": "Dostępne słowa:",
                "categories": {
                    "Zwierzęta": ["słoń", "pingwin", "motyl", "krokodyl", "kangur"],
                    "Programowanie": ["python", "kodowanie", "hangman", "developer", "algorytm", "baza", "funkcja"],
                    "Kraje": ["polska", "anglia", "francja", "niemcy", "włochy"],
                    "Jedzenie": ["pizza", "kanapka", "czekolada", "truskawka", "hamburger"]
                }
            }
        }
        
        self.current_language = "English (UK)"
        self.current_category = "Animals"  # Start with a fixed category
        self.word = ""
        self.guessed = []
        self.attempts = 10
        self.game_over = False
        self.settings_window = None
        
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
        # Main container with padding
        main_container = tk.Frame(self.root, bg="#1a252f")
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Top frame with title and settings button
        top_frame = tk.Frame(main_container, bg="#2c3e50", relief=tk.RAISED, bd=2)
        top_frame.pack(pady=(0, 20), fill=tk.X)
        
        # Title
        title = tk.Label(top_frame, text="🎮 HANGMAN GAME 🎮", 
                         font=("Helvetica", 36, "bold"), 
                         bg="#2c3e50", fg="#ecf0f1", pady=15)
        title.pack(side=tk.LEFT, expand=True)
        
        # Settings button (gear emoji)
        settings_btn = tk.Button(top_frame, text="⚙️", 
                                command=self.open_settings,
                                font=("Arial", 28),
                                bg="#34495e", fg="white",
                                relief=tk.FLAT,
                                padx=15, pady=10,
                                activebackground="#2c3e50")
        settings_btn.pack(side=tk.RIGHT, padx=15)
        
        # Info frame with language, category, and words
        info_frame = tk.Frame(main_container, bg="#34495e", relief=tk.SUNKEN, bd=2)
        info_frame.pack(pady=(0, 20), fill=tk.X)
        
        # Top info line
        top_info = tk.Frame(info_frame, bg="#34495e")
        top_info.pack(fill=tk.X, padx=15, pady=10)
        
        self.language_info = tk.Label(top_info, text="", 
                                     font=("Helvetica", 13, "bold"),
                                     bg="#34495e", fg="#ecf0f1")
        self.language_info.pack(side=tk.LEFT, padx=15)
        
        self.category_info = tk.Label(top_info, text="", 
                                     font=("Helvetica", 13, "bold"),
                                     bg="#34495e", fg="#f39c12")
        self.category_info.pack(side=tk.LEFT, padx=15)
        
        # Available words panel
        words_label = tk.Label(info_frame, text="",
                              font=("Helvetica", 11, "bold"),
                              bg="#34495e", fg="#2ecc71")
        words_label.pack(anchor=tk.W, padx=15, pady=(0, 5))
        self.words_label_ref = words_label
        
        self.words_display = tk.Label(info_frame, text="",
                                     font=("Helvetica", 10),
                                     bg="#34495e", fg="#ecf0f1",
                                     wraplength=1200, justify=tk.LEFT)
        self.words_display.pack(anchor=tk.W, padx=15, pady=(0, 10))
        
        # Game content frame (center)
        game_frame = tk.Frame(main_container, bg="#1a252f")
        game_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        # Hangman display
        self.hangman_label = tk.Label(game_frame, text="", 
                                      font=("Courier", 11), 
                                      bg="#1a252f", fg="#e74c3c")
        self.hangman_label.pack(pady=10)
        
        # Word display
        self.word_label = tk.Label(game_frame, text="", 
                                   font=("Helvetica", 48, "bold"), 
                                   bg="#1a252f", fg="#3498db")
        self.word_label.pack(pady=20)
        
        # Attempts counter
        self.attempts_label = tk.Label(game_frame, text="", 
                                       font=("Helvetica", 16, "bold"), 
                                       bg="#1a252f", fg="#f39c12")
        self.attempts_label.pack(pady=10)
        
        # Guessed letters
        self.guessed_label = tk.Label(game_frame, text="", 
                                      font=("Helvetica", 12), 
                                      bg="#1a252f", fg="#2ecc71", 
                                      wraplength=1200)
        self.guessed_label.pack(pady=15)
        
        # Input frame for letter
        input_frame = tk.Frame(main_container, bg="#1a252f")
        input_frame.pack(pady=(0, 20))
        
        self.guess_letter_label = tk.Label(input_frame, text="Guess a letter:", 
                 font=("Helvetica", 13), 
                 bg="#1a252f", fg="#ecf0f1")
        self.guess_letter_label.pack(side=tk.LEFT, padx=10)
        
        self.input_entry = tk.Entry(input_frame, font=("Helvetica", 14), width=5)
        self.input_entry.pack(side=tk.LEFT, padx=10)
        self.input_entry.bind("<Return>", lambda event: self.guess_letter())
        
        self.guess_btn = tk.Button(input_frame, text="Guess Letter", 
                              command=self.guess_letter, 
                              font=("Helvetica", 11, "bold"),
                              bg="#3498db", fg="white", 
                              padx=20, pady=8, relief=tk.RAISED,
                              activebackground="#2980b9")
        self.guess_btn.pack(side=tk.LEFT, padx=10)
        
        # Button frame
        button_frame = tk.Frame(main_container, bg="#1a252f")
        button_frame.pack(pady=(0, 10))
        
        self.guess_word_btn = tk.Button(button_frame, text="Guess Word (-2)", 
                                   command=self.guess_word, 
                                   font=("Helvetica", 11, "bold"),
                                   bg="#9b59b6", fg="white", 
                                   padx=20, pady=8, relief=tk.RAISED,
                                   activebackground="#8e44ad")
        self.guess_word_btn.pack(side=tk.LEFT, padx=10)
        
        self.new_game_btn = tk.Button(button_frame, text="New Game", 
                                 command=self.new_game, 
                                 font=("Helvetica", 11, "bold"),
                                 bg="#2ecc71", fg="white", 
                                 padx=20, pady=8, relief=tk.RAISED,
                                 activebackground="#27ae60")
        self.new_game_btn.pack(side=tk.LEFT, padx=10)
        
        self.quit_btn = tk.Button(button_frame, text="Quit", 
                             command=self.root.quit, 
                             font=("Helvetica", 11, "bold"),
                             bg="#e74c3c", fg="white", 
                             padx=20, pady=8, relief=tk.RAISED,
                             activebackground="#c0392b")
        self.quit_btn.pack(side=tk.LEFT, padx=10)
    
    def open_settings(self):
        """Open settings window"""
        if self.settings_window is not None:
            self.settings_window.lift()
            return
        
        self.settings_window = tk.Toplevel(self.root)
        self.settings_window.title(self.get_text("settings"))
        self.settings_window.geometry("400x200")
        self.settings_window.configure(bg="#2c3e50")
        
        # Settings title
        settings_title = tk.Label(self.settings_window, 
                                 text=self.get_text("settings"),
                                 font=("Helvetica", 18, "bold"),
                                 bg="#2c3e50", fg="#ecf0f1")
        settings_title.pack(pady=20)
        
        # Language frame
        lang_frame = tk.Frame(self.settings_window, bg="#2c3e50")
        lang_frame.pack(pady=15)
        
        tk.Label(lang_frame, text=self.get_text("language"),
                font=("Helvetica", 13),
                bg="#2c3e50", fg="#ecf0f1").pack(side=tk.LEFT, padx=15)
        
        self.language_var = tk.StringVar(value=self.current_language)
        language_menu = tk.OptionMenu(lang_frame, self.language_var,
                                     *self.languages.keys(),
                                     command=self.change_language)
        language_menu.config(font=("Helvetica", 12), bg="#3498db", fg="white", width=18)
        language_menu.pack(side=tk.LEFT, padx=15)
        
        # Close button
        close_btn = tk.Button(self.settings_window, 
                            text=self.get_text("close_settings"),
                            command=self.close_settings,
                            font=("Helvetica", 12, "bold"),
                            bg="#2ecc71", fg="white",
                            padx=25, pady=10)
        close_btn.pack(pady=20)
        
        # Handle window close
        self.settings_window.protocol("WM_DELETE_WINDOW", self.close_settings)
    
    def close_settings(self):
        """Close settings window"""
        if self.settings_window is not None:
            self.settings_window.destroy()
            self.settings_window = None
    
    def change_language(self, language):
        """Change the game language (keeping category)"""
        self.current_language = language
        self.update_ui_text()
        # Keep current category, but pick a new word
        self.pick_new_word()
        self.update_info()
        self.update_display()
    
    def update_ui_text(self):
        """Update all UI text based on current language"""
        self.guess_letter_label.config(text=self.get_text("guess_letter"))
        self.guess_btn.config(text=self.get_text("guess_letter_btn"))
        self.guess_word_btn.config(text=self.get_text("guess_word_btn"))
        self.new_game_btn.config(text=self.get_text("new_game_btn"))
        self.quit_btn.config(text=self.get_text("quit_btn"))
        self.words_label_ref.config(text=self.get_text("available_words"))
    
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
    
    def update_info(self):
        """Update language, category, and available words info display"""
        self.language_info.config(text=f"Language: {self.current_language}")
        self.category_info.config(text=f"Category: {self.current_category}")
        
        # Get available words for current category
        categories_dict = self.languages[self.current_language]["categories"]
        available_words = categories_dict.get(self.current_category, [])
        words_text = ", ".join(available_words)
        self.words_display.config(text=words_text)
    
    def pick_new_word(self):
        """Pick a new word from the current category"""
        categories_dict = self.languages[self.current_language]["categories"]
        
        # If category doesn't exist in this language, pick a random one
        if self.current_category not in categories_dict:
            self.current_category = random.choice(list(categories_dict.keys()))
        
        random_category_words = categories_dict[self.current_category]
        self.word = random.choice(random_category_words)
    
    def new_game(self):
        """Start a new game with randomly selected category"""
        categories_dict = self.languages[self.current_language]["categories"]
        category_names = list(categories_dict.keys())
        self.current_category = random.choice(category_names)
        
        self.pick_new_word()
        
        self.guessed = []
        self.attempts = 10
        self.game_over = False
        self.input_entry.delete(0, tk.END)
        self.input_entry.focus()
        
        self.update_info()
        self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
