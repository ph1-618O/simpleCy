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