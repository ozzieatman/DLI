
#Final Version of the Endpoint. Takes an argument as list. 


def numbers_to_add(mRange):
    #Add a check here to ensure the server does not crash.
    if mRange > 10:
        return ("Unable to run; too large")

    mList = list(range(mRange))
    mTotal = 0

    for x in mList:
        mTotal += x

    return (mTotal)