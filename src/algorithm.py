
alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','æ','ø','å')

def encode(input):

    splitInput = list(str(input.lower()))
    encodedBinary = ""
    binary = []

    for j in range(len(splitInput)):
        binaryControlValue = 16
        for i in range(len(alphabet)):

            if alphabet[i] == splitInput[j]:
                indexForCharacter = i+1
                for k in range(5):
                    if indexForCharacter >= binaryControlValue:
                        indexForCharacter = indexForCharacter - binaryControlValue
                        encodedBinary += "1"
                    else:
                        encodedBinary += "0"

                    binaryControlValue = binaryControlValue/2

                encodedBinary += " "
            elif splitInput[j] == " ":
                encodedBinary += ", "
                break
    return encodedBinary



def decode():
    return None