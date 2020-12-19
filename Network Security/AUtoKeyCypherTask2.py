#Group 4
#Made by Talha Hussain 51 and Noman Ahmed 42
def decryption2(data,A):
    temp=""
    inc=0
    l=len(A)
    for x in data:
        if(x>="A" and x<="Z"):
            a=ord(x)
            if(inc>=l):
                if(temp[inc-l]==" "):
                    l=l-1
                if(temp[inc-l]>"Z"):
                    b=ord(temp[inc-l])-32
                else:
                    b=ord(temp[inc-l])
                c=(a-b)%26
            else:
                if(A[inc]>"Z"):
                    b=ord(A[inc])-32
                else:
                    b=ord(A[inc])
                c=(a-b)%26
            temp=temp+chr(c+65)
        elif(x>="a" and x<="z"):
            a=ord(x)
            if(inc>=l):
                if(temp[inc-l]==" "):
                    l=l-1
                if(temp[inc-l]<"a"):
                    b=ord(temp[inc-l])+32
                else:
                    b=ord(temp[inc-l])
            if(inc>=l):
                c=(a-b)%26
            else:
                if(A[inc]<"a"):
                    b=ord(A[inc])+32
                else:
                    b=ord(A[inc])
                c=(a-b)%26
            temp=temp+chr(c+97)
        elif(x==" "):
            temp=temp+x
            inc=inc-1
        inc+=1
    return temp
print("Made by group # 4\nNoman Ahmed 42\nTalha Hussain 51")
data="Pvrdl zo xskm xo vm"
Key="work"
print("\nCipher Text: "+data+"\nKey: "+Key+"\nPlain Text: "+decryption2("Pvrdl zo xskm xo vm","work"))
