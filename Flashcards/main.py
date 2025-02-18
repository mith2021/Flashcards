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

        self.add_button = tk.Button(root, text="Add Flashcard", command= lambda: [self.add_flashcard()], bg="#FF9800", fg="#FFFFFF", font=("Helvetica", 12), relief="flat", padx=10, pady=5)
        self.add_button.pack(pady=10)

        # Flashcards storage
        self.flashcards = []
        self.flashcard_questions = []
        self.current_index = -1

        self.list_title = tk.Label(root, text="List Of Flashcards: select to edit", bg="#FF9800", fg="#FFFFFF", font=("Helvetica", 12), relief="flat", padx=10, pady=5)
        self.list_title.pack()

        self.selected_option = tk.StringVar(root)
        self.selected_option.set("No Flashcards")

        self.menu = tk.OptionMenu(root, self.selected_option, "No Flashcards")
        self.menu.pack(pady=20)

    #update flashcards list 
    def update_flashcards_list(self):
        menu = self.menu['menu']
        menu.delete(0,'end')

        if self.flashcards:
            for flashcard in self.flashcards:
                flashcard_index = self.flashcards.index(flashcard)
                menu.add_command(label=flashcard["Question"], command=lambda q=flashcard["Question"]: self.select_flashcard(q, flashcard_index))
            self.selected_option.set(self.flashcards[-1]["Question"])  # Set last added as default
        else:
            self.selected_option.set("No Flashcards")
            menu.add_command(label="No Flashcards", command=lambda: self.selected_option.set("No Flashcards"))

    def add_flashcard(self):
        question = self.question_entry.get()
        answer = self.answer_entry.get()
        if question and answer:
            self.flashcards.append({"Question": question, "Answer": answer})
            self.flashcard_label.config(text=f"Question: {question}")
            self.next_card()

            self.question_entry.delete(0, tk.END)  # Clears the question entry
            self.answer_entry.delete(0, tk.END)    # Clears the answer entry

            self.update_flashcards_list()
        else:
            messagebox.showwarning("Input Error", "Please enter both question and answer")
            
    #select flashcard
    def select_flashcard(self, q, flashcard_index):
        self.selected_option.set(q)
        
        self.flashcard_label.config(text=f"Edit Question: {q}")

        self.question_entry.delete(0, tk.END) 
        self.answer_entry.delete(0, tk.END)  

        self.question_entry.insert(0, self.flashcards[flashcard_index]["Question"]) 
        self.answer_entry.insert(0, self.flashcards[flashcard_index]["Answer"]) 
        
        def update_flashcard(flashcard_index):
            updated_question = self.question_entry.get()
            updated_ans = self.answer_entry.get()

            if updated_question and updated_ans:
                self.flashcards[flashcard_index] = {"Question": updated_question, "Answer": updated_ans}
                self.selected_option.set(updated_question)
                
                self.update_flashcards_list()
            else:
                messagebox.showwarning("Input Error", "Please enter both question and answer")

        update_button = tk.Button(self.root, text="Update Flashcard", command=update_flashcard(flashcard_index), bg="#FF9800", fg="#FFFFFF", font=("Helvetica", 12), relief="flat", padx=10, pady=5)
        update_button.pack(pady=10)
        
    def show_answer(self):
        if self.current_index != -1:
            ans = self.flashcards[self.current_index]["Answer"]
            self.flashcard_label.config(text=f"Answer: {ans}")

    def next_card(self):
        self.current_index += 1 
        if len(self.flashcards) <= self.current_index:
            self.current_index = 0
        if self.flashcards:
            question = self.flashcards[self.current_index]["Question"]
            self.flashcard_label.config(text=f"{question}")
        else: 
            self.flashcard_label.config(text="No Flashcards available.")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardsApp(root)
    root.mainloop()

