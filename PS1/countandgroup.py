def item_order(order):
    salad = 0
    hamburger = 0
    water = 0

    startspace = 0
    space = 0

    while space > -1:
        space = order.find(' ', startspace)
        if space == -1:
            word = order[startspace:]
        else:
            word = order[startspace:space]
        if word == 'salad':
            salad += 1
        if word == 'hamburger':
            hamburger += 1
        if word == 'water':
            water += 1
        startspace = space + 1
    neworder = "salad:"+str(salad)+" hamburger:"+str(hamburger)+" water:"+str(water)
    return neworder
