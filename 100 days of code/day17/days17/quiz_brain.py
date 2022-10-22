class Quiz:
    def __init__(self,  question_list):
        self.number_question = 0
        self.score = 0
        self.question_list = question_list

    

    
    def next_question(self):
        cur_question = self.question_list[self.number_question]
        self.number_question += 1
        user_answer = input(f"{self.number_question}: {cur_question.text} . True/False.")
        self.check_answer(user_answer, cur_question.answer)

    def is_continue(self):
        if(self.number_question < len(self.question_list)):
            return True
        return False

    def check_answer(self, user_answer, correct_answer):
        if(user_answer == correct_answer):
            self.score +=1
            print("You got it")
        else:
            print("That's wrong.")
        print(f"The correct answer is{correct_answer}")
        print(f"Your score is {self.score} / {len(self.question_list)}")
    

        
