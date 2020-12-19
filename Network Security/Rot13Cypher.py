#Group 4
#Made by Talha Hussain 51 and Noman Ahmed 42
def R13():
    y=13
    temp=""
    for x in data:
        if(x>="A" and x<="Z"):
            a=ord(x)
            c=a-65
            c=(c+y)%26
            c=65+c
            temp=temp+chr(c)
        elif(x>="a" and x<="z"):
            a=ord(x)
            c=a-97
            c=(c+y)%26
            c=97+c
            temp=temp+chr(c)
        elif(x==" "):
            temp=temp+x
    return temp
data=input("Please enter a message : ")
print("\nThe message is after ROT13Cypher is : "+R13())
print("Made by group # 4\nNoman Ahmed 42\nTalha Hussain 51")