import random

def generate_equation():
    # Generate a decimal with two digits after the decimal point
    x = round(random.uniform(-10, 10), 2)

    a = random.randint(-10,10)
    b = random.randint(-10,10)
    c = random.choice([i for i in range(-10, 11) if i != 0])  # c cannot be zero as it's a denominator
    d = random.randint(-10,10)
    e = random.randint(-10,10)
    f = random.randint(-10,10)
    h = random.choice([i for i in range(-10, 11) if i != 0])  # h cannot be zero as it's a denominator
    i = random.randint(-10,10)
    g = int((c * a * (x + b) + c * d * x - e * f * x - i * h) / e)

    return a, b, c, d, e, f, g, h, i, x

def check_answer(student_answer, correct_answer):
    return abs(student_answer - correct_answer) < 0.01 # For precision up to two decimal places

def main():
    a, b, c, d, e, f, g, h, i, correct_answer = generate_equation()
    print(f"Solve the equation: {a}*(x + {b})/{c} + {d}x = {e}({f}x + {g})/{h} + {i}")
    student_answer = input("Your answer (format x=value): ")

    # Parse the student answer to obtain value after "x="
    try:
        student_answer = round(float(student_answer.split('=')[1]), 2)
    except:
        print("Invalid input format!")
        return

    if check_answer(student_answer, correct_answer):
        print("Correct!")
    else:
        print("Incorrect!")
    print(f"The correct answer is x={round(correct_answer, 2)}")

if __name__ == "__main__":
    main()



