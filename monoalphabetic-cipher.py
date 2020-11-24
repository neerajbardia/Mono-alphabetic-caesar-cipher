#monoalphabetic cipher

dict_values={'a':'n','b':'h','c':'d','d':'r','e':'z','f':'k','g':'a','h':'p','i':'s','j':'l','k':'u','l':'c','m':'j','n':'f','o':'w','p':'e','q':'g','r':'x','s':'m','t':'b','u':'i','v':'o','w':'v','x':'q','y':'t','z':'y',' ':' '}
#the above dictionary is where the letter substitutions are defined, it can be changed as we want but remember to change it such that no letters are repeated

cipher_text=""
decoding=""
def get_key(val): 
    for key, value in dict_values.items():                               #function to return the key when its respective value is passed
        if val == value: 
            return key
            
choice=int(input("Select \n 1. Encryption \n 2. Decryption \n Enter your choice:"))
if choice==1:
    plain_text=input("Enter the plain-text:")                            #input plain text
    
    for i in range(0,len(plain_text)):
        cipher_text+=dict_values[plain_text[i]]                          #generating cipher text
    print("Encrypted text:",cipher_text)                                 
    
elif choice==2:     
    cipher_text=input("Enter the cipher-text:")                          #input cipher text
    for i in range(0,len(cipher_text)):
        decoding+=get_key(cipher_text[i])                                #generating the plain text
    print("Decoded text:",decoding)
