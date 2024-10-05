
class Question:
    def __init__(self, text, choices, correct_answer):
        self.text = text
        self.choices = choices
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        return answer.lower() == self.correct_answer.lower()

def load_questions(filename):
    questions = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 6):
                text = lines[i].strip()
                choices = [lines[i+1].strip(), lines[i+2].strip(), lines[i+3].strip(), lines[i+4].strip()]
                correct_answer = lines[i+5].strip()
                question = Question(text, choices, correct_answer)
                questions.append(question)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    return questions

def ask_question(question):
    print(question.text)
    for i, choice in enumerate(question.choices, start=1):
        print(f"{i}. {choice}")
    answer = input("Your answer (a/b/c/d): ")
    if question.is_correct(answer):
        print("Correct!\n")
        return True
    else:
        print(f"Incorrect! The correct answer was: {question.correct_answer}\n")
        return False

def play_quiz(questions):
    score = 0
    for question in questions:
        if ask_question(question):
            score += 1
    print(f"\nYour final score is {score}/{len(questions)}.")

def main():
    print("Welcome to the Quiz Game!")
    filename = input("Enter the name of the question file: ")
    questions = load_questions(filename)

    if questions:
        play_quiz(questions)
    else:
        print("No questions available. Exiting.")

if __name__ == "__main__":
    main()
