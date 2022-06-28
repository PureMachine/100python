from question_model import Question
from data import TriviaData
from quiz_brain import QuizBrain
from ui import QuizInterface

td = TriviaData(amount=10)
td.get_questions()
question_bank = []
print(td.questions)
for question in td.questions:
    new_question = Question(question["question"], question["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
