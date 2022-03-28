def mostActive(customers):
    numberOfTrades = customers[0]
    trades = dict()

    for cust in customers[1:]:
        count = trades.get(cust)
        if count:
            trades[cust] = count + 1
        else:
            trades[cust] = 1

    topFive = list()
    for k, v in trades.items():
        if (v / numberOfTrades)*100 > 5:
            topFive.append(k)

    for c in sorted(topFive):
        print(c)


def getInter(a,b):
    print(set(a).intersection(b))

def main():
    #test = (4, 'a', 'a', 'b', 'c')
    a, b = ['a', 'b', 'g', 'r'], ['e', 'g', 'l', 1, 'w']
    x = set(a)
    y = set(b)
    print(x.union(y))

    #print(x)
    #getInter(a,b)
    #mostActive(test)

if __name__ == '__main__':
    main()