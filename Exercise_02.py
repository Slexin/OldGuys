listLower = [chr(i) for i in range(97, 123)]
listUpper = [chr(i) for i in range(65,91)]

def encoderCaesar(strng, shift):
    result = ""
    for i in strng:
        if i.isupper():   
            charI = listUpper.index(i)         
            result += listUpper[(charI+shift)%26]
        elif i.islower(): 
            charI = listLower.index(i)
            result += listLower[(charI+shift)%26]
        else:
            result+= i
            
    return result

def main():
    strng = input("Input what string you want to encode: ")
    shift = int(input("How many times to you want to shift? Choose a number between 1 and 25! "))
    if shift <1 or shift >25:
        print("You don't handle instructions very well, do you?")
        return 
    print(encoderCaesar(strng, shift))

main()

