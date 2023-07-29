str_time = input("What time is it now?")  # Corrected variable name
str_wait_time = input("What is the number of hours to wait?")  # Added the missing closing parenthesis

time = int(str_time)
wait_time = int(str_wait_time)  # Corrected variable name

time_when_alarm_goes_off = time + wait_time  # Corrected variable name and a typo in the variable name

print(time_when_alarm_goes_off)  # Corrected variable name
