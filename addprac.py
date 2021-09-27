

import random
import os

def addprac():
    lB=10
    hB=99
    no_of_no=5
    state=""
    score= 0
    count= 0

    while(1):
        state=input(">").lower()
        if (state=="exit"):
            break

        elif (state=="lb"):
            lB=int(input(">>Enter lower bound "))

        elif (state=="hb"):
            hB=int(input(">>Enter higher bound  "))

        elif (state=="nn"):
            no_of_no=int(input(">>Enter number of numbers  "))

        elif (state=="score"):
            print(score,"/",count)
            print("accuracy = ", float(score)/float(count) * 100,"%")

        else:
            addition=0
            for i in range(0,no_of_no):
                n=random.randint(lB, hB)
                addition += n
                print(n)

            ans=int(input(">Enter answer_____\b\b\b\b"))
            count= count+1

            if ans==addition:
                print("Correct Answer!!")
                score = score +1
                print("score is: ", score,"/",count)


            elif ans != addition:
                print("Nope :( answer is ", addition)
                print("Your score is:  ", score,"/",count)






