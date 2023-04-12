input = int(input())

x = [input]
y = [input]

count = 0
while(True):
    length = len(x)
    for i in x:
        if i==1:
            print(count)
            exit(0)
        else:
            if i%3==0:
                y.append(int(i/3))
            if i%2==0:
                y.append(int(i/2))
            y.append(i-1)
    count += 1
    y = y[length:]
    x = list(y)