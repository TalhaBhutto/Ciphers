def encrypt(Data,key):
    l=len(Data)
    l2=0
    temp=""
    num=0
    while((l/key)%1):
        l=l+1
        Data=Data+"X"
    col=int(l/key)
    while(l2<l):
        temp=temp+Data[(l2%key)*col+num]
        l2=l2+1
        if(l2%key==0):
            num=num+1
    return temp
def decrypt(Data,key):
    l=len(Data)
    l2=0
    num=0
    temp=""
    col=int(l/key)
    while(l2<l):
        temp=temp+Data[(l2%col)*key+num]
        l2=l2+1
        if(l2%col==0):
            num=num+1
    return temp
def Encryption():
    #data=input("Enter a message for encryption: ")
    #A=int(input("Enter the KEY : "))
    data="WEARESTUDYINGANDTRYINGTOUNDERSTANDTRANSPOSITIONCIPHERS"
    A=4
    print("The encrypted message is:\n"+encrypt(data,A))
def Decryption():
    #data=input("Enter a message for decryption: ")
    #A=int(input("Enter the KEY : "))
    data="WNRIEDSTATTIRRAOEYNNSIDCTNTIUGRPDTAHYONEIUSRNNPSGDOXAESX"
    A=4
    print("The decrypted message is:\n"+decrypt(data,A))
print("Made by group # 4\nNoman Ahmed 42\nTalha Hussain 51")
key=input("Press 1 for Encrypther and any other key for decryption : ")
temp=""
if(key=="1"):
    Encryption()
else:
    Decryption()