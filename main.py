'''TO FIND THE ENCRYPTED AND DECRYPTED WORD FOR THE GIVEN MESSAGE
'''
#THE alphabets has been intialised to the str1 variable 
str1='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

#initializing empty string to encrypt and decrypt variable
encrypt=' '
decrypt=' '

def decrpting():
    decrypt=' '
    for i in msg:
            index=str1.find(i)
            adding=(index-keys)%26
            decrypt+= str1[adding]
    print(f"the decrypted word is: {decrypt} ")


def encrypting():
    encrypt=" "
    for i in msg:
            index=str1.find(i)       #to find the 
            adding=(index+keys)%26   # %26 because there are 26 alphabets 
            encrypt = encrypt+str1[adding] 
    print(f'the message given was:{msg} encrypted to {encrypt}')


while True:
    #msg takes the message that needs to be encrypted or decrypted
    msg=input(str("enter the str: "))
    #the integer key the needs to be added for encryption and subtracted for decrpyt in terms of indicies
    keys=int(input("Enter the key (integer value): "))
#taking variable EnOrDe=>encrypt or decrypt
    EnOrDe=input("Whether you wanted to Encrypt('e') or Decrypt('d'): ")
    if EnOrDe.lower() =='d':
        decrpting()
        
    elif EnOrDe.lower()=='e':
        encrypting()

    #reintialising into empty string because for the next word.orelse it continues with the older words     
    decrypt=' '
    encrypt=' '

    

