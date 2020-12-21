def encrypt(D,K):
    l=len(D)
    while(l%K):
        l+=1
    l2=l
    l3=0
    row=0
    K2=(K-1)*2
    num=0
    temp=""
    while(l>0):
        if(l3+num*k2>len(D)):
            num=0
            l3+=1
            
        temp=temp+D[l3+num*k2]
        num=num+1
        l-=1
def decrypt(D,K):
    #hehehe
def Encryption():
    data=input("Enter a message for encryption: ")
    A=input("Enter the KEY : ")
    print("The encrypted message is:\n"+encrypt(data,A))
    print(encrypt(data,A))
def Decryption():
    data=input("Enter a message for decryption: ")
    A=input("Enter the KEY : ")
    print("The decrypted message is:\n"+decrypt(data,A))
print("Made by group # 4\nNoman Ahmed 42\nTalha Hussain 51")
key=input("Press 1 for Encrypther and any other key for decryption : ")
temp=""
if(key=="1"):
    Encryption()
else:
    Decryption()