import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.tk = tk.Tk()
        self.tk.title = "Quizzler"
        self.tk.configure(bg=THEME_COLOR, pady=20, padx=20)

        self.lb_score = tk.Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 16, "bold"))
        self.lb_score.grid(column=1, row=0)

        self.can = tk.Canvas()
        self.can.configure(bg="white", width=300, height=250)
        self.can_text = self.can.create_text(150, 125, text="Question Goes Here", font=("Arial", 20, "italic"), width=280)
        self.can.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        btn_true_image = tk.PhotoImage(file="images/true.png")
        btn_false_image = tk.PhotoImage(file="images/false.png")
        self.btn_true = tk.Button(command=self.press_true, image=btn_true_image)
        self.btn_false = tk.Button(command=self.press_false, image=btn_false_image)
        self.btn_true.grid(column=0, row=2)
        self.btn_false.grid(column=1, row=2)

        self.get_next_question()

        self.tk.mainloop()

    def press_true(self):
        if self.quiz.check_answer("True"):
            self.tk.configure(bg="green")
            self.lb_score.configure(bg="green")
        else:
            self.tk.configure(bg="red")
            self.lb_score.configure(bg="red")
        self.get_next_question()

    def press_false(self):
        if self.quiz.check_answer("False"):
            self.tk.configure(bg="green")
            self.lb_score.configure(bg="green")
        else:
            self.tk.configure(bg="red")
            self.lb_score.configure(bg="red")
        self.get_next_question()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.lb_score.configure(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.can.itemconfig(self.can_text, text=q_text)
        else:
            self.end_game()

    def end_game(self):
        self.can.itemconfig(self.can_text,
                            text=f"Game Over. Your final score is: {self.quiz.score}/{self.quiz.question_number}")
        self.btn_true.grid_forget()
        self.btn_false.grid_forget()


