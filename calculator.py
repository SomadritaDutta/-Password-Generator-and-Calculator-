n=int(input("How many numbers you want for the operation?"))
def add_calc(numbers):
    return sum(numbers)

def sub_calc(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -=num
    return result

def mult_calc(numbers):
    result = numbers[0]
    for i in numbers[1:]:
        result =result * i
    return result  

def div_calc(numbers):
    result = numbers[0]
    for divi in numbers[1:]:
        if divi==0:
            return "Zero is not allowed"
        result = result / divi
    return result      
while True:    
 print("Choose an operation ")
 print("\n 1.Addition\t2.Substract\t3.Multiplication\t4.Division\t5.Quit") 
 choice=int(input("Enter your choice"))

 if choice ==5:
    print("Stop")
    break

 if choice not in [1,2,3,4]:
    print("Invalid Choice")
    continue

 numbers=[]
 for i in range(n):
    num = float(input(f"Enter number{i+1}:"))
    numbers.append(num)

 if choice==1:
    result = add_calc(numbers)
    print("The result: ",result)
 elif choice==2:
    result = sub_calc(numbers)
    print("The result: ",result)
 elif choice==3:
    result = mult_calc(numbers)
    print("The result: ",result)
 elif choice==4:
    result = div_calc(numbers)
    print("The result: ",result)

    
   