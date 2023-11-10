dict = {"a":"1","b":"2","c":"3"}

for i in dict:
    if i == "a":
        print("Si estaba a")
    if i != "d":
        print("No estaba d")
        break

for i,j in dict:
    print(i,j)