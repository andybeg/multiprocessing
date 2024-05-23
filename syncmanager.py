import multiprocessing as mp
import time

def demoFunc(targetDict, targetList):
    counter = 0
    while True:
        targetDict[1] = '1'
        targetDict['2'] = counter
        targetDict[0.25] = None
        targetList.reverse()
        counter += 1

if __name__ == '__main__':
    with mp.Manager() as manager:
        myDict = manager.dict()
        myList = manager.list(range(10))

        p = mp.Process(target=demoFunc, args=(myDict, myList))
        p.start()
        while True:
            print(myDict)
            time.sleep(1)

        p.join()

        print(myDict)
        print(myList)