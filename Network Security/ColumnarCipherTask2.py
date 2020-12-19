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
data="LETSTRYCOLUMNARCIPHERTOSECUREOURTHEMESSAGE"
A="MANGO"
print("The encrypted message is:\n"+encrypt(data,A))
print(encrypt(data,A))
print("Made by group # 4\nNoman Ahmed 42\nTalha Hussain 51")
