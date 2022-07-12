dct={}
while(True):
    user = input("what your name: ")
    password = input("what your pass: ")
    if(user=="exit" and password=="exit"):
        break
    dct[user]=password
print(dct)

