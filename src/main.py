from src.algorithm import encode, decode

choice = int(input("Which one would i like to choose"))
print("1. Encode")
print("2. Decode")

if choice == 1:
    print("You have chosen encode")
    encode()
elif choice == 2:
    print("You have chosen decode")
    decode()
