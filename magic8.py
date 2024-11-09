import random
import logging

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

answers = [
    "Yes - definitely",
    "It is decidedly so",
    "Without a doubt",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
    "Absolutely",
    "Certainly",
    "No way",
    "Not in a million years"
]

while True:
    name = input("Enter your name: ")
    question = input("Ask a question: ")
    answer = ""

    if not question:
        print("Please ask a question.")
        continue

    if not name:
        print("Please enter your name.")
        continue

    try:
        random_number = random.randint(1, len(answers))
        assert 1 <= random_number <= len(answers), "Random number out of range: {}".format(random_number)
    except Exception as e:
        logging.error("An error occurred: %s", str(e))
        print("An error occurred. Please try again.")
    else:
        answer = answers[random_number - 1]

        with open("questions_and_answers.log", "a") as log_file:
            log_file.write(f"{name} asks: {question}\n")
            log_file.write(f"Magic 8 Ball's answer: {answer}\n")

        print(f"{name} asks: {question}")
        print(f"Magic 8 Ball's answer: {answer}")

    another_question = input("Do you want to ask another question? (yes/no): ")
    if another_question.lower() != "yes":
        break
