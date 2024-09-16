# (Project 1) : Simple Calculator
def simple_calculator():
    def Add(x,y):
         return x+y
    def Subtract(x,y):
        return x-y
    def  Multiply (x,y):
        return x*y
    def Division (x,y):
        if y != 0:
          return x/y
        else:
            return ("Syntax error. Since second number is 0")              
    def Modulus (x,y):
        if y != 0:
          return x/y
        else:
            return ("Syntax error. Since second number is 0")
    
    print("Select operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Division")
    print("5. Modulus")

    select_op=int(input("Enter choice (1/2/3/4/5): "))

    if select_op not in [1,2,3,4,5]:
        print("Invalid operation. Select 1 / 2 / 3 / 4 / 5 this operation.")
        return
    
    try:
        num1=float(input("Enter the first number : "))
        num2=float(input("Enter the Second number : "))

        if select_op == 1:
            result=Add(num1,num2)
            print(f"{num1} + {num2} = {result}")
        elif select_op == 2:
           result=Subtract(num1,num2)
           print(f"{num1} - {num2} = {result}")
        elif select_op == 3:
           result=Multiply(num1,num2)
           print(f"{num1} * {num2} = {result}")
        elif select_op == 4:
           result=Division(num1,num2)
           print(f"{num1} / {num2} = {result}")
        elif select_op == 5:
           result=Modulus(num1,num2)
           print(f"{num1} % {num2} = {result}")

    except:
        print("Invalid data.Please enter numeric values")

simple_calculator()




# # (Project 2): Number Guessing Game
import random

def number_guessing_game():
    print("welcome to the number guessing game.")
    print("Try to guess the number between 1 and 100")

    main_number = random.randint(1,100)
    attempt = 0

    while True:
       try:
          guess_the_number = int(input("Guess the number : "))
          attempt +=1

          if guess_the_number < main_number:
            print("Too low !")
            
          elif guess_the_number > main_number:
            print("Very high !")

          else:
            print(f"Congratulation.You've guessed the in {attempt} attempts")
            break

       except ValueError:
          print("Invalid number .Please try again")
     
number_guessing_game()
