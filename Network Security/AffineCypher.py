#Group 4
#Made by Talha Hussain 51 and Noman Ahmed 42
def affine(data,A,B):
    temp=""
    for x in data:
        if(x>="A" and x<="Z"):
            a=ord(x)
            c=a-65
            c=(c*A+B)%26
            c=65+c
            d=int(c)
            temp=temp+chr(d)
        elif(x>="a" and x<="z"):
            a=ord(x)
            c=a-97
            c=(c*A+B)%26
            c=97+c
            d=int(c)
            temp=temp+chr(d)
        elif(x==" "):
            temp=temp+x
    return temp
def affine2(data,A_inverse,A,B):
    temp=""
    for x in data:
        if(x>="A" and x<="Z"):
            a=ord(x)
            c=a-65.0
            c=(A_inverse*(c-B))%26
            c=65+c
            d=int(c)
            temp=temp+chr(d)
        elif(x>="a" and x<="z"):
            a=ord(x)
            c=a-97
            c=(A_inverse*(c-B))%26
            c=97+c
            d=int(c)
            temp=temp+chr(d)
        elif(x==" "):
            temp=temp+x
    return temp
def Encryption():
    data=input("Enter a message for encryption: ")
    A=int(input("Enter the value of a : "))
    B=int(input("Enter the value of b : "))
    print("The encrypted message is:\n"+affine(data,A,B))
def Decryption():
    data=input("Enter a message for decryption: ")
    A=float(input("Enter the value of a : "))
    A_inverse=27/A
    B=float(input("Enter the value of b : "))
    print("The decrypted message is:\n"+affine2(data,A_inverse,A,B))
print("Made by group # 4\nNoman Ahmed 42\nTalha Hussain 51")
key=int(input("Press 1 for Encrypther and any other key for decryption : "))
temp=""
if(key==1):
    Encryption()
else:
    Decryption()