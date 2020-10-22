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