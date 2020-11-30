with open("text2.txt") as file:
    data = file.read()
    txt = data.split(" ")
    ls = []
    for i in txt:
        if(len(i) >=4):
            ls.append(i)

    x = " ".join(ls)
    print(x)

with open("text3.txt", 'w') as fi:
    fi.write(x)
