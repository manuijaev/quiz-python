import random
questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "Which programming language is known as the 'language of the web'?",
        "choices": ["A) Python", "B) JavaScript", "C) C++", "D) Java"],
        "answer": "B"
    },
    {
        "question": "Who developed the theory of relativity?",
        "choices": ["A) Isaac Newton", "B) Nikola Tesla", "C) Albert Einstein", "D) Galileo Galilei"],
        "answer": "C"
    },
    {
        "question": "What is 5 + 7?",
        "choices": ["A) 10", "B) 11", "C) 12", "D) 13"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B"
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
