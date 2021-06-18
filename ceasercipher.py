#encoding function and decoding function
def converter(inputtext,k):
    text=""
    for i in inputtext:
        if i!=" ":
            text=text+chr((ord(i)+(k)))
        else:
            text=text+" "
    return text

print("NOTE:This algorithm is ascii based encoding and decoding")
print("===============================================================================================================================================")
while True:
    a=1
    while a:#loop for valid choice
            try:

                codetype=int(input("enter \n1 for encoding \n2 for decoding\n3 to exit\nyour choice: "))
                print("===============================================================================================================================================")
                a=0
            except:
                print("Enter Valid input")
    a=1
    if codetype==3:#exit to main
        print("Thank you for using Caesar Cipher")
        break
    if codetype>3:
        print("Enter a valid choice i.e 1 or 2 or 3")
        a=0
        continue


    while a:#loop for valid key
        try:
            key=int(input("enter key(Example:+5,+6,-1,-5): "))
            a=0
        except:
            print("Enter Valid Key")

    if codetype==1:#encoding processs
        pt=input("enter plain text: ")
        ct=converter(pt,key)
        print("Cipher text is: ",ct)
        codetype=3

    if codetype==2:#decoding process
        ct=input("enter Cipher text: ")
        k=-1*key
        pt=converter(ct,k)
        print("Plain text is: ",pt)
        codetype=3

    if codetype==3:#exit to main
        print("Your key is '",key,"'\n make sure you use same key for decoding")
        print("Thank you for using Caesar Cipher")
        print("===============================================================================================================================================")
        break
