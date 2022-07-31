from data import question_data
from question_model import Question
from quiz_brain import QuestionBrain
import random
from quiz_brain import QuestionBrain

question_bank = []
for item in question_data:
    q1 = item['question']
    a1 = item['correct_answer']
    question_1 = Question(q1, a1)
    question_bank.append(question_1)
quiz = QuestionBrain(question_bank)
point=0
while quiz.still_has_question():
    quiz.pull_up()
print("Congratulation, You successfully completed the Quiz! ")
print(f"Your final score is {quiz.score}")
