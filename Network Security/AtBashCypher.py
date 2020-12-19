#Group 4
#Made by Talha Hussain 51 and Noman Ahmed 42
def bash():
    temp=""
    for x in data:
        if(x>="A" and x<="Z"):
            a=2*ord("M")-ord(x)+1
            temp=temp+chr(a)
        elif(x>="a" and x<="z"):
            a=2*ord("m")-ord(x)+1
            temp=temp+chr(a)
        elif(x==" "):
            temp=temp+x
    return temp
data=input("Please enter a message : ")
print("\nThe message is after ATBash is : "+bash())
print("Made by group # 4\nNoman Ahmed 42\nTalha Hussain 51")