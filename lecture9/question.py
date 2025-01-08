class Question:

    def __init__(self, question: str, answer_alternatives: list, correct_index: int):
        self.question = question
        self.answer_alternatives = answer_alternatives
        self.correct_index = correct_index

    def is_correct(self, given_answer: str) -> bool: 
        if self.answer_alternatives[self.correct_index] == given_answer:
            return True
        else: 
            return False
        
    def is_correct_index(self, given_answer_index: int) -> bool:
        return self.correct_index == given_answer_index
        
if __name__ == "__main__":
    q = Question("What is 2+2?", ["4", "5", "Ask ChatGPT", "0"], 0)
    print(type(q))
    print(q.is_correct("5"))
    print(q.is_correct("4"))
    print(q.is_correct_index(0))
    print(q.is_correct_index(1))