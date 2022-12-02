import random
from collections import Counter
s=open('assignment8.2.txt', 'r')
k=(s.readlines())
new=[]
for i in k:
        if '\n' in i:
            new.append(i[:-1])
        else:
            new.append(i)
s.close()
def randoms():
    s=random.choices(new)
    return s
secret_word=randoms()
def game(n):
    new=[]
    check=[]
    for i in n:
        for j in range(len(i)):
            new.append('_')
            check.append(i[j])
    print("WELCOME TO THE HANGMAN GAME")
    print('*'*27)
    print()
    print("The word consist",len(new),'letters')
    print(''.join(new))
    Attempt = 6
    guessed = []
    while Attempt!=0:
        #global Attempt
        li=[]
        letter=input("Guess a letter : ")
        for i in n:
            for j in i:
                li.append(j)
        value = Counter(li)
        if letter.upper() not in guessed:
                guessed.append(letter.upper())
                if letter.upper() in li:
                    k = value[letter.upper()]
                    for i in range(k):
                        k = li.index(letter.upper())
                        new[k] = letter.upper()
                        li[k] = "*"
                    if new==check:
                        print("Congratulations you Won and you successfully guessed the word",''.join(check))
                        Attempt=0
                    else:
                        Attempt-=1
                        print("you made the right guess")
                        print()
                        print(''.join(new))
                        print()
                        print('You have',Attempt,'guess remaining')
                else:
                    print("Invalid Input")
                    print()
                    print(''.join(new))
                    print()
                    Attempt -= 1
                    print('You have', Attempt, 'guess remaining')
        else:
            print("You have already guessed this letter")
    if Attempt==0 and check!=new:
        print()
        print('The Secret Word is',''.join(check))
game(secret_word)
print()
def main():
    print("Do you want to try again \n YES \n NO")
    k=input()
    if k.upper()=='YES':
        print()
        print("Lets Rock & Roll Again ")
        secret_word=randoms()
        game(secret_word)
    else:
        print("Thank you for spending time with us :)")
if __name__=="__main__":
    main()