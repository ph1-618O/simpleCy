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
    
query = input("Decode, or Code? ")
query = query.lower()
if query == 'decode':
    decodeMessage = input("Enter coded message:: ")
    print(f"Message Recieved: {decodeMessage}")
    shiftNum = int(input("Enter the shift:: "))
    print(f'Shift Entered: {shiftNum}')
    if shiftNum == 25:
        print('Invalid shift, please choose again. ')
        shiftNum = int(input('Enter a different number: '))
    return print(f'This is your coded message:: {decoder(decodeMessage, shiftNum)}')