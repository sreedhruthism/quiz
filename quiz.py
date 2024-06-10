questions = ("What is smallest prime number?: ",
                       "What is capital of China?: ",
                       "Which gas makes up the majority of Earth's atmosphere?: ",
                       "In which year did the American Civil War end?: ",
                       "Which is the most sensitive organ in our body?: ")

options = (("A. 0", "B. 1", "C. 2", "D. -1"),
                   ("A. Delhi", "B. Turkey", "C. Sydney", "D. Beijing"),
                   ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
                   ("A. 1890", "B. 1978", "C. 1786", "D. 1865"),
                   ("A. Nose", "B. Eyes", "C. Ears", "D. Skin"))

answers = ("C", "D", "A", "D", "D")
guesses = []
score = 0
question_num = 0


for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")


print("Sree Dhruthi Mulakaledu / Jain University")