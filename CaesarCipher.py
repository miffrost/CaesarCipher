aakkoset = 'abcdefghijklmnopqrstuvwxyzåäö'

def siirra(i,k, m):
    while i+k>=m:
        i = i - m
    return i + k

def CaesarCipher(teksti, k):
    global aakkoset
    numeroidutAakkoset = {aakkoset[i]:i for i in range(len(aakkoset))}
    teksti = teksti.lower()
    return "".join([aakkoset[siirra(numeroidutAakkoset[i],k,len(aakkoset))] if i in aakkoset else i for i in teksti])
    
def main():
    s = ""
    viesti = str(input("Kirjoita viestisi tähän:\n"))
    print(" - - - ")
    for i in range(len(aakkoset)):
        print("+" + str(i) + ": " + CaesarCipher(viesti,i))

main()