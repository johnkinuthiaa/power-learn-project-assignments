print("---Personalized Greeting App----")
name =input("Whats your name? :")
color =input("Whats your favourite color? :")
if name != "" and color !="":
    print(f"Hello, {name}! Your favorite color, {color}, is awesome!")
else:
    print("name or color cannot be empty")