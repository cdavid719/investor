import hashlib, binascii, os, psycopg2, re, math
#from classes import User

digits=0
def ccCheck(): #Verifies CC number.
    ccInput= int(input("What is your card number?  "))
    digits= int(math.log10(ccInput))+1 #Gets input length and stores it in digits
    if digits != 12:
        print("That number is not 12 digits long.")
        ccCheck()
    else: 
        expCheck()
  

def expCheck():
    expInput= int(input("Expiration date?  "))
    digits= int(math.log10(expInput))+1
    if digits != 4:
        print("That number is not 4 digits long.")
        expCheck()
    else: 
        cvcCheck()
   
    
def cvcCheck():
    cvcInput = int(input("What is the CVC? "))
    digits= int(math.log10(cvcInput))+1
    if digits != 3:
        print("That number is not 3 digits long.")
        cvcCheck()


ccCheck() #Starts Program
    


# print("Allow us to verify this information.")
# def hash_creditCardNum(creditCardNum):
#     #Hash a creditCardNum for storing.
#     salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
#     cardHash = hashlib.pbkdf2_hmac('sha512', creditCardNum.encode('utf-8'), 
#                                 salt, 100000)
#     cardHash = binascii.hexlify(cardHash)
#     return (salt + cardHash).decode('ascii')
# def verify_creditCardNum(stored_creditCardNum, provided_creditCardNum):
#     #Verify a stored creditCardNum against one provided by user
#     salt = stored_creditCardNum[:64]
#     stored_creditCardNum = stored_creditCardNum[64:]
#     cardHash = hashlib.pbkdf2_hmac('sha512', 
#                                 provided_creditCardNum.encode('utf-8'), 
#                                 salt.encode('ascii'), 
#                                 100000)
#     cardHash = binascii.hexlify(cardHash).decode('ascii')
#     return cardHash == stored_creditCardNum