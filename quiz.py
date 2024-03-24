class Questions:
    def __init__(self, question_text, options, correct_option):
        self.question_text = question_text
        self.options = options
        self.correct_option = correct_option

def ask_question(question_object):
    print(question_object.question_text)
    for i, option in enumerate(question_object.options, start=1):
        print(f"{i}. {option}")

    user_answer = input("Enter the number of your answer: ")
    return int(user_answer)

# Example usage
question1 = Questions("What is the capital of Armenia?", ["Yerevan", "Tbilisi", "Baku", "Ankara"], 1)
print(question1.__dict__)
# question2 = Questions("What is the capital of Great Britain?", ["Washington", "New York", "London", "Paris"], 3)
# question3 = Questions("What is the capital of Russia?", ["Minsk", "Kyiv", "Moscow", "Ankara"], 3)
# question4 = Questions("What is the capital of America?", ["Lose Angelos", "Washington", "Marsel", "Otawa"], 2)

user_response1 = ask_question(question1)
# user_response2 = ask_question(question2)
# user_response3 = ask_question(question3)
# user_response4 = ask_question(question4)

correct_answer = question1.correct_option

if user_response1 == correct_answer:
    print("Correct!")
else:
    print(f"Wrong! The correct answer is {correct_answer}: {question1.options[correct_answer - 1]}")
