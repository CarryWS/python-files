string = 'a'*100000
G = int(input('写入几G:'))
with open('a.txt','w') as f:
    for i in range(G):
        for i in range(10786):
            f.write(string)
