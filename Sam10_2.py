import os

a = os.stat("text.txt").st_size == 0
if a == True:
    print("Файл пустой! ")

b = os.stat("text1.txt").st_size == 0
if b == False:
    file = open("text1.txt", "r")
    print(*file)