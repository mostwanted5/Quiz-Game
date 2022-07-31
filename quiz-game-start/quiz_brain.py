class QuestionBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list=question_list
    def still_has_question(self):
        return self.question_number < len(self.question_list)
    point=0
    def pull_up(self):
        next_question=self.question_list[self.question_number]
        self.question_number+=1
        answer=input(f"Q.{self.question_number}: {next_question.question} (True or False?): ")
        self.check_answer(next_question.answer, answer)
        print("\n")
    def check_answer(self, question_answer, user_answer):
        if question_answer.lower() == user_answer.lower():
            print("You got it, it is a right answer! ")
            self.score+=1
        else:
            print("Your answer is wrong!")
            print(f"The correct answer was: {question_answer}")
        print(f"Your score is {self.score}/{self.question_number}")