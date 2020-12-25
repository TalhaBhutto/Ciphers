def encrypt(D,K):
    l=len(D)
    l3=0
    k2=(K-1)*2
    k3=0
    num2=0
    num3=0
    temp=""
    while(l>0):
        if((l3+num3+1)>len(D)):
            l3+=1
            num3=0
            num2=0
            if(l3+1==K):
                k2=k3=(K-1)*2
            else:
                k2=k2-2
                k3=k3+2
        else:
            if(num2==0):
                temp=temp+D[l3+num3]
                num3=num3+k2
                if(l3>0 and l3<K):
                    num2+=1
            else:
                temp=temp+D[l3+num3] 
                num3=num3+k3
                num2-=1
            l-=1
    return temp
def decrypt(D,K):
    temp=[]
    l=len(D)
    l2=0
    l3=0
    k2=(K-1)*2
    k3=0
    num2=0
    num3=0
    for x in D:
        temp.append(x)
    while(l>l2):
        if((l3+num3+1)>len(D)):
            l3+=1
            num3=0
            num2=0
            if(l3+1==K):
                k2=k3=(K-1)*2
            else:
                k2=k2-2
                k3=k3+2
        else:
            if(num2==0):
                temp[l3+num3]=D[l2]
                num3=num3+k2
                if(l3>0 and l3<K):
                    num2+=1
            else:
                temp[l3+num3]=D[l2] 
                num3=num3+k3
                num2-=1
            l2+=1
    D=""
    for x in temp:
        D=D+x
    return D
def Encryption():
    data=input("Enter a message for encryption: ")
    A=int(input("Enter the KEY : "))
    print("The encrypted message is:\n"+encrypt(data,A))
def Decryption():
    data=input("Enter a message for decryption: ")
    A=int(input("Enter the KEY : "))
    print("The decrypted message is:\n"+decrypt(data,A))
print("Made by group # 4\nNoman Ahmed 42\nTalha Hussain 51")
key=input("Press 1 for Encrypther and any other key for decryption : ")
temp=""
if(key=="1"):
    Encryption()
else:
    Decryption()