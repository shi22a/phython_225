



prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

profit =0
for x in prices:
    for y in stock:
        if x==y:
            profit += prices[x]*stock[y]
print(profit)



