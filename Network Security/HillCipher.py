#Made By Talha Hussain  Bhutto B17158051
def encrypt(data,key):
    d=data
    data=""
    for x in d:
        if(x!=" "):
            data=data+x
    temp=[]
    a=0
    b=0
    if(len(data)%2==1):
        data=data+"X"
    stop=len(data)/2
    l1=0
    while(l1<stop):
        a=b=0
        if(data[l1*2]>="a" and data[l1*2]<="z" and data[l1*2+1]>="a" and data[l1*2+1]<="z"):
            a=ord(data[l1*2])-97
            b=ord(data[l1*2+1])-97
        elif(data[l1*2]>="A" and data[l1*2]<="Z" and data[l1*2+1]>="A" and data[l1*2+1]<="Z"):
            a=ord(data[l1*2])-65
            b=ord(data[l1*2+1])-65
        else:
            return "Plese enter a character from A-Z or a-z"
        temp.append([a,b])
        l1+=1
    return temp   
def decrypt(a,b):
    a+b
def Encryption():
    data=input("Enter a message for encryption: ")
    A=input("Enter the key : ")
    #print("The encrypted message is:\n"+encrypt(data,A))
    print(encrypt(data,A))
def Decryption():
    data=input("Enter a message for decryption: ")
    A=input("Enter the key : ")
    print("The decrypted message is:\n"+decrypt(data,A))
print("Made by group # 4\nNoman Ahmed 42\nTalha Hussain 51")
key=int(input("Press 1 for Encrypther and any other key for decryption : "))
temp=""
if(key==1):
    Encryption()
else:
    Decryption()