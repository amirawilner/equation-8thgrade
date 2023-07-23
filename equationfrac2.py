import random

def generate_equation():
    # Generate a decimal with two digits after the decimal point
    x = round(random.uniform(-10, 10), 2)

    a = random.randint(-10,10)
    b = random.choice([i for i in range(-10, 11) if i != 0])  # b and e cannot be zero as they are denominators
    d = random.randint(-10,10)
    e = random.choice([i for i in range(-10, 11) if i != 0])

    # Calculate c based on x to ensure ((x+a)/b + c == (x+d)/e)
    c = (x + d) / e - (x + a) / b

    return a, b, c, d, e, x

def check_answer(student_answer, correct_answer):
    return abs(student_answer - correct_answer) < 0.01 # For precision up to two decimal places

def main():
    a, b, c, d, e, correct_answer = generate_equation()
    print(f"Solve the equation: (x + {a})/{b} + {round(c, 2)} = (x + {d})/{e}")
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





