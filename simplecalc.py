while True:
   print("Options:")
   print("Enter 'add' to add two numbers")
   print("Enter 'subtract' to subtract two numbers")
   print("Enter 'multiply' to multiply two numbers")
   print("Enter 'divide' to divide two numbers")
   print("Enter 'q' to end the program")
   user_input = input(": ")

   if user_input == "q":
      break
   elif user_input == "add":
      num1 = int(input("First Number: "))
      if type(num1) is not (int or float):
          print("Input must be a number")
          break
      num2 = int(input("Second Number: "))
      result =  num1 + num2
      print("The answer is: "+ str(result))
   elif user_input == "subtract":
      num1 = int(input("First Number: "))
      num2 = int(input("Second Number: "))
      result =  num1 - num2
      print("The answer is: "+ str(result))
   elif user_input == "multiply":
      num1 = int(input("First Number: "))
      num2 = int(input("Second Number: "))
      result =  num1 * num2
      print("The answer is: "+ str(result))
   elif user_input == "divide":
      num1 = int(input("First Number: "))
      num2 = int(input("Second Number: "))
      result =  num1 / num2
      print("The answer is: "+ str(result))
   else:
      print("Unknown input")