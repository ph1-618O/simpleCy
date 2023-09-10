def validate_text(p_text):
    try:
        eval(p_text)
        print(eval(p_text))
        print("Invalid Input Try Again")
    except:
        print("Data is accepted")
        
def decoder(coded, shift):
    decoded = []
    for char in coded:
        if char.isalpha():
            char = char.lower()
            limitAlpha = ord(char) - shift
            if (limitAlpha < ord('a')) :
                backshift = ord('a') - limitAlpha
                backshift = ord('z') - backshift
                backshift = chr(backshift)
                #print(f'Backshift : {backshift}')
                decoded.append(backshift)
            else:
                decoded.append(chr(limitAlpha))
    return ''.join(decoded)
    
def caesar(uncoded, shift):
    coded = []
    for char in uncoded:
        if char.isalpha():
            char = char.lower()
            limitAlpha = ord(char) + shift
            if (limitAlpha >= ord('a')) & (limitAlpha <= ord('z')) :
                limitAlpha = chr(limitAlpha)
                #print(f'LimitAlpha: {limitAlpha}')
                coded.append(limitAlpha)
            else:
                frontShift = ((limitAlpha % ord('z')) % 26) + ord('a')
                #print(f'Frontshift: {frontShift}')
                coded.append(chr(frontShift))
                #coded.append(frontShift)
    return ''.join(coded)
    
def askInput():
    query = input("Decode, or Code? ")
    query = query.lower()
    validate_text(query)
    if query == 'decode':
        decodeMessage = input("Enter coded message:: ")
        validate_text(decodeMessage)
        print(f"Message Recieved: {decodeMessage}")
        shiftNum = int(input("Enter the shift:: "))
        print(f'Shift Entered: {shiftNum}')
        if shiftNum == 25:
            print('Invalid shift, please choose again. ')
            shiftNum = int(input('Enter a different number: '))
        return print(f'This is your coded message:: {decoder(decodeMessage, shiftNum)}')
    else:
        toCode = input('Enter message to code:: ')
        print(f"Message Recieved: {toCode}")
        validate_text(toCode)
        shiftNum = int(input('Enter the shift:')) - 1
        #removing 1 because 1 = 0
        print(f'Shift Entered: {shiftNum}')
        
        if shiftNum == 25:
            print('Invalid shift, please choose again. ')
            shiftNum = int(input('Enter a different number: '))
        return print(f'This is your coded message:: {caesar(toCode, shiftNum)}')
        
        
print(askInput())
