HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE, 'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("No history found!")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(HISTORY_FILE, 'w')
    file.close()
    print("History clearead.")

def save_to_history(equation, result):
    file = open(HISTORY_FILE, 'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts)!=3:
        print("Invalid input. Use format: number operator number (e.g 8 + 8)")
        return
    
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == "0":
            print("Cann't divide by zero")
            return
        result = num1 / num2
    else:
        print("Invalid operator. USE ONLY (+,-,*,/)")
        return
    
    if int(result) == result:
        result = int(result)
    print("Result:", result)
    save_to_history(user_input, result)


def main():
    print('----- SIMPLE CALCULATOR (type history, clear or exit)')
    while True:
        user_input = input("Enter calculator (+,-,*,/) or command (history, clear) : ")
        if user_input == 'exit':
            print('Goodbye')
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculate(user_input)

main()