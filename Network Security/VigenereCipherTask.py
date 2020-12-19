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
def getkey(key):
    if(key>="A" and key<="Z"):
        a=ord(key)-65
        return a
    elif(key>="a" and key<="z"):
        a=ord(key)-97
        return a
def affine2(data,A):
    temp=""
    y=Key(A,data)
    inc=0
    for x in data:
        if(x>="A" and x<="Z"):
            a=ord(x)
            c=a-getkey(y[inc])
            if(chr(c)<"A"):
                c=c+26
            temp=temp+chr(c)
        elif(x>="a" and x<="z"):
            a=ord(x)
            c=a-getkey(y[inc])+1
            if(chr(c)>"a"):
                c=c+26
            temp=temp+chr(c)
        elif(x==" "):
            temp=temp+x
        inc+=1
    return temp
print("Made by group # 4\nNoman Ahmed 42\nTalha Hussain 51")
data="OZELNVUXTGWHVUBJLVTYDKURVDVFKPNA"
A="TRYHARD"
print("for text : "+data+" and key : "+A)
print("The decrypted message is:\n"+affine2(data,A))