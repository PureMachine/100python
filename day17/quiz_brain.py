class QuizBrain:

    def __init__(self, question_list):
        self.question = 0
        self.question_list = question_list
        self.current_question = 0
        self.answer = ""
        self.score = 0

    def next_question(self):
        self.current_question = self.question_list[self.question]
        self.question += 1
        self.answer = input(f"Question.{self.question}: {self.current_question.text}.\n"
                            f"Answer True or False\n")

    def questions_remaining(self):
        return self.question >= len(self.question_list)

    def evaluate_answer(self):
        if self.answer == self.current_question.answer:
            return True
        else:
            return False

    def update_score(self, result=1):
        if result == 0:
            self.score += 1
        print(f"Score: {self.score}/{self.question}")

    def final_score(self):
        print(f"Final score: {self.score}/{len(self.question_list)}")
