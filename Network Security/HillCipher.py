#Made By Talha Hussain  Bhutto B17158051
def encrypt(data,key):
    if(len(key)!=4):
        return "lenght of key must be of 4 letters"
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
        if(data[l1*2]>="a" and data[l1*2]<="z"):
            a=ord(data[l1*2])-97
        elif(data[l1*2]>="A" and data[l1*2]<="Z"):
            a=ord(data[l1*2])-65
        elif (data[l1*2+1]>="A" and data[l1*2+1]<="Z"):
            b=ord(data[l1*2+1])-65
        else:
            return "Plese enter characters from A-Z or a-z"
        if (data[l1*2+1]>="A" and data[l1*2+1]<="Z"):
            b=ord(data[l1*2+1])-65
        elif(data[l1*2+1]>="a" and data[l1*2+1]<="z"):
            b=ord(data[l1*2+1])-97
        else:
            return "Plese enter characters from A-Z or a-z"
        temp.append([a,b])
        l1+=1
    temp2=[]
    for x in key:
        if(x<="Z" and x>="A"):
            temp2.append(ord(x)-65)
        elif(x<="z" and x>="a"):
            temp2.append(ord(x)-97)
        else:
            return "key can only contain alphabets"
    det=0
    det=temp2[0]*temp2[3]-temp2[1]*temp2[2]
    if(det==0):
        return "Inverse not possible!!"
    else:
        det=26-(det%26)
    temp3=[1,2,3,4]
    temp3[0]=(temp2[3]*det)%26
    temp3[3]=(temp2[0]*det)%26
    temp3[1]=26-(temp2[1]*det)%26
    temp3[2]=26-(temp2[2]*det)%26
    l1=0
    l2=0
    while(l1<len(temp)):
        l2=(temp2[0]*temp[l1][0]+temp2[1]*temp[l1][1])%26
        temp[l1][1]=(temp2[2]*temp[l1][0]+temp2[3]*temp[l1][1])%26
        temp[l1][0]=l2
        l1+=1
        l2=0
    data=""
    for x in temp:
        data=data+chr(x[0]+65)+chr(x[1]+65)
    return data
def decrypt(data,key):
    if(len(key)!=4):
        return "lenght of key must be of 4 letters"
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
        if(data[l1*2]>="a" and data[l1*2]<="z"):
            a=ord(data[l1*2])-97
        elif(data[l1*2]>="A" and data[l1*2]<="Z"):
            a=ord(data[l1*2])-65
        elif (data[l1*2+1]>="A" and data[l1*2+1]<="Z"):
            b=ord(data[l1*2+1])-65
        else:
            return "Plese enter characters from A-Z or a-z"
        if (data[l1*2+1]>="A" and data[l1*2+1]<="Z"):
            b=ord(data[l1*2+1])-65
        elif(data[l1*2+1]>="a" and data[l1*2+1]<="z"):
            b=ord(data[l1*2+1])-97
        else:
            return "Plese enter characters from A-Z or a-z"
        temp.append([a,b])
        l1+=1
    temp2=[]
    for x in key:
        if(x<="Z" and x>="A"):
            temp2.append(ord(x)-65)
        elif(x<="z" and x>="a"):
            temp2.append(ord(x)-97)
        else:
            return "key can only contain alphabets"
    det=0
    det=temp2[0]*temp2[3]-temp2[1]*temp2[2]
    if(det==0):
        return "Inverse not possible!!"
    else:
        det=26-(det%26)
    a=temp2[0]
    temp2[0]=(temp2[3]*det)%26
    temp2[3]=(a*det)%26
    temp2[1]=26-(temp2[1]*det)%26
    temp2[2]=26-(temp2[2]*det)%26
    l1=0
    l2=0
    while(l1<len(temp)):
        l2=(temp2[0]*temp[l1][0]+temp2[1]*temp[l1][1])%26
        temp[l1][1]=(temp2[2]*temp[l1][0]+temp2[3]*temp[l1][1])%26
        temp[l1][0]=l2
        l1+=1
        l2=0
    data=""
    for x in temp:
        data=data+chr(x[0]+65)+chr(x[1]+65)
    return data
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
key=input("Press 1 for Encrypther and any other key for decryption : ")
temp=""
if(key==1):
    Encryption()
else:
    Decryption()
