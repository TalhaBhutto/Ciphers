def encrypt(Data,key):
    l=len(Data)
    l2=0
    temp=""
    temp2=""
    num=0
    while((l/key)%1):
        l=l+1
        Data=Data+"X"
    col=int(l/key)
    while(l2<l):
        if(num%2==0):
            temp=temp+Data[(l2%key)*col+num]
        else:
            temp2=temp2+Data[(l2%key)*col+num]
        l2=l2+1
        if(l2%key==0):
            num=num+1
    return temp+temp2
data="Lets try another route to secure our the message using transposition cipher"
A=4
print("The encrypted message is:\n"+encrypt(data,A))