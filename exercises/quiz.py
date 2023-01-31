import json

with open("files/quiz.json", "r") as file:
    content = file.read()

quiz = json.loads(content)

score = 0
for question in quiz:
    print(question["question"])
    for index, alternative in enumerate(question["answers"]):
        print(index + 1, " - ", alternative)
    user = int(input("Enter the number of the correct answer: "))
    print(f"You entered: {user} - {question['answers'][user - 1]}, which is ", end='')
    if question["correct"] == user:
        score += 1
        print("correct")
    else:
        print("incorrect")

print("Your score is", score, "out of", len(quiz))