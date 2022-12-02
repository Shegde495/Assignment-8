
import random
secret_number=random.randint(1000,10000)
secret_number=str(secret_number)
print("Welcome to the game")
count=0
while True:
    choice=input("Enter a four digit number")
    li1=[]
    li2=[]
    c=0
    b=0
    for i in choice:
        li1.append(i)
    for j in secret_number:
        li2.append(j)
    if li1==li2:
        count=count+1
        print('Congratulations , you took',count,'attempts to guess the number')
        break
    for i in li1:
        if i in li2:
            if li1.index(i)==li2.index(i):
                c=c+1
            else:
                b=b+1
    print(c,'cow',',',b,'bull')
    count=count+1


