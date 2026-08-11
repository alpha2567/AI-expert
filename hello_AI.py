name = input("hello i am AI bot what is you name?:")
print(f"nice to meet you {name}")
mood = input("how are you feeling today?(good/bad):").lower()
if mood == "good":
    print("i am glad to hear that")
elif mood == "bad":
    print("i am sorry to hear that")
else:
    print("invalid input")
print(f"it was nice chatting with you {name}, goodbye") 