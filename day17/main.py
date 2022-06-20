from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


question_bank = []


def run():

    for trivia in question_data:
        question_bank.append(Question(trivia["text"], trivia["answer"]))

    qb = QuizBrain(question_bank)
    while qb.questions_remaining():
        qb.next_question()
        if qb.evaluate_answer():
            qb.update_score(0)
        else:
            qb.update_score()
    qb.final_score()


if __name__ == "__main__":
    run()

