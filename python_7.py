# Morning time zone starts at 04:00:00 to 11:59:59
# Afternoon time zone starts at 12:00:00 to 15:59:59
# Evening time zone starts at 16:00:00 to 19:59:59
# Night time zone starts at 20:00:00 to 24:59:59

import time

name = input("Enter your name Sir: ").title() #It is used to capitalize the first letter 
current_time = time.strftime('%H:%M:%S') #strftime is used to get the current hour of the day from the system's time
print(current_time)

hour = int(time.strftime('%H'))

if hour <= 4 and hour < 12:
    print("Good Morning",name)

elif hour >= 12 and hour < 15:
        print("Good Afternoon",name)
elif hour >= 15 and hour < 19:
          print("Good Evening",name)
else:
           print("Good Night",name)