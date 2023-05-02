MORSE_CODE_DICT = {
    """
    This is a Python program that allows the user to convert text to Morse code, Morse code to text,
    encrypt and decrypt text using a key, and print the Morse code dictionary.
    
    :param text: The input text that the user wants to convert to morse code or encrypt/decrypt
    :return: The code does not return anything, it only prints output to the console.
    """
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', 
    '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', '/': '-..-.', 
    '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

def text_to_morse(text):
    """
    The above code contains functions for converting text to Morse code, Morse code to text, encryption
    and decryption of text using a given key, and displaying the Morse code dictionary.
    
    :param text: The text that needs to be converted to Morse code or decrypted/encrypted
    :return: There are multiple functions in the code, each returning a different value:
    - `text_to_morse(text)` function returns a string of morse code representation of the input text.
    - `morse_to_text(morse)` function returns a string of text representation of the input morse code.
    - `encryption(str,key)` and `decryption(str,key)` functions do not return anything, but print
    """
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
        
# This code block is creating a menu-driven program that allows the user to choose from various
# options such as converting text to Morse code, Morse code to text, encrypting and decrypting text
# using a key, and printing the Morse code dictionary. The `while True:` loop ensures that the program
# keeps running until the user chooses to quit. The `try-except` block is used to handle any invalid
# input from the user. The user's choice is taken as input using the `input()` function and is
# converted to an integer using the `int()` function. Based on the user's choice, the corresponding
# function is called. The `continue` statement is used to go back to the start of the loop and display
# the menu again after the function has been executed. The `break` statement is used to exit the loop
# and end the program when the user chooses to quit.
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
