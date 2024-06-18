import tkinter as tk

class Program(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1024x768")
        self.title("Finite-state machine simulator | NBL-1-FSM")
        self.canvas = tk.Canvas(self, bg="#a9a9a9")
        self.current_action = None

        add_state_button = tk.Button(self, text="Add state", command=lambda: self.set_current_action("add"))
        delete_state_button = tk.Button(self, text="Delete state", command=lambda: self.set_current_action("delete"))
        move_state_button = tk.Button(self, text="Move state", command=lambda: self.set_current_action("move"))
        make_transition_button = tk.Button(self, text="Make transition", command=lambda: self.set_current_action("transition"))
        self.current_action_label = tk.Label(self, text="Current action: None")

    
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

        self.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        if self.current_action == "add":
            self.add_state(event)
        elif self.current_action == "delete":
            self.delete_state(event)
        elif self.current_action == "move":
            self.move_state(event)
        elif self.current_action == "transition":
            self.make_transition(event)

    def set_current_action(self, action: str):
        self.current_action = action
        self.current_action_label["text"] = f"Current action: {action}"

    def add_state(self, event):
        self.canvas.create_oval(event.x-25, event.y-25, event.x+25, event.y+25, fill="#abab00", outline="#6f6f6f", width=3)
    
    def delete_state(self, event):
        pass

    def move_state(self, event):
        pass

    def make_transition(self, event):
        pass


def main():
    window = Program()
    window.mainloop()


if __name__ == "__main__":
    main()
