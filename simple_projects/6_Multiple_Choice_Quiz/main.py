from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are banannas?\n(a) Teel\n(b) Blue\n(c) Yellow\n\n",
    "What color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Magenda\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt + "\n")
        if answer == question.answer:
            score += 1
    print("You got : " + str(score) + "/" + str(len(questions)))
            
run_quiz(questions)