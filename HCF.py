num1 = int(input("Enter the first number = "))  
num2 = int(input("Enter the second number = "))
if num1>num2:
    min_n = num2
else:
    min_n = num1
for i in range(1,min_n+1):
    if num1%i==0 and num2%i==0:
        hcf = i

print(f"HCF of {num1} and {num2} is {hcf}")
 
