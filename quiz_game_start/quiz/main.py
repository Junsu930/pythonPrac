from data import question_data;
from question_model import Question
from question_brain import QuizBrain
question_bank = [];
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer )
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
def continueQuiz():
    if quiz.next_question() == question_bank[quiz.question_number].answer :
        if quiz.question_number == quiz.final_number-1:
            print("퀴즈 완료! 축하드립니다.")
            return
        else:
            quiz.question_number = quiz.question_number+1
            continueQuiz()
    else:
        print("퀴즈 실패")
        return

continueQuiz()