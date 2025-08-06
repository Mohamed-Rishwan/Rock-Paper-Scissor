import tkinter as tk
import random

# Choices
choices = ["rock", "paper", "scissor"]

# Global variables
player_score = 0
computer_score = 0
tie_score = 0
valid_rounds_played = 0
max_valid_rounds = 0

# Color and Font
BG_COLOR = "#121212"
BTN_COLOR = "#1F1F1F"
TEXT_COLOR = "#FFFFFF"
ACCENT_COLOR = "#00FFAA"
FONT_TITLE = ("Segoe UI", 20, "bold")
FONT_NORMAL = ("Segoe UI", 12)
FONT_BUTTON = ("Segoe UI", 11, "bold")

# Emoji Map
emoji_map = {
    "rock": "🪨",
    "paper": "📄",
    "scissor": "✂"
}

# Create main window
root = tk.Tk()
root.title("🎮 Rock Paper Scissors")
root.geometry("420x500")
root.config(bg=BG_COLOR)
root.resizable(False, False)

# Title
title = tk.Label(root, text="🎮 Rock Paper Scissors", font=FONT_TITLE, fg=ACCENT_COLOR, bg=BG_COLOR)
title.pack(pady=20)

# Frame for the game
game_frame = tk.Frame(root, bg=BG_COLOR)
# game_frame.pack()   # ❌ Don't pack here

# Round tracker
round_tracker = tk.Label(game_frame, text="", font=FONT_NORMAL, fg="lightgray", bg=BG_COLOR)
round_tracker.pack(pady=5)

# Result text
result_text = tk.Label(game_frame, text="Choose your move!", font=("Segoe UI", 13), fg="#FFD700", bg=BG_COLOR)
result_text.pack(pady=10)

# Emoji display (reduced font size)
emoji_display = tk.Label(game_frame, text="", font=("Segoe UI", 18), bg=BG_COLOR, fg=TEXT_COLOR)
emoji_display.pack(pady=5)

# Scoreboard
scoreboard = tk.Label(game_frame, text="", font=FONT_NORMAL, fg=TEXT_COLOR, bg=BG_COLOR)
scoreboard.pack(pady=10)

# Buttons
button_frame = tk.Frame(game_frame, bg=BG_COLOR)
button_frame.pack(pady=10)

def update_ui():
    round_tracker.config(text=f"Valid Rounds: {valid_rounds_played}/{max_valid_rounds}")
    scoreboard.config(text=f"👤 You: {player_score}    🤖 Computer: {computer_score}    🤝 Ties: {tie_score}")

def show_final_result():
    if player_score > computer_score:
        result_text.config(text="🎉 You won the game!", fg="#00FF00")
    else:
        result_text.config(text="💻 Computer won the game!", fg="#FF5555")
    restart_btn.pack(pady=15)

def play(player_choice):
    global player_score, computer_score, tie_score, valid_rounds_played

    if player_score == max_valid_rounds or computer_score == max_valid_rounds:
        return

    computer_choice = random.choice(choices)
    emoji_display.config(
        text=f"You: {emoji_map[player_choice]}  VS  Computer: {emoji_map[computer_choice]}"
    )

    if player_choice == computer_choice:
        result_text.config(text="It's a tie!", fg="#CCCC00")
        tie_score += 1
    elif (player_choice == "rock" and computer_choice == "scissor") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissor" and computer_choice == "paper"):
        result_text.config(text="You win this round!", fg="#00FF00")
        player_score += 1
        valid_rounds_played += 1
    else:
        result_text.config(text="Computer wins this round!", fg="#FF5555")
        computer_score += 1
        valid_rounds_played += 1

    update_ui()

    if player_score == max_valid_rounds or computer_score == max_valid_rounds:
        show_final_result()

def restart_game():
    global player_score, computer_score, tie_score, valid_rounds_played
    player_score = computer_score = tie_score = valid_rounds_played = 0
    result_text.config(text="Choose your move!", fg="#FFD700")
    emoji_display.config(text="")
    scoreboard.config(text="")
    round_tracker.config(text="")
    restart_btn.pack_forget()
    game_frame.pack_forget()
    mode_frame.pack(pady=40)

def start_game(rounds):
    global max_valid_rounds
    max_valid_rounds = rounds
    update_ui()
    mode_frame.pack_forget()
    game_frame.pack()

# Game Buttons
rock_btn = tk.Button(button_frame, text="🪨 Rock", font=FONT_BUTTON, bg=BTN_COLOR, fg=TEXT_COLOR,
                     command=lambda: play("rock"), width=10)
paper_btn = tk.Button(button_frame, text="📄 Paper", font=FONT_BUTTON, bg=BTN_COLOR, fg=TEXT_COLOR,
                      command=lambda: play("paper"), width=10)
scissor_btn = tk.Button(button_frame, text="✂ Scissor", font=FONT_BUTTON, bg=BTN_COLOR, fg=TEXT_COLOR,
                        command=lambda: play("scissor"), width=10)

rock_btn.grid(row=0, column=0, padx=5, pady=5)
paper_btn.grid(row=0, column=1, padx=5, pady=5)
scissor_btn.grid(row=0, column=2, padx=5, pady=5)

# Restart button
restart_btn = tk.Button(root, text="🔁 Restart Game", font=FONT_BUTTON, bg="#333", fg="#FFF", command=restart_game)

# Mode Selection
mode_frame = tk.Frame(root, bg=BG_COLOR)
mode_frame.pack(pady=40)

mode_title = tk.Label(mode_frame, text="Choose match type", font=("Segoe UI", 14), fg="skyblue", bg=BG_COLOR)
mode_title.pack(pady=10)

btn_best3 = tk.Button(mode_frame, text="🥉 Best of 3", font=FONT_BUTTON, bg=BTN_COLOR, fg=TEXT_COLOR,
                      width=20, command=lambda: start_game(2))
btn_best5 = tk.Button(mode_frame, text="🥈 Best of 5", font=FONT_BUTTON, bg=BTN_COLOR, fg=TEXT_COLOR,
                      width=20, command=lambda: start_game(3))
btn_best7 = tk.Button(mode_frame, text="🥇 Best of 7", font=FONT_BUTTON, bg=BTN_COLOR, fg=TEXT_COLOR,
                      width=20, command=lambda: start_game(4))
btn_exit = tk.Button(mode_frame, text="❌ Exit", font=FONT_BUTTON, bg="#800000", fg="#FFFFFF",
                     width=20, command=root.destroy)  # ✅ Fixed exit command

btn_best3.pack(pady=5)
btn_best5.pack(pady=5)
btn_best7.pack(pady=5)
btn_exit.pack(pady=5)

# Start GUI loop
root.mainloop()
