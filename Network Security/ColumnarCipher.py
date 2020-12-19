def encrypt(Data,key):
    l=len(Data)
    l2=0
    temp2=[]
    temp2.append("{")
    temp=""
    k2=""
    num=0
    num2=0
    num4=0
    row=0
    LK=int(len(key))
    while((l/LK)%1):
        l=l+1
        Data=Data+"X"
    row=int(l/LK)
    while(l2<l):
        temp=temp+Data[(l2%row)*LK+num]
        l2=l2+1
        if(l2%row==0):
            temp2.append(key[num]+temp)
            temp=""
            num=num+1
    for x in temp2:
        num=0
        num2=0
        num3=0
        for y in temp2:
            if(x[0]>y[0]):
                x=y
        x2=""
        for z in x:
            if(num2!=0):
                temp=temp+z
            num2=num2+1
        for y in temp2:
            if(x==y and num3==0):
                temp2[num]="{"
                num3=num3+1
            num=num+1
    return temp
def decrypt(Data,A):
    l=len(Data)
    l2=0
    temp2=[]
    temp=""
    k2=A
    key=[]
    for x in A:
        key.append(x)
    k3=""
    num=0
    num2=0
    row=0
    LK=int(len(key))
    row=int(l/LK)
    for x in key:
        num=0
        num2=0
        for y in key:
            if(x>y):
                x=y
        for y in key:
            if(x==y and num2==0):
                key[num]="{"
                num2=num2+1
            num=num+1
        k3=k3+x
    for x in k3:
        temp2.append(x)
    num=0
    while(l2<l):
        temp=temp+Data[l2]
        l2=l2+1
        if(l2%row==0):
            temp2.append(k3[num]+temp)
            temp=""
            num=num+1
    for x in k2:
        num=0
        num2=0
        for y in temp2:
            if(x==y[0]):
                x=y
        for z in x:
            if(num2!=0):
                temp=temp+z
            num2=num2+1
        for y in temp2:
            if(x==y):
                temp2[num]="{"
            num=num+1
    l2=0
    num=0
    l=int(len(temp))
    Data=""
    col=int(l/LK)
    while(l2<l):
        Data=Data+temp[(l2%col)*LK+num]
        l2=l2+1
        if(l2%col==0):
            num=num+1
    return Data
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