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
data="WE HAVE STUDIED THE THREE DIFFERENT TECHNIQUES OF TRANSPOSITION CIPHERS"
A=5
print("The encrypted message is:\n"+encrypt(data,A))