import random


def rand_int_gen(min, max):
    """
    Generate random integer with specified lower & upper bounds
    """
    try:
         rand = random.randint(min,max)
    except:
        rand = random.randint(int(min), int(max))
    return rand


def rand_oper_gen():
    """
        Generate random arithmetic operator
    """
    return random.choice(['+', '-', '*', '/'])


def rand_answer(n1, n2, oper):
    """
            Generate random problem and answer
    """
    p = f"{n1} {oper} {n2}"
    if oper == '+': a = n1 + n2
    elif oper == '-': a = n1 - n2
    elif oper == '*':a = n1 * n2
    else: a = n1/n2

    return p, a

def math_quiz():
    """
        Generate quiz questions and count user's score
    """
    s = 0
    t_q = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = rand_int_gen(1, 10)
        n2 = rand_int_gen(1, 5.5)
        o = rand_oper_gen()

        PROBLEM, ANSWER = rand_answer(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER: #correct answer
            print("Correct! You earned a point.")
            s += -(-1)
        else: #incorrect answer
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
