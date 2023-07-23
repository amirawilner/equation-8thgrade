import random

def generate_equation():
    a = random.randint(-10,10)
    # b and d cannot be zero as they are denominators
    b = random.choice([i for i in range(-10, 11) if i != 0])
    c = random.randint(-10,10)
    d = random.choice([i for i in range(-10, 11) if i != 0])

    # Generate a decimal with two digits after the decimal point
    x = round(random.uniform(-10, 10), 2)
    
    # Ensure ((x+a)*d == (x+c)*b) to keep equation balanced
    while not ((x + a) * d == (x + c) * b):
        x = round(random.uniform(-10, 10), 2)

    return a, b, c, d, x

def check_answer(student_answer, correct_answer):
    return abs(student_answer - correct_answer) < 0.01 # For precision up to two decimal places

def main():
    a, b, c, d, correct_answer = generate_equation()
    print(f"Solve the equation: (x + {a})/{b} = (x + {c})/{d}")
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

