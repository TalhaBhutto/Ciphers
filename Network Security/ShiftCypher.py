#Group 4
#Made by Talha Hussain 51 and Noman Ahmed 42
def shift(y1):
    y=int(y1)
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
print("Made by group # 4\nNoman Ahmed 42\nTalha Hussain 51")
data="Zlkdoxqrixqflk vlk plisba qeb pefcq zfmebo"
temp=""
for y in range(26):
    print(shift(str(y)))
print("\nThe key is 3")
print("\nThe message is :"+shift("3"))
print("\nThank your sir! ^.^")
print("Made by group # 4\nNoman Ahmed 42\nTalha Hussain 51")

