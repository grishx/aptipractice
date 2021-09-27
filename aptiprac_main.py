import libraryapti
import os
print("Hello! \nEnter choices:\n1.Addition Practice\n2.Squares Practice\n3.Cubes Practice")

while(1):
    ip= input(">")
    if ip == "exit":
        print("byee")
        break
    if ip == "cls":
        os.system("cls")


    if ip == "1":
        libraryapti.addprac()
    else:
        continue
