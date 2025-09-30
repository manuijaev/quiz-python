import random
questions = [
    {
        "question": "What color is the sky on a clear day?",
        "choices": ["A) Green", "B) Blue", "C) Red", "D) Yellow"],
        "answer": "B"
    },
    {
        "question": "How many legs does a cat have?",
        "choices": ["A) Two", "B) Three", "C) Four", "D) Five"],
        "answer": "C"
    },
    {
        "question": "What is 2 + 2?",
        "choices": ["A) 3", "B) 4", "C) 5", "D) 6"],
        "answer": "B"
    },
    {
        "question": "Which fruit is yellow and curved?",
        "choices": ["A) Apple", "B) Banana", "C) Orange", "D) Mango"],
        "answer": "B"
    },
    {
        "question": "Which day comes after Monday?",
        "choices": ["A) Sunday", "B) Wednesday", "C) Tuesday", "D) Friday"],
        "answer": "C"
    }
]

random.shuffle(questions)

score = 0

print("Welcome to the CLI Quiz Game!")
print("Type A, B, C, or D to answer.")

for idx, q in enumerate(questions, 1):
    print(f"Q{idx}: {q['question']}")
    for choice in q['choices']:
        print(choice)

    
    while True:
        try:
            answer = input("Your answer: ").strip().upper()
            if answer not in ["A", "B", "C", "D"]:
                raise ValueError("Invalid choice! Please enter A, B, C, or D.")
            break
        except ValueError as e:
            print(e)

    
    if answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was {q['answer']}.")
print("Quiz Over!")
print(f"Your final score is {score}/{len(questions)}.")

if score == len(questions):
    print(" Excellent! Perfect score!")
elif score >= len(questions) // 2:
    print(" Good job, you did well!")
else:
    print("Try Again! Keep practicing!")
