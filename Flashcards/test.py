import tkinter as tk
from tkinter import messagebox

class FlashcardsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcards App")
        self.root.geometry("400x600")
        self.root.configure(bg="#2B2B2B")  # Dark background

        # Title label
        self.title_label = tk.Label(root, text="Flashcards App", font=("Helvetica", 20, "bold"), bg="#2B2B2B", fg="#FFFFFF")
        self.title_label.pack(pady=15)

        # Flashcard display
        self.flashcard_frame = tk.Frame(root, bg="#3C3F41", width=300, height=200, relief="solid", bd=1)
        self.flashcard_frame.pack(pady=20)

        self.flashcard_label = tk.Label(self.flashcard_frame, text="Click 'Show' to reveal", font=("Helvetica", 14), wraplength=280, justify="center", bg="#3C3F41", fg="#FFFFFF")
        self.flashcard_label.pack(expand=True)

        # Buttons frame
        self.buttons_frame = tk.Frame(root, bg="#2B2B2B")
        self.buttons_frame.pack(pady=10)

        self.show_button = tk.Button(self.buttons_frame, text="Show Answer", command=self.show_answer, bg="#4CAF50", fg="#FFFFFF", font=("Helvetica", 12), relief="flat", padx=10, pady=5)
        self.show_button.grid(row=0, column=0, padx=5)

        self.next_button = tk.Button(self.buttons_frame, text="Next", command=self.next_card, bg="#2196F3", fg="#FFFFFF", font=("Helvetica", 12), relief="flat", padx=10, pady=5)
        self.next_button.grid(row=0, column=1, padx=5)

        # Input fields
        self.input_frame = tk.Frame(root, bg="#2B2B2B")
        self.input_frame.pack(pady=20)

        tk.Label(self.input_frame, text="Question:", bg="#2B2B2B", fg="#FFFFFF", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", padx=5)
        self.question_entry = tk.Entry(self.input_frame, width=30, font=("Helvetica", 12), relief="solid", bd=1, bg="#3C3F41", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.question_entry.grid(row=0, column=1, pady=5)

        tk.Label(self.input_frame, text="Answer:", bg="#2B2B2B", fg="#FFFFFF", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", padx=5)
        self.answer_entry = tk.Entry(self.input_frame, width=30, font=("Helvetica", 12), relief="solid", bd=1, bg="#3C3F41", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.answer_entry.grid(row=1, column=1, pady=5)

        self.add_button = tk.Button(root, text="Add Flashcard", command=self.add_flashcard, bg="#FF9800", fg="#FFFFFF", font=("Helvetica", 12), relief="flat", padx=10, pady=5)
        self.add_button.pack(pady=10)

        # Flashcards storage
        self.flashcards = []
        self.current_index = -1

        # Flashcard selection list
        self.list_title = tk.Label(root, text="List Of Flashcards: select to edit", bg="#2B2B2B", fg="#FFFFFF", font=("Helvetica", 12))
        self.list_title.pack()

        self.selected_option = tk.StringVar(root)
        self.selected_option.set("No Flashcards")

        self.menu = tk.OptionMenu(root, self.selected_option, "No Flashcards", command=self.select_flashcard)
        self.menu.pack(pady=20)

    def update_flashcards_list(self):
        """Updates the dropdown list with new flashcards."""
        menu = self.menu["menu"]
        menu.delete(0, "end")  # Clear the current options

        if self.flashcards:
            for flashcard in self.flashcards:
                menu.add_command(label=flashcard["Question"], command=lambda q=flashcard["Question"]: self.selected_option.set(q))
            self.selected_option.set(self.flashcards[-1]["Question"])  # Set last added as default
        else:
            self.selected_option.set("No Flashcards")
            menu.add_command(label="No Flashcards", command=lambda: self.selected_option.set("No Flashcards"))

    def add_flashcard(self):
        """Adds a flashcard and updates the dropdown list."""
        question = self.question_entry.get()
        answer = self.answer_entry.get()
        if question and answer:
            self.flashcards.append({"Question": question, "Answer": answer})
            self.flashcard_label.config(text=f"Question: {question}")

            self.question_entry.delete(0, tk.END)  # Clear the entry
            self.answer_entry.delete(0, tk.END)

            self.update_flashcards_list()  # Refresh dropdown list
        else:
            messagebox.showwarning("Input Error", "Please enter both question and answer")

    def select_flashcard(self, selected_question):
        """Displays the selected flashcard."""
        for index, flashcard in enumerate(self.flashcards):
            if flashcard["Question"] == selected_question:
                self.current_index = index
                self.flashcard_label.config(text=f"Question: {flashcard['Question']}")
                break

    def show_answer(self):
        """Reveals the answer to the current flashcard."""
        if self.current_index != -1:
            ans = self.flashcards[self.current_index]["Answer"]
            self.flashcard_label.config(text=f"Answer: {ans}")

    def next_card(self):
        """Displays the next flashcard."""
        self.current_index += 1
        if len(self.flashcards) <= self.current_index:
            self.current_index = 0
        if self.flashcards:
            question = self.flashcards[self.current_index]["Question"]
            self.flashcard_label.config(text=f"Question: {question}")
        else:
            self.flashcard_label.config(text="No Flashcards available.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardsApp(root)
    root.mainloop()
