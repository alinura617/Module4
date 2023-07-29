currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait?")  # Added the closing parenthesis for input prompt

currentTimeInt = int(currentTimeStr)  # Corrected the variable names
waitTimeInt = int(waitTimeStr)  # Corrected the variable names

finalTimeInt = currentTimeInt + waitTimeInt
print(finalTimeInt)  # Corrected the variable name

