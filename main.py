MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', 
    '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', '/': '-..-.', 
    '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

def text_to_morse(text):
    morse = []
    for char in text.upper():
        morse_code = MORSE_CODE_DICT.get(char)
        if morse_code is not None:
            morse.append(morse_code)
    return ' '.join(morse)

def morse_to_text(morse):
    text = []
    for code in morse.split():
        for char, morse_code in MORSE_CODE_DICT.items():
            if code == morse_code:
                text.append(char)
                break
    return ''.join(text)

def encryption(str,key):
    strr=list()
    str1=list()
    for i in str:
        strr.append(i)
    for j in strr:
        code=ord(j)
        ncode= int(code)+int(key)
        if ncode>122:
            ncode-=26
        if(code==32):
            ncode=32
        str1.append(chr(ncode))
            
    print("Encrypted text:")
    for k in str1:
        print(k,end="")
        
def decryption(str,key):
    strr=list()
    str1=list()
    for i in str:
        strr.append(i)
    for j in strr:
        code=ord(j)
        ncode= int(code)-int(key)
        if ncode<96:
            ncode+=26
        if(code==32):
            ncode=32
        str1.append(chr(ncode))

    print("Decrypted text:")
    for k in str1:
        print(k,end="")

def dicti():
  for key,value in MORSE_CODE_DICT.items():
	        print(key, ':', value)
        
while True:
    try:       
        print("\nEnter your choice")
        choice = int(input("1.TEXT TO MORSE\n2.MORSE TO TEST\n3.ENCRYPT THE TEXT\n4.DECRYPT THE TEXT\n5.PRINT MORSE CODE DICTIONARY\n6.QUIT\n\n"))

        if (choice==1):
            print("Converting text to morse code")
            text=input("Enter the text: ")
            print("Converted morse code is ",text_to_morse(text))
            continue
            
        
        elif(choice==2):
            print("Converting text to morse code")
            morse=input("Enter the morse code: ")
            print("Convertes text is ",morse_to_text(morse))
            continue
            
        elif(choice==3):
            print("Encrypting the text")
            text=input("Enter the text: ")
            ekey=int(input("Enter the key: "))
            encryption(text,ekey)
            print()
            
        elif(choice==4):
            print("Decrypting the text")
            text=input("Enter the text: ")
            dkey=int(input("Enter the key: "))
            decryption(text,dkey)
            print()
        elif(choice==5):
            print("This is the text to morse dictionary")
            dicti()
        elif(choice==6):
            break
        
        else:
            print ("please enter a value")
    except ValueError:
        print("Enter a valid option") 
        continue          
