import tkinter

def set_title(row, column):
    global curr_player
    if board[row][column]["text"] == "":
        board[row][column]["text"] = curr_player
        if check_winner():
            label.config(text=curr_player + " wins!")
            disable_buttons()
        elif is_draw():
            label.config(text="It's a draw!")
        else:
            toggle_player()

def check_winner():
    # Check rows
    for row in range(3):
        if board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] != "":
            return True
    # Check columns
    for column in range(3):
        if board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] != "":
            return True
    # Check diagonals
    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] != "":
        return True
    if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] != "":
        return True
    return False

def is_draw():
    for row in range(3):
        for column in range(3):
            if board[row][column]["text"] == "":
                return False
    return True

def toggle_player():
    global curr_player
    curr_player = playerO if curr_player == playerX else playerX
    label.config(text=curr_player + "'s turn")

def disable_buttons():
    for row in range(3):
        for column in range(3):
            board[row][column].config(state="disabled")

# Game setup
playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

color_gray = "#343434"

# Window setup
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player + "'s turn", font=("consolas", 20),
                      background=color_gray, foreground="white")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("consolas", 50, "bold"),
                                            background=color_gray, foreground="blue", width=4, height=1,
                                            command=lambda row=row, column=column: set_title(row, column))
        board[row][column].grid(row=row + 1, column=column)

label.grid(row=0, column=0, columnspan=3)
frame.pack()
window.mainloop()
