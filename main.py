import time

t = int(input("Enter the time : "))

        
current_time = time.strftime('%H:%M:%S')
print(current_time)
current_hour = int(time.strftime( '%H'))
print(current_hour)
current_minute = int(time.strftime( '%M'))
print(current_minute)
current_seconds = int(time.strftime( '%S'))
print(current_seconds)


if current_hour < 12:
    print("Good Morning")
elif current_hour <= 12 and current_hour < 16:
    print("Good Afternoon")  
else:
    print("Good Evening")
  











