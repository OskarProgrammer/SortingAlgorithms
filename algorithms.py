import random

class Sort(object):
   
    def quickSort(self, array: list) -> list:
        if len(array) <= 1:
            return array
        else:
            pivot = array[0]
            greater = [x for x in array if x>pivot ]
            less = [x for x in array if x<pivot ]
            return self.quickSort(less) + [pivot] + self.quickSort(greater)
    
    def bumbleSort(self, array: list) -> list:
        i = 1
        while i != 0:
            i = 0
            for x in range(len(array)):
                try:
                    if array[x] > array[x+1]:
                        mem = array[x]
                        array[x],array[x+1] = array[x+1], mem
                        i += 1
                except IndexError:
                    pass
        return array
    
    def insertSort(self, array: list):
        n = len(array)

        if n<=1:
            return

        for x in range(1, n):
            current = array[x]
            previousIndex = x-1
            while previousIndex >= 0 and current < array[previousIndex]:
                array[previousIndex + 1] = array[previousIndex]
                previousIndex -= 1

            array[previousIndex + 1] = current

sort = Sort()

randomList = [random.randrange(-20,100) for x in range(100)]

print(sort.quickSort(randomList))
print(sort.bumbleSort(randomList))

randomList = [random.randrange(-20,100) for x in range(100)]

sort.insertSort(randomList)
print(randomList)