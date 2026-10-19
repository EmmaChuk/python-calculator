history = []

while True:
    op = input("Pick any operation (+, -, /, *), 'exit' to cancel, 'history' to view history, 'clear' to clear history: ").lower()
    
    if op == "exit":
        break
        
    elif op == "clear":
        history.clear()
        print("History cleared")
        continue
        
    elif op == "history":
        if not history:
            print("No history yet")
        else:
            for i in history:
                print(i)
        continue
                
    if op not in ["+", "-", "*", "/"]:
        print("Invalid Operation")
        continue
        
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))   
    except ValueError:
        print("Not a Number")
        continue
   
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Invalid Format!")
            continue
        else:
            result = num1 / num2
    
    cal = f"{num1} {op} {num2} = {result}" 
    print(cal)
    if len(history) < 5:
        history.append(cal)
    else:
        print("Storage Full")
     