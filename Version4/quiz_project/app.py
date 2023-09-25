quiz = {
    "question1": {
        "question": "What is the capital of Camboida?",
        "answer": "Phnom Penh"
    },
    "question2": {
        "question": "What is the capital of Thailand?",
        "answer": "Bangkok"
    },
    "question3": {
        "question": "What is the capital of Vietnam?",
        "answer": "Hanoi"
    },
    "question4": {
        "question": "Write Apple",
        "answer": "Apple"
    },
    "question5": {
        "question": "What the name fo country beside border on khmer?",
        "answer": "Thailand"
    },
    "question6": {
        "question": "Who is the top Rapper in Cambodia?",
        "answer": "Vannda"
    },
    "question5": {
        "question": "Who is the top community in Cambodia ?",
        "answer": "GD"
    },

}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print("Correct")
        score = score + 1
        print("You score is : " + str(score))
        print("")
        print("")

    else:
        print("Wrong!")
        print("The answer is : " + value['answer'])
        print("Your score is : " + str(score))
        print("")
        print("")
    

print("You got " + str(score) + "out of 7 question correctly")
score_percentage = float((score/7 * 100))
print("Your percentage is " + "{:.2f}%".format(score_percentage))