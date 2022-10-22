from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []
for question in question_data:
  q_text = question["text"]
  q_answer = question["answer"]
  new_question = Question(q_text, q_answer)
  question_bank.append(new_question)

quiz = Quiz(question_bank)

while(quiz.is_continue()):
  quiz.next_question()
