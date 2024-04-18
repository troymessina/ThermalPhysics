def iterate():
    # create solid
    L = 10
    for i in range(13):
        # sample solid to obtain distribution
        # calculate entropy and store it
        # plot distribution
        L = L*2
        solid.exchange(L)
    # plot entropy as a function of L
