dct={}
while(True):
    user = input("what your name: ")
    password = input("what your pass: ")
    if(user=="exit" and password=="exit"):
        break
    if (user in dct):
        print("user already exist")
    else:
        dct[user] = password
lst=[]
lst2=[]
for item in dct:
    lst.append(item)
    lst2.append(dct[item])
print(lst)
print(lst2)

