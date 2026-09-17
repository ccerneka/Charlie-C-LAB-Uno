name = input("enter your name: ")
age = int(input("enter your age: "))
color = input("enter your color: ")

if age >= 18:
    print(f"Hello, {name}! You are an adult and your favorite color is {color}. Nice choice!")
else:
    print(f"Hello, {name}! You are a minor and your favorite color is {color}. That's a fun color!")

if color.lower() in ["blue", "green", "purple"]:
    print(f"{color} is a calm and beautiful color.")
elif color.lower() in ["red", "yellow", "orange"]:
    print(f"{color} is a bright and energetic color.")
else:
    print(f"{color} is a unique color.")