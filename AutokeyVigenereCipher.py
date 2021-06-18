dict_alpha={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
dict_numer={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}

def encoding(pt,key):
    ct=""
    j=0
    for i in range(0,len(pt)):
        if pt[i]!=" ":
            val=(dict_alpha[pt[i]]+dict_alpha[key[j]])%26
            ct=ct+dict_numer[val]
            j+=1
        else:
            ct=ct+" "

    return(ct)

def decoding(ct,key):
    pt=""
    j=0
    for i in range(0,len(ct)):
        if ct[i]!=" ":
            val=dict_alpha[ct[i]]-dict_alpha[key[j]]
            if val<0:
                val=val+26
            pt=pt+dict_numer[val]
            key=key+dict_numer[val]
            j+=1
        else:
            pt=pt+" "

    return(pt)

def alphatest(text):
    try:
        for i in text:
            if (((ord(i)>=ord('a') and ord(i)<=ord('z')) or (ord(i)>=ord('A') and ord(i)<=ord('Z'))or i==" ")!=True):
                raise ValueError()
        text=text.lower()
        return text
    except :
        print("Enter only alphabets")
        return('fail')

def keytest(text):
    try:
        for i in text:
            if (((ord(i)>=ord('a') and ord(i)<=ord('z')) or (ord(i)>=ord('A') and ord(i)<=ord('Z')))!=True):
                raise ValueError()
        text=text.lower()
        return text
    except :
        print("Enter only alphabets")
        return('fail')

def leng(text):
    size=len(text)
    for i in text:
        if i==" ":
            size-=1
    return(size)

def tq():
    print("Thank you ")
    print("===============================================================================================================================================")

def textadjust(text):
    t=""
    for i in text:
        if i!=" ":
            t=t+i
    return t

def keyadjust(key,text):
    size=len(text)-len(key)
    size+=1
    key=key+text[:size]
    return(key)


print("===============================================================================================================================================")
print("AutoKey Vigenere Cipher is a purely alphabetical cipher and it is not case sensitive")

a=1
while a:
    print("===============================================================================================================================================")
    a=1
    while a:#loop for valid choice
            try:
                codetype=int(input("enter \n1 for encoding \n2 for decoding\n3 to exit\nyour choice: "))
                print("===============================================================================================================================================")
                a=0
            except:
                print("Enter Valid input")

    if codetype==3:
        tq()
        break


    if codetype==1:
        b=1
        while b:
            pt=input("Eneter plain text: ")
            pt=alphatest(pt)
            b=0
            if pt=='fail':
                b=1

        b=1
        while True:
            while b:
                length=leng(pt)
                key=input("Enter the key: ")
                okey=key
                key=keytest(key)
                b=0
                if key=='fail':
                    b=1

            if length>len(key):
                key=keyadjust(key,textadjust(pt))
            ct=encoding(pt,key)
            print("Cipher text:  ",ct)
            print("Key: ",okey)
            print("Note:Use the same Key for decryption")
            tq()
            break



    if codetype==2:
        b=1
        while b:
            ct=input("Eneter Cipher text: ")
            ct=alphatest(ct)
            b=0
            if ct=='fail':
                b=1

        b=1
        while True:
            while b:
                length=leng(ct)
                key=input("Enter the key: ")
                key=keytest(key)
                b=0
                if key=='fail':
                    b=1

            pt=decoding(ct,key)
            print("Plain text:  ",pt)
            tq()
            break
