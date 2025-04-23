from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

"""Fix the bugs and complete the remaining programs"""


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        if self.quiz.still_has_questions:

            self.label = Label(text="score: 0", bg=THEME_COLOR, fg="white")
            self.label.grid(row=0, column=1, sticky="e")

            self.canvas = Canvas(width=300, height=250, bg="white")
            self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

            self.score_text = self.canvas.create_text(
                150,
                125,
                width=280,
                text="Hello",
                fill="black",
                font=("Ariel", 20, "italic"),
            )

            true_image = PhotoImage(file="./images/true.png")
            self.btn_true = Button(image=true_image, command=self.answer_true)

            self.btn_true.grid(row=3, column=0)

            false_image = PhotoImage(file="./images/false.png")
            self.btn_false = Button(image=false_image, command=self.answer_false)
            self.btn_false.grid(row=3, column=1)

            self.get_next_question()
        else:
            self.canvas.itemconfig(
                self.score_text, text="quiz completed, thank you for playing"
            )

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.score_text, text=q_text)

    def answer_true(self):
        self.feedback(self.quiz.check_answer(user_answer="true"))
        self.label.config(text=f"score: {self.quiz.score}")

    def answer_false(self):
        is_right = "false"
        self.quiz.check_answer(user_answer=is_right)
        self.feedback()

    def feedback(self, is_true):
        self.is_true = is_true
        if is_true:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
