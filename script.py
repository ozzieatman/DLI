
#Solution for the test that may be run outside of an Django environent.
#Python3 /directory/script.py



def numbers_to_add():
    mList = list(range(1000))
    mTotal = 0

    for x in mList:
        mTotal += x

    print (mTotal)