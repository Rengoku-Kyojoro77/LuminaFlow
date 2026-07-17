import random
import tkinter as tk

guessnum = 0


def getWord():
    global guessnum
    guessedWord = EntryBox.get().lower().strip()

    if len(guessedWord) != 5:
        return

    if guessedWord not in wordlist:
        return

    letter_counts = {}
    for letter in chosenWord:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

    colors = ["grey"] * 5

    for i in range(5):
        if guessedWord[i] == chosenWord[i]:
            colors[i] = "green"
            letter_counts[guessedWord[i]] -= 1

    for i in range(5):
        if colors[i] == "green":
            continue

        if guessedWord[i] in chosenWord and letter_counts[guessedWord[i]] > 0:
            colors[i] = "gold"
            letter_counts[guessedWord[i]] -= 1

    for i in range(5):
        label = tk.Label(
            text=guessedWord[i].upper(),
            pady=5,
            font=("Arial", 14, "bold"),
            borderwidth=1,
            relief="solid",
            width=4,
            bg=colors[i],
            fg="white",
        )
        label.grid(row=guessnum, column=i, sticky=tk.NSEW, padx=2, pady=2)

    update_keyboard(guessedWord, colors)

    EntryBox.delete(0, tk.END)

    if guessedWord == chosenWord or guessnum >= 5:
        GuessButton.config(state="disabled")
        for key in keyboard_buttons.values():
            key.config(state="disabled")

        result_label = tk.Label(
            text=f"The word was: {chosenWord.upper()}",
            font=("Arial", 12, "bold"),
            fg="black",
        )
        result_label.grid(row=102, column=0, columnspan=5, pady=10)

    guessnum += 1


def press_key(char):
    if len(EntryBox.get()) < 5:
        EntryBox.insert(tk.END, char)


def update_keyboard(guessedWord, colors):
    for i in range(5):
        char = guessedWord[i].upper()
        color = colors[i]
        current_btn = keyboard_buttons.get(char)

        if not current_btn:
            continue

        current_color = current_btn.cget("bg")
        if current_color == "green":
            continue
        if current_color == "gold" and color == "grey":
            continue

        current_btn.config(bg=color, fg="white" if color != "lightgray" else "black")


try:
    with open("Fiveletterwords.txt") as file:
        words = file.read()
    wordlist = [w.strip().lower() for w in words.split("\n") if w.strip()]
except FileNotFoundError:
    wordlist = ["first", "apple", "react", "house", "robot", "words", "train"]

chosenWord = random.choice(wordlist)

window = tk.Tk()
window.title("Wordle")
window.geometry("350x570")

EntryBox = tk.Entry(font=("Arial", 14), justify="center")
EntryBox.grid(row=99, column=0, columnspan=5, pady=10)

GuessButton = tk.Button(
    text="Guess", font=("Arial", 12), command=getWord, bg="lightgray"
)
GuessButton.grid(row=100, column=0, columnspan=5, pady=5)

keyboard_frame = tk.Frame(window)
keyboard_frame.grid(row=101, column=0, columnspan=5, pady=10)

rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
keyboard_buttons = {}

for row_idx, row_letters in enumerate(rows):
    row_frame = tk.Frame(keyboard_frame)
    row_frame.pack()
    for char in row_letters:
        btn = tk.Button(
            row_frame,
            text=char,
            font=("Arial", 10, "bold"),
            width=2,
            height=1,
            bg="lightgray",
            command=lambda c=char: press_key(c),
        )
        btn.pack(side=tk.LEFT, padx=1, pady=1)
        keyboard_buttons[char] = btn

window.mainloop()