import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def calculator():
    print("Enter the operator that you want to perform (+, -, *, /, %, ^): ")
    speak("Enter the operator that you want to perform.")
    operator = input("Operator: ")

    if operator in ('+', '-', '*', '/'):
        print(f"How many numbers do you want to {operator}?")
        speak(f"How many numbers do you want to {operator}?")
        count = int(input("Enter count: "))

        numbers = []
        for i in range(count):
            print(f"Enter number {i + 1}: ")
            speak(f"Enter number {i + 1}.")
            num = float(input())
            numbers.append(num)

        if operator == '+':
            result = sum(numbers)
            print(f"The sum is: {result}")
            speak(f"The sum is {result}.")
        elif operator == '-':
            result = numbers[0]
            for num in numbers[1:]:
                result -= num
            print(f"The result of subtraction is: {result}")
            speak(f"The result of subtraction is {result}.")
        elif operator == '*':
            result = 1
            for num in numbers:
                result *= num
            print(f"The product is: {result}")
            speak(f"The product is {result}.")
        elif operator == '/':
            result = numbers[0]
            for num in numbers[1:]:
                if num == 0:
                    print("Division by zero is not allowed.")
                    speak("Division by zero is not allowed.")
                    return
                result /= num
            print(f"The result of division is: {result}")
            speak(f"The result of division is {result}.")
    elif operator == '%':
        print("Enter the first number: ")
        speak("Enter the first number.")
        a = int(input())

        print("Enter the second number: ")
        speak("Enter the second number.")
        b = int(input())

        result = a % b
        print(f"The remainder is: {result}")
        speak(f"The remainder is {result}.")
    elif operator == '^':
        print("Enter the base number: ")
        speak("Enter the base number.")
        a = int(input())

        print("Enter the exponent: ")
        speak("Enter the exponent.")
        b = int(input())

        result = a ** b
        print(f"The result of {a}^{b} is: {result}")
        speak(f"The result of {a} raised to the power of {b} is {result}.")
    else:
        print("Invalid operator.")
        speak("Invalid operator.")

if __name__ == "__main__":
    calculator()
