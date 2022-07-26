num1 = int(input("Enter the first number = "))  
num2 = int(input("Enter the second number = "))

max_n = max(num2,num1)

while True:
    if(max_n%num2==0 and max_n%num1==0):
        break
    max_n = max_n+1

print(f"LCM of {num1} and {num2} is {max_n}")
 
