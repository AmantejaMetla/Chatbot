from tkinter import *
from chatbot import chatbot_response  # Ensure this is the correct function for chatbot responses

def on_send():
    user_input = user_entry.get()
    if user_input.strip():  # Prevent sending empty input
        chat_window.config(state=NORMAL)
        chat_window.insert(END, f"You: {user_input}\n", "user")
        response = chatbot_response(user_input)
        chat_window.insert(END, f"Chatbot: {response}\n\n", "bot")
        chat_window.config(state=DISABLED)
        chat_window.see(END)  # Automatically scroll to the bottom
        user_entry.delete(0, END)

# Create GUI
root = Tk()
root.title("Chatbot Assistant")
root.geometry("600x700")
root.resizable(False, False)

# Colors and Fonts
BG_COLOR = "#1E1E2E"
TEXT_COLOR = "#EAEAEA"
BOT_COLOR = "#4BA3C3"
USER_COLOR = "#78E08F"
FONT = ("Arial", 12)
BUTTON_COLOR = "#00ADB5"
ENTRY_BG = "#393E46"
ENTRY_TEXT_COLOR = "#FFFFFF"

# Chat window (Scrollable)
chat_frame = Frame(root, bg=BG_COLOR)
chat_frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

chat_window = Text(
    chat_frame,
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    font=FONT,
    wrap=WORD,
    state=DISABLED,
    padx=10,
    pady=10,
)
chat_window.tag_configure("user", foreground=USER_COLOR)  # User's text in green
chat_window.tag_configure("bot", foreground=BOT_COLOR)  # Bot's text in blue
chat_window.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(chat_frame, command=chat_window.yview, bg=BG_COLOR)
scrollbar.pack(side=RIGHT, fill=Y)
chat_window.config(yscrollcommand=scrollbar.set)

# Input area frame
input_frame = Frame(root, bg=BG_COLOR)
input_frame.pack(fill=X, padx=10, pady=10)

user_entry = Entry(
    input_frame,
    bg=ENTRY_BG,
    fg=ENTRY_TEXT_COLOR,
    font=FONT,
    insertbackground=TEXT_COLOR,
    bd=2,
    relief=FLAT,
    width=40,
)
user_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

send_button = Button(
    input_frame,
    text="Send",
    bg=BUTTON_COLOR,
    fg=TEXT_COLOR,
    font=("Arial", 12, "bold"),
    command=on_send,
    relief=FLAT,
    width=10,
)
send_button.grid(row=0, column=1, padx=10, pady=10)

input_frame.columnconfigure(0, weight=1)

# Run the application
root.mainloop()
