open_brackets=['[','{','(']
close_brackets=[']','}',')']
s=input("Enter the string : ")
li=[]
for i in s:
    if i in close_brackets:
        if len(li)>0:
            if close_brackets.index(i)==open_brackets.index(li[-1]):
                li.pop()
                flag=1
            else:
                print("Invalid string")
                flag=0
                break
        else:
            print("Invalid string")
            flag=0
            break
    else:
        li.append(i)
        flag = 1
if flag==1:
    if len(li)==0:
        print("Valid String")
    else:
        print("Invalid String")
