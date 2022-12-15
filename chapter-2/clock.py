current_time=float(input("What hour is it now"))
print(current_time)

alarm=float(input("What time do you want to set your alarm for"))
print(alarm)

print((current_time+alarm)%24)