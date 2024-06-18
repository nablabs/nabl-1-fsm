import tkinter as tk

class Program(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Finite-state machine simulator | NBL-1-FSM")
        self.canvas = tk.Canvas(self, bg="#a9a9a9")

        # I want a variable that will know what is the current action of the user. This can be add, delete, move or make transition.
        self.current_action = None

        add_state_button = tk.Button(self, text="Add state", command=lambda: self.set_current_action("add"))
        delete_state_button = tk.Button(self, text="Delete state", command=lambda: self.set_current_action("delete"))
        move_state_button = tk.Button(self, text="Move state", command=lambda: self.set_current_action("move"))
        make_transition_button = tk.Button(self, text="Make transition", command=lambda: self.set_current_action("transition"))
        self.current_action_label = tk.Label(self, text="Current action: None")

    
        # I want to grid all the buttons at the top and the canvas below them. I want them to stick to the borders of the window and move on resize.
        add_state_button.grid(row=0, column=0, sticky="we")
        delete_state_button.grid(row=0, column=1, sticky="we")
        move_state_button.grid(row=0, column=2, sticky="we")
        make_transition_button.grid(row=0, column=3, sticky="we")
        self.canvas.grid(row=1, column=0, columnspan=4, sticky="nswe")
        self.current_action_label.grid(row=2, column=0, columnspan=4, sticky="we")
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

    def set_current_action(self, action: str):
        self.current_action = action
        self.current_action_label["text"] = f"Current action: {action}"

def main():
    window = Program()
    window.mainloop()


if __name__ == "__main__":
    main()
