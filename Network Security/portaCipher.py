    
#Group 4
#Made by Talha Hussain 51 and Noman Ahmed 42
def Key(key,data):
    temp=""
    inc=0
    A=len(key)
    for x in data:
        temp=temp+key[inc%A]
        inc+=1
    return temp
def encryption2(data,A):
    temp=""
    inc=0
    y=Key(A,data)
    for x in data:
        if(y[inc]>="A" and y[inc]<="Z"):
            b=ord(y[inc])-65
        elif(y[inc]>="a" and y[inc]<="z"):
            b=ord(y[inc])-97
        if(x>="A" and x<="Z"):
            a=ord(x)-65
            c=(a+13)%26
            if(a<13):
                b=(int(b/2)+c)%13
                c=b+13
            else:
                b=(c-int(b/2))%13
                c=b
            temp=temp+chr(c+65)
        elif(x>="a" and x<="z"):
            a=ord(x)-97
            c=(a+13)%26
            if(a<=13):
                b=(int(b/2)+c)%13
                c=b+13
            else:
                b=(c-int(b/2))%13
                c=b
            temp=temp+chr(c+97)
        elif(x==" "):
            temp=temp+x
            inc=inc-1
        inc+=1
    return temp
def decryption2(data,A):
    temp=""
    inc=0
    y=Key(A,data)
    for x in data:
        if(y[inc]>="A" and y[inc]<="Z"):
            b=ord(y[inc])-65
        elif(y[inc]>="a" and y[inc]<="z"):
            b=ord(y[inc])-97
        if(x>="A" and x<="Z"):
            a=ord(x)-65
            if(a>13):
                c=a-13
                c=(int(b/2)-c)%13
            else:
                c=(int(b/2)+a)%13
                c=c+13
            c=(a+13)%26
            if(a<13):
                b=(int(b/2)+c)%13
                c=b+13
            else:
                b=(c-int(b/2))%13
                c=b
            temp=temp+chr(c+65)
        elif(x>="a" and x<="z"):
            a=ord(x)-97
            c=(a+13)%26
            if(a<=13):
                b=(int(b/2)+c)%13
                c=b+13
            else:
                b=(c-int(b/2))%13
                c=b
            temp=temp+chr(c+97)
        elif(x==" "):
            temp=temp+x
            inc=inc-1
        inc+=1
    return temp
def Encryption():
    data=input("Enter a message for encryption: ")
    A=input("Enter the KEY : ")
    print("The encrypted message is:\n"+encryption2(data,A))
def Decryption():
    data=input("Enter a message for decryption: ")
    A=input("Enter the KEY : ")
    print("The decrypted message is:\n"+decryption2(data,A))
print("Made by group # 4\nNoman Ahmed 42\nTalha Hussain 51")
key=input("Press 1 for Encrypther and any other key for decryption : ")
temp=""
if(key=="1"):
    Encryption()
    #print(Key("PRACTICE","ASSIGNMENTDUENEXTCLASS"))
else:
    Decryption()