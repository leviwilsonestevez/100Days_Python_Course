from question_model import Question


class QuizBrain:
    def __init__(self, question_list: list[Question]):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self) -> bool:
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number} : {current_question.text} Type the answer (True/False):")
        self.check_answer(answer=answer, current_question=current_question)

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def check_answer(self, answer: str, current_question: Question):
        if answer.lower() == current_question.answer.lower():
            self.score += 1
            print("You got it right!!")
            print(f"The correct answer was : {current_question.answer} ")
            print(f"The current score answer is : {self.score}/{self.question_number} \n")
        else:
            print("You got it wrong!!")
            print(f"The correct answer is : {current_question.answer} ")
            print(f"The current score answer is : {self.score}/{self.question_number} \n")
