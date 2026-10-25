age = input("Enter your age:")
age_int = int(age)
if age_int < 13:
    print("You are a Child.")
elif age_int < 20:
    print("You are a Teenager.")
elif age_int < 60:
    print("You are an Adult.")
else:
    print("You are a Senior Citizen.")
