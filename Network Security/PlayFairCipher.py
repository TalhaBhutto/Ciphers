#Made BY Talha HUssain BHutto
def encrypt(D,K):
    k2=""
    num=0
    l2=0
    pairs=[]
    pairs2=[]
    rows=["","","","",""]
    cols=["","","","",""]
    l=len(D)
    if(l%2==1):
        l+=1
        D=D+"X"
    while(l/2>l2):
        pairs.append(D[l2*2]+D[l2*2+1])
        l2+=1
    for x in K:
        cond=True
        for y in k2:
            if(x==y):
                cond=False
        if(x=="J" and cond):
            cond=False
            k2=k2+"I"
        if(cond):
            k2=k2+x
    table=k2
    while(num<26):
        cond=True
        a=chr(65+num)
        for x in k2:
            if(x==a):
                cond=False
        if(num==9):
            cond=False
        if(cond):
            table=table+a
        num+=1
    num=0
    num2=0
    for x in table:
        rows[num]=rows[num]+x
        cols[num2]=cols[num2]+x
        num2+=1
        if(num2%5==0):
            num+=1
            num2=0
    for x in pairs:
        condr=True
        condc=True
        diag=[]
        for y in rows:
            x0=True
            x1=True
            num=0
            num2=0
            for y1 in y:
                if(x[0]==y1 and num<2):
                    num+=1
                if(x[1]==y1 and num<2):
                    num+=1
            if(num==2):
                for y3 in y:
                    if(x[0]==y3 and x0):
                        x0=False
                        if(num2<4):
                            x=y[num2+1]+x[1]
                        else:
                            x=y[0]+x[1]
                    if(x[1]==y3 and x1):
                        if(num2<4):
                            x1=False
                            x=x[0]+y[num2+1]
                        else:
                            x=x[0]+y[0]
                    num2+=1
                condr=False
        for z in cols:
            x0=True
            x1=True
            num=0
            num2=0
            for z1 in z:
                if(x[0]==z1):
                    num+=1
                if(x[1]==z1):
                    num+=1
            if(num==2):
                for z3 in z:
                    if(x[0]==z3 and x0):
                        x0=False
                        if(num2<4):
                            x=z[num2+1]+x[1]
                        else:
                            x=z[0]+x[1]
                    if(x[1]==z3 and x1):
                        x1=False
                        if(num2<4):
                            x=x[0]+z[num2+1]
                        else:
                            x=x[0]+z[0]
                    num2+=1
                condc=False
        if(x[0]==x[1]):
            x=x[0]+x[1]
        elif(condr and condc):
            row_start=0
            row_end=0
            col_start=0
            col_end=0
            num2=0
            for u in rows:
                num=0
                for u2 in u:
                    if(x[0]==u2):
                        col_start=num
                        row_start=num2
                    elif(x[1]==u2):
                        col_end=num
                        row_end=num2
                    num+=1
                num2+=1
            x=rows[row_start][col_end]+rows[row_end][col_start]
        pairs2.append(x)
    temp=""
    for x in pairs2:
        temp=temp+x
    return temp
def decrypt(D,K):
    k2=""
    num=0
    l2=0
    pairs=[]
    pairs2=[]
    rows=["","","","",""]
    cols=["","","","",""]
    l=len(D)
    if(l%2==1):
        l+=1
        D=D+"X"
    while(l/2>l2):
        pairs.append(D[l2*2]+D[l2*2+1])
        l2+=1
    for x in K:
        cond=True
        for y in k2:
            if(x==y):
                cond=False
        if(x=="J" and cond):
            cond=False
            k2=k2+"I"
        if(cond):
            k2=k2+x
    table=k2
    while(num<26):
        cond=True
        a=chr(65+num)
        for x in k2:
            if(x==a):
                cond=False
        if(num==9):
            cond=False
        if(cond):
            table=table+a
        num+=1
    num=0
    num2=0
    for x in table:
        rows[num]=rows[num]+x
        cols[num2]=cols[num2]+x
        num2+=1
        if(num2%5==0):
            num+=1
            num2=0
    for x in pairs:
        condr=True
        condc=True
        diag=[]
        for y in rows:
            x0=True
            x1=True
            num=0
            num2=0
            for y1 in y:
                if(x[0]==y1 and num<2):
                    num+=1
                if(x[1]==y1 and num<2):
                    num+=1
            if(num==2):
                for y3 in y:
                    if(x[0]==y3 and x0):
                        x0=False
                        if(num2>0):
                            x=y[num2-1]+x[1]
                        else:
                            x=y[4]+x[1]
                    if(x[1]==y3 and x1):
                        if(num2>0):
                            x1=False
                            x=x[0]+y[num2-1]
                        else:
                            x=x[0]+y[4]
                    num2+=1
                condr=False
        for z in cols:
            x0=True
            x1=True
            num=0
            num2=0
            for z1 in z:
                if(x[0]==z1):
                    num+=1
                if(x[1]==z1):
                    num+=1
            if(num==2):
                for z3 in z:
                    if(x[0]==z3 and x0):
                        x0=False
                        if(num2>0):
                            x=z[num2-1]+x[1]
                        else:
                            x=z[4]+x[1]
                    if(x[1]==z3 and x1):
                        x1=False
                        if(num2>0):
                            x=x[0]+z[num2-1]
                        else:
                            x=x[0]+z[4]
                    num2+=1
                condc=False
        if(x[0]==x[1]):
            x=x[0]+x[1]
        elif(condr and condc):
            row_start=0
            row_end=0
            col_start=0
            col_end=0
            num2=0
            for u in rows:
                num=0
                for u2 in u:
                    if(x[0]==u2):
                        col_start=num
                        row_start=num2
                    elif(x[1]==u2):
                        col_end=num
                        row_end=num2
                    num+=1
                num2+=1
            x=rows[row_start][col_end]+rows[row_end][col_start]
        pairs2.append(x)
    temp=""
    for x in pairs2:
        temp=temp+x
    return temp
def Encryption():
    data=input("Enter a message for encryption: ")
    A=input("Enter the KEY : ")
    D=""
    cond=True
    for x in data:
        if(x>="a" and x<="z"):
            x=chr(ord(x)-32)
        elif(x>"z" or x<"A" or (x>"Z" and x<"a")):
            cond=False
        D=D+x
    if(cond):    
        print("The encrypted message is:\n"+encrypt(D,A))
    else:
        print("Invalid Input!!\nEnter alphabets only....")
def Decryption():
    data=input("Enter a message for decryption: ")
    A=input("Enter the KEY : ")
    D=""
    cond=True
    for x in data:
        if(x>="a" and x<="z"):
            x=chr(ord(x)-32)
        elif(x>"z" or x<"A" or (x>"Z" and x<a)):
            cond=False
        D=D+x
    if(cond):    
        print("The encrypted message is:\n"+decrypt(D,A))
    else:
        print("Invalid Input!!\nEnter alphabets only....")
print("Made by Talha Hussain Bhutto")
key=input("Press 1 for Encrypther and any other key for decryption : ")
temp=""
if(key=="1"):
    Encryption()
else:
    Decryption()