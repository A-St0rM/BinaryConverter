from src.algorithm import encode, decode

print("1. Encode")
print("2. Decode")
choice = int(input("Which one would you like to choose: "))


if choice == 1:
    print("You have chosen encode")
    chosenSentence = input("What would you like to encode to binary?: ")
    encodedBinary = encode(chosenSentence)
    print(encodedBinary)

elif choice == 2:
    print("You have chosen decode")
    decode()
