dict_alpha={}

def encoding(pt):
    ct=""
    for i in pt:
        if i!=" ":
            ct=ct+dict_alpha[i]
        else:
            ct=ct+" "
    return(ct)

def decoding(ct):
    pt=""
    for i in ct:
        if i!=" ":
            pt=pt+return_key(i)
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



def tq():
    print("Thank you ")
    print("===============================================================================================================================================")

def keyred(key):
  lst=[]
  nkey=""
  for i in key:
    if i not in nkey:
      nkey=nkey+i
  return nkey

def keygen(key):
    dict_alpha['a']=key[0]
    lst=[]
    lst.append(key[0])
    j=1
    br=97
    for i in range(98,123):
        if j<len(key):
            if key[j] not in lst:
                dict_alpha[chr(i)]=key[j]
                lst.append(key[j])
            else:
                j=j+1
                dict_alpha[chr(i)]=key[j]
                lst.append(key[j])
            j=j+1
        else:
          f=1
          for k in range(br,123):
            if chr(k) not in lst:
              dict_alpha[chr(i)]=chr(k)
              lst.append(chr(k))
              br=k
              break

def return_key(val):
    for key, value in dict_alpha.items():
        if value==val:
            return key
    return('Key Not Found')



print("===============================================================================================================================================")
print("Keyword Cipher is a purely alphabetical cipher and it is not case sensitive")
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
                key=input("Enter the key: ")
                okey=key
                key=keytest(key)
                b=0
                if key=='fail':
                    b=1


            keygen(keyred(key))
            print(dict_alpha)
            ct=encoding(pt)
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
                key=input("Enter the key: ")
                key=keytest(key)
                b=0
                if key=='fail':
                    b=1
            keygen(keyred(key))
            pt=decoding(ct)
            print("Plain text:  ",pt)
            tq()
            break
