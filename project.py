
import sys
cal = input("введите числа и операции: ")
cal = cal.split()
numbers = []

for i in cal:
    if i in ("+","-","*","/","^"):
        
        if len(numbers) < 2:
            print("ошибка")
            sys.exit(1)
        b = numbers.pop()
        a = numbers.pop()
        
        if i == "+": 
            numbers.append(a+b)
            
        elif i == "-": 
            numbers.append(a-b)
            
        elif i == "*": 
            numbers.append(a*b)
            
        elif i == "/": 
            if b==0: 
                print("деление на 0")
                sys.exit(1)
            numbers.append(a/b)
            
        elif i == "^": 
            numbers.append(a**b)
            
    else:
        numbers.append(float(i))
    	
print(numbers)

