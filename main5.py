dct = {}
while (True):
    user = input("what your name: ")
    password = input("what your pass: ")
    if (user == "exit" and password == "exit"):
        break
    if (user in dct):
        print("user already exist")
    else:
        dct[user] = password
myuser=input("muser? ")
if(myuser in dct):
    print(dct[myuser])
else:
    print("user not exist")
