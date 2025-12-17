# Quiz Game Program

questions = (("Which planet is known as the Red Planet?:"),
           ("What is the capital city of Australia?:"),
           ("Which gas do humans primarily exhale?"),
           ("Who wrote the play Romeo and Juliet?"))
options = (("A: Mars", "B: Jupiter","C: Saturn","D: Venus"),
           ("A: Canberra", "B: Sydney", "C: Melbourne", "D: Brisbane"),
           ("A: Hydrogen", "B: Nitrogen", "C: Carbon dioxide", "D: Oxygen"),
           ("A: Jane Austen", "B: William Shakespeare", "C: Charles Dickens", "D: Mark Twain"))

answers = ("A", "A", "C", "B")
guesses = []
score = 0
question_number = 0

for question in questions:
    print("--------------------------------------")
    print(question)
    for option in options[question_number]:
            print(option)
    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
          score += 1
          print("Correct!")
    else:
          print("Incorrect!")
          print(f"{answers[question_number]} is the correct answer")
    question_number += 1
print("-------")
print("RESULTS")
print("-------")

for answer in answers:
      print(answer, end = " ")

print()

for guess in guesses:
      print(guess, end = " ")

print()
print(f"Your total score is {int(score/len(questions)*100)}%")