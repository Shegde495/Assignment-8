n=int(input("Enter the number of co-ordinates : "))
li=[]
for i in range(n):
    x,y=map(int,(input("Enter the co_ordinates in x,y format: ").split(',')))
    li.append((x,y))
check_x_negative=sorted(li)
check_y_negative=sorted(li, key=lambda x:x[1])
if check_x_negative[0][0]<=0 or check_y_negative[0][1]<=0:
    li2 = []
    for i in li:
        new = []
        for j in i:
            if j == 0 or j < 0 or j > 0:
                j = j + 8
                new.append(j)
        li2.append(tuple(new))
    print("The set of positive co_ordinates ")
    print(li2)

else:
    print("All Co-ordinates are positive")
