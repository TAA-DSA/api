from tkinter import *


THEME_COLOR = "#375362"


class QuizUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label(text="score: 0", bg=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1, sticky="e")

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.true_image = PhotoImage(file="./images/true.png")
        self.btn = Button(image=self.true_image, command="")
        self.btn.grid(row=3, column=0)

        self.false_image = PhotoImage(file="./images/false.png")
        self.btn = Button(image=self.false_image, command="")
        self.btn.grid(row=3, column=1)

        self.score_text = self.canvas.create_text(
            150, 125, text="Hello", fill="black", font=("Ariel", 20, "italic")
        )

        self.window.mainloop()
